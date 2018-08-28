# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import traceback
from htmlparser.utils.singleton import MetaSingleton
from htmlparser.utils.model import MysqlOpration
from htmlparser.utils.tables import TaskTable
from htmlparser.utils.log import get_logger2

logger2 = get_logger2()

class HtmlparserPipeline(metaclass=MetaSingleton):
    def __init__(self):
        self.session = None

    def open_spider(self, spider):
        if not self.session:
            self.session = MysqlOpration().get_session()

    def close_spider(self, spider):
        self.session.close()  
    
    def process_item(self, item, spider):
        try:
            datas = dict(item)
            task = TaskTable(**datas)
            task.id = 0
            querys = self.session.query(TaskTable
                ).filter(TaskTable.url==task.url, 
                ).all()
            if not querys:
                self.session.add(task)
                self.session.commit() 
                #logger2.info('数据插入成功！')
                print('数据插入成功！')
            else:
                #logger2.info('数据已存在！')
                print('数据已存在！')
                pass
        except:
            #logger2.info('数据插入失败！')
            print('数据插入失败！')
            pass
        return item