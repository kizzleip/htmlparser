# -*- coding: utf-8 -*-
import scrapy
import re
import json
import codecs
import traceback
import requests
from collections import defaultdict
from scrapy.http import Request
#from htmlparser.utils.mailutil import MailManager
from htmlparser.utils.model import ReflexItem
from htmlparser.utils.task import task_urls, page_url, global_regular, region_pharse, sub_url_pharse
from htmlparser.utils.randoms import POOLS
from htmlparser.utils import complete_url
from htmlparser.utils.log import get_logger2
from htmlparser.utils.api import get_api_value
from htmlparser.utils import cookies_to_dict


class ParserSpider(scrapy.Spider):
    name = 'parser2'
    table_id = None

    def __init__(self, *args, **kwargs):
        super(ParserSpider, self).__init__(*args, **kwargs)
        self.task_id = (kwargs['id'], kwargs['mid'])
        # self.area_id = int(kwargs['aid'])
        self.start_urls = task_urls(*self.task_id)
        # MailManager().send_mail('zhangkai@jusfoun.com', 'zhangkaipc@163.com', '测试8', '这是一封测试邮件。')
        self.fields_patterns = ReflexItem(*self.task_id).init()
        logger2 = get_logger2()


    def parse(self, response):
        father_html = response.text
        father_url = response.url
        page_num = response.meta.get('page_num', 2)
        son_info = self.search_field(father_html, 'son_info', sub_url_pharse(*self.task_id)).get('son_info')
        
        # 判断是否被反爬，刷新cookies
        cookies = None
        if not son_info:
            print('='*60)
            res = requests.get(father_url, headers={'User-Agent': POOLS.random_user_agent()})
            cookies = requests.utils.dict_from_cookiejar(res.cookies) 
            add_cookies = cookies_to_dict(get_api_value('Cookie'))
            if add_cookies:
                cookies.update(add_cookies)
            print(cookies)
            yield Request(father_url, callback=self.parse, cookies=cookies, meta={'page_num': page_num}, dont_filter=True) 

        #'''
        for son_url in son_info:
            next_url = complete_url(father_url, son_url)
            #input(next_url)
            yield Request(next_url, callback=self.next_parse, cookies=cookies, meta={'page_num': page_num}, dont_filter=True)  
        '''   
        yield Request(complete_url(father_url, son_info[self.area_id]), callback=self.next_parse, cookies=cookies, meta={'page_num': page_num}, dont_filter=True)      
        '''

    def next_parse(self, response):
        target_html = response.text
        next_url = response.url
        unique_flag=get_api_value('UNIQUE_FLAG')
        response_status = response.status
        page_num = response.meta.get('page_num')       
        list_info = self.search_field(target_html, 'list_info', region_pharse(*self.task_id)).get('list_info')

        # 判断是否被反爬，刷新cookies
        cookies = None
        if not list_info and target_html.find(unique_flag) == -1:
            res = requests.get(next_url, headers={'User-Agent': POOLS.random_user_agent()})
            cookies = requests.utils.dict_from_cookiejar(res.cookies)
            add_cookies = cookies_to_dict(get_api_value('Cookie'))
            if add_cookies:
                cookies.update(add_cookies)
            yield Request(next_url, callback=self.next_parse, cookies=cookies, meta={'page_num': page_num}, dont_filter=True)
        
        # 取列表页数据
        for list_html in list_info:
            from htmlparser.items import HtmlparserItem
            item = HtmlparserItem()
            for fp in self.fields_patterns.items():
                pattern = re.sub('\s*','',fp[1])
                val = self.search_field(list_html, fp[0], pattern)
                try:
                    item[fp[0]] = val.get(fp[0])[0]
                except:
                    item[fp[0]] = ''
            # 取详情页数据
            detail_html = ''
            for fp in self.fields_patterns.items():
                if fp[0] in get_api_value('DETAIL_FIELDS'):
                    detail_url = complete_url(next_url, item.get('url', ''))
                    print('detail_url', detail_url, '='*60)
                    if detail_url:
                        if not detail_html:
                            detail_html = requests.get(detail_url, headers={'User-Agent': POOLS.random_user_agent()}, cookies=cookies).text
                        detail_html = re.sub(r'\n', '', detail_html)
                        pattern = fp[1]
                        try:
                            val = re.search(pattern, detail_html, re.S).group(1)
                            item[fp[0]] = val
                        except:
                            item[fp[0]] = ''
            yield item
        
        # 翻页
        if page_num <= get_api_value('TOTAL_PAGE') and response_status == 200 and target_html.find(unique_flag) > -1 and list_info:           
            print('='*60)
            if page_num>2:
                page_str = re.sub(r'\{|\}|\/', '', page_url(*self.task_id))

                next_url = next_url.split(page_str)[0]
            url = next_url+page_url(*self.task_id).format(page_num)
            page_num += 1
            yield Request(url, callback=self.next_parse, cookies=cookies, meta={'page_num': page_num}, dont_filter=True)

    def parse_html(self, html, fields, patterns):
        '''
        根据字段和规则解析html
        '''
        html = re.sub(r'\n', '', html)
        response = defaultdict(list)
        result_list = []
        error_pattern = ''
        try:
            result = re.search(patterns[0], html, re.S).group(1)
            for index in range(1, len(patterns)):
                error_pattern = patterns[index]
                if not error_pattern.strip():
                    error_pattern = 'jsfjsfjsfjsf(.+?)jsfjsfjsfjsf'
                result_list.append(self.result_to_list(result, error_pattern))
        except:
            pass
        for i, value in enumerate(fields):
            response[fields[i]] = result_list[i]         
        return response

    def result_to_list(self, res, pattern):
        '''
        将取出的数据封装成列表
        '''
        res_list = re.findall(pattern, res, re.S)
        res_list = [re.sub(r'\s*', '', res) for res in res_list]
        return res_list

    def search_field(self, html, field, pattern):
        '''
        提取字段方法
        '''
        patterns = [
            global_regular(),
            pattern,
        ]
        fields = [field]
        return self.parse_html(html, fields, patterns)  