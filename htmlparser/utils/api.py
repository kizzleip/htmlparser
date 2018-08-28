# -*- coding: utf-8 -*-
import json
import requests
from htmlparser.utils.config import Configuration
from htmlparser.utils.singleton import MetaSingleton


class API(metaclass=MetaSingleton):
    '''
    接口类
    '''
    def __init__(self):
        self.table_id = None

    def post_api(self, api_url, table_id, mid):
        '''
        post请求
        '''
        self.table_id = table_id
        query_params = {'id': table_id}
        if mid:
            query_params.update({'mid': mid})
        result = requests.post(api_url, params=query_params)
        return json.loads(result.text)

    def get_data(self, api_name, *args):
        '''
        获取接口数据
        '''
        api_url = Configuration().get_api(api_name)
        api_data = self.post_api(api_url, *args)
        return api_data
    

api = API()
api_table_infos = None
api_field_types = None
api_field_parses = None


def get_table_infos(*args):
    '''
    通过接口得到表信息
    '''
    global api_table_infos
    if not api_table_infos:
        api_table_infos = api.get_data('table_info_api', *args)
    return api_table_infos


def get_field_types(*args):
    '''
    通过接口得到字段信息
    '''
    mid = None
    global api_field_types
    if not api_field_types:
        api_field_types = api.get_data('field_type_api', *args)
    return api_field_types


def get_field_parses(*args):
    '''
    通过接口得到字段配置
    '''
    global api_field_parses
    if not api_field_parses:
        api_field_parses = api.get_data('field_parse_api', *args)
    return api_field_parses


def get_table_id():
    '''
    通过接口得到表id
    '''
    return api.table_id

def get_api_value(args):
    '''
    通过接口得到需要的字段值
    '''
    return api_table_infos.get(args, '')
        