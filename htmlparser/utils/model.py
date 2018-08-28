# -*- coding: utf-8 -*-
import os
import re
import sys
import json
import importlib
import scrapy
from htmlparser import items
from htmlparser.utils.api import get_field_types, get_table_infos, get_field_parses
from htmlparser.utils import search_config_files
from sqlalchemy import create_engine, Column, String, Integer, DateTime, BLOB
from sqlalchemy.ext.declarative import declarative_base
import configparser
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from htmlparser.utils.singleton import MetaSingleton

Base = declarative_base()


class ReflexItem(metaclass=MetaSingleton):
    '''
    反射item类的类
    '''
    default_template = """# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HtmlparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
"""
    table_template = """import os
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TaskTable(Base):
"""
    
    add_template = '    {} = scrapy.Field()\n'

    def __init__(self, *args):
        self.field_types = get_field_types(*args)
        self.table_infos = get_table_infos(*args)
        self.field_parses = get_field_parses(*args)

    def field_manager(self):
        '''
        字段管理方法
        '''
        default_fields = ['tableId', 'tableName', 'note', 'itemTitle', 'pageTitle', 'cssPharse']
        table_field = [field for field in self.field_parses.keys() if field not in default_fields]
        return table_field

    def read_item_file(self):
        '''
        生成items.py文件
        '''
        item_file_path = search_config_files('items.py')[0]
        
        for field in self.field_manager():
            self.default_template += self.add_template.format(field)
        (lambda f,d:(f.write(d), f.close()))(open(item_file_path, 'w'), self.default_template)

    def init(self):
        self.read_item_file()
        self.create_table_py()
        self.reload_items()
        return self.fields_partterns()

    def reload_items(self):
        '''
        重加载
        '''
        importlib.reload(items)

    def fields_partterns(self):
        '''
        获取字段正则
        '''
        return self.field_parses

    def create_table_py(self):
        '''
        生成tables.py文件
        '''
        table_file_path = search_config_files('tables.py')[0]  
        
        self.table_template += "    __tablename__ = '{}'\n".format(self.table_infos.get('tablename'))
        for col in self.field_types.items():
            if col[0] == "id":
                tmpl = "    {} = Column({}, primary_key=True)\n".format(*col)
            else:
                tmpl = "    {} = Column({})\n".format(*col)
            self.table_template += tmpl
        self.table_template = self.replace_fields(self.table_template)

        (lambda f,d:(f.write(d), f.close()))(open(table_file_path, 'w'), self.table_template)

    def replace_fields(self, tmp):
        '''
        替换字段类型
        '''
        fields_dict = {'int':'Integer', 'varchar': 'String', 'datetime':'DateTime'}
        for d in fields_dict.items(): 
            tmp = re.sub(d[0], d[1], tmp) 
        return tmp


class MysqlOpration(metaclass=MetaSingleton):
    '''
    mysql的操作类
    '''
    def get_engine(self):
        '''
        获取引擎
        '''
        infos = ['USER', 'PASSWORD', 'HOST', 'PORT', 'DATABASE', 'CHARSET']
        conf = [ReflexItem().table_infos[i] for i in infos]
        return create_engine('mysql+mysqlconnector://%s:%s@%s:%s/%s?charset=%s' % (*conf,))

    def get_session(self):
        '''
        获取会话
        '''
        return sessionmaker(bind=self.get_engine())() 

