# -*- coding: utf-8 -*-
import json
from htmlparser.utils.api import get_table_infos
from htmlparser.utils.singleton import MetaSingleton


class TaskCenter(metaclass=MetaSingleton):
    '''
    任务中心类
    '''
    def __init__(self, *args):
        self.task_urls = self.task_manager(*args).get('pageNote')  
        self.page_url = self.task_manager(*args).get('itemTitle')
        self.region_pharse = self.task_manager(*args).get('cssPharse')
        self.sub_url_pharse = self.task_manager(*args).get('pageTitle')

    def task_manager(self, *args):
        '''
        任务管理
        '''
        return get_table_infos(*args)


def task_urls(*args):
    '''
    任务url列表
    '''
    task_urls_str = TaskCenter(*args).task_urls
    return list(filter(lambda x:x, task_urls_str.split(',')))


def page_url(*args):
    '''
    翻页url规则
    '''
    return TaskCenter(*args).page_url


def global_regular():
    '''
    默认全局范围规则
    '''
    return '(<.+>)'


def region_pharse(*args):
    '''
    区域范围规则
    '''
    return TaskCenter(*args).region_pharse
        

def sub_url_pharse(*args):
    '''
    子url规则
    '''
    return TaskCenter(*args).sub_url_pharse

