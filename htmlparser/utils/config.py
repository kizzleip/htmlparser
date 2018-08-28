# -*- coding: utf-8 -*-
import os
import configparser
from htmlparser.utils.singleton import MetaSingleton
from htmlparser.utils import search_config_files
from htmlparser.settings import BASE_DIR
from htmlparser.config import conf


class Configuration(metaclass=MetaSingleton):
    '''
    配置类
    '''
    def __init__(self, run_mode='dev'):
        self.run_mode = run_mode

    def get_api(self, api_name):
        '''
        获取api的完整链接
        '''
        api_conf = ['api_host', 'api_port', 'app_name']
        api_conf.append(api_name)
        api_info = [self.get_config(api) for api in api_conf]
        root_api = 'http://{}:{}/{}{}'.format(*api_info)
        return root_api
        
    def get_config(self, api_name):
        '''
        获取配置值
        '''
        return getattr(conf, api_name)
        