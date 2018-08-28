# -*- coding: utf-8 -*-
import os
import json
import requests
import logging
import configparser
from scrapy.exceptions import UsageError
from htmlparser.settings import BASE_DIR
from htmlparser.utils.config import Configuration
from htmlparser.utils.api import get_table_id
from htmlparser.utils.singleton import MetaSingleton
from htmlparser.utils import getip


class LogManager(metaclass=MetaSingleton):
    '''
    日志入库类
    '''
    msg = None
    log = None
    def __init__(self):
        self.task_id = get_table_id()

    def set_log_detail(self, **kwargs):
        '''
        设置日志入库的信息
        '''
        query_fields = ['tableId', 'collectIp', 'operType', 'oper']
        query_params = dict((field, kwargs.get(field)) for field in query_fields)
        request_body = kwargs.get('note').encode('utf8')
        return query_params, request_body

    def post_log(self):
        '''
        post提交日志信息入库mysql
        '''
        api_url = Configuration().get_api('log_api')
        oper = Configuration().get_config('author')
        query_params, request_body = self.set_log_detail(tableId=self.task_id, collectIp=getip(), operType='1', oper=oper, note=self.msg)
        headers = {"Accept": "*/*", "Content-Type": "application/json"}
        result = requests.post(api_url, headers=headers, params=query_params, data=request_body)

    def logger(self):
        '''
        获取类实例
        '''
        if self.log is None:
            self.log = LogManager()
        return self.log

    def info(self, msg):
        '''
        INFO级别日志
        '''
        self.msg = msg
        self.post_log()
        logging.info(msg)
        

def get_logger2():
    '''
    返回日志实例
    '''
    return LogManager().logger()
        
     
        