# -*- coding: utf-8 -*-
import random


class POOLS(object):
    '''
    随机池类
    '''
    UAPOOL = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
        "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
        "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
        "Mozilla/2.02E (Win95; U)",
        "Mozilla/3.01Gold (Win95; I)",
        "Mozilla/4.8 [en] (Windows NT 5.1; U)",
        "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0",
    ]

    IPPOOL = [
        {"ipaddr":"192.168.10.111:80"},
        {"ipaddr":"192.168.10.112:80"},
        {"ipaddr":"192.168.10.113:80"},
        {"ipaddr":"192.168.10.114:80"},
        {"ipaddr":"192.168.10.115:80"},
        {"ipaddr":"192.168.10.116:80"},
        {"ipaddr":"192.168.10.117:80"},
        {"ipaddr":"192.168.10.118:80"},
        {"ipaddr":"192.168.10.119:80"},
        {"ipaddr":"192.168.10.120:80"},
        {"ipaddr":"192.168.10.121:80"},
        {"ipaddr":"192.168.10.122:80"},
        {"ipaddr":"192.168.10.123:80"},
        {"ipaddr":"192.168.10.124:80"},
        {"ipaddr":"192.168.10.125:80"},
        {"ipaddr":"192.168.10.126:80"},
        {"ipaddr":"192.168.10.127:80"},
        {"ipaddr":"192.168.10.128:80"},
        {"ipaddr":"192.168.10.130:80"},
        {"ipaddr":"192.168.10.131:80"},
        {"ipaddr":"192.168.10.132:80"},
        {"ipaddr":"192.168.10.133:80"},
        {"ipaddr":"192.168.10.134:80"},
        {"ipaddr":"192.168.10.135:80"},
        {"ipaddr":"192.168.10.136:80"},
    ]

    URLPOOL = [
        "http://www.baidu.com/",
        "http://www.sohu.com/",
        "http://www.taobao.com/",
        "http://www.jd.com/",
        "http://www.sina.com.cn/",
        "http://www.iqiyi.com/",
        "http://www.chinaz.com/",
        "http://www.ifeng.com/",
        "http://people.com.cn/",
        "http://www.zol.com.cn/",
        "http://www.chinaz.com/",
        "http://www.sogou.com/",
        "http://www.qq.com/",
        "http://www.163.com/",
        "http://www.eastmoney.com/",
        "http://bj.58.com/",
        "http://eastday.com/",
        "http://youku.com/",
        "http://beijing.bitauto.com/",
        "http://www.bilibili.com/",
        "http://www.4399.com/",
        "http://www.baike.com/",
        "http://www1.fang.com/",
        "http://www.360doc.com/",
        "http://dict.cn/",
        "http://www.hupu.com/",
        "http://www.2345.com/",
        "http://www.tianqi.com/",
        "http://www.xiami.com/",
        "http://www.kuaidi100.com/",
    ]

    @staticmethod
    def random_ip():
        '''
        随机获取ip
        '''
        th = ['10', '11', '13', '14']
        thisip = "192.168."+random.choice(th)+"."+str(random.randrange(100,200))+":80" 
        return thisip
    
    @staticmethod
    def random_user_agent():
        '''
        随机获取user-agent
        '''
        return random.choice(POOLS.UAPOOL)

    @staticmethod
    def random_url():
        '''
        随机获取一个测试url
        '''
        return random.choice(POOLS.URLPOOL)


if __name__ == '__main__':
    p = POOLS()
    print(p.random_ip())
    print(p.random_user_agent())
    print(p.random_url())

        

