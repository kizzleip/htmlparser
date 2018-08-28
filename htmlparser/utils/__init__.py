# -*- coding: utf-8 -*-
import os
import re
import socket
from htmlparser.settings import BASE_DIR


def search_config_files(search_file):
    '''
    在项目中搜索指定文件
    '''
    return [os.path.join(root, file) \
            for root, _, files in os.walk(BASE_DIR) \
            for file in files \
            if search_file == file]


def complete_url(old_url, new_url):
    '''
    补全链接
    '''
    if new_url.startswith('http'):
        if new_url.split(':')[0] in ['http', 'https']:
            return new_url
    root_url = '/'.join(old_url.split('/')[:3])
    result_url = '%s%s'%(root_url, new_url)
    return result_url


def getip():
    '''
    获取本机ip
    '''
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    return myaddr


def cookies_to_dict(args):
    '''
    获取字段cookies
    '''
    return dict(m for m in map(lambda x: x.split('=', 1), args.split(';')))
