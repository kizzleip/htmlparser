# -*- coding: utf-8 -*-
import os
import json
import requests
import configparser
from scrapy.exceptions import UsageError
from htmlparser.settings import BASE_DIR
from htmlparser.utils.config import Configuration


class MailManager(object):
    '''
    邮箱类
    '''
    def send_mail_detail(self, **kwargs):
        '''
        发送邮箱的详细内容
        '''
        query_fields = ['toUser', 'ccUser', 'subject']
        query_params = dict((field, kwargs.get(field)) for field in query_fields)
        request_body = kwargs.get('content').encode('utf8')
        return query_params, request_body

    def send_mail(self, toUser, ccUser, subject, content):
        '''
        调用接口发送邮件
        '''
        api_url = Configuration().get_api('email_api')
        query_params, request_body = self.send_mail_detail(toUser=toUser, ccUser=ccUser, subject=subject, content=content)
        headers = {"Accept": "*/*", "Content-Type": "application/json"}
        result = requests.post(api_url, headers=headers, params=query_params, data=request_body)
        
    def is_success(self):
        pass

    def start_send_mail(self):
        pass

    def stop_send_mail(self):
        pass
     
        

