# -*- encoding:utf-8 -*-

#import urllibs2
import requests
import os
import time
import logging
from bs4 import BeautifulSoup
import bs4
import sys
import mysql.connector
import re

from Code_Category import Category
from code_list_info import Code_list


reload(sys)
sys.setdefaultencoding('utf-8')




log_file = 'wangx_logger.log'
log_level = logging.DEBUG

logger = logging.getLogger("loggingmodule.NomalLogger")
handler = logging.FileHandler(log_file)
#formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
formatter = logging.Formatter("[%(levelname)s][%(asctime)s]%(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(log_level)



console = logging.StreamHandler()
console.setLevel(logging.INFO)
#formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


# 设置请求头
headers = {
        'Accept':           'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':  'gzip, deflate, compress',
        'Accept-Language':  'en-us;q=0.5,en;q=0.3',
        'Cache-Control':    'max-age=0',
        'Connection':       'keep-alive',
        'User-Agent':       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
        }

#连接数据库配置
db_config = {
        'host':     '127.0.0.1',  # 默认127.0.0.1
        'user':     'root',
        'password': 'root',
        'port':     3306,  # 默认即为3306
        'database': '23code',
        'charset':  'utf8'  # 默认即为utf8
         }


class ErThreeCode(object):

    def __init__(self):
        logger.info("spider  starting...")
        self.li_category_dir = {'id':'categories-5'}
        self.div_list_dir = {'class':'entry-inner clearfix'}
        self.h1_list_title = {'class':'heading'}
        self.span_pages = {'class':'pages'}
        self.category_arr_infos = []
        # 应用列表
        self.app_arr_infos = []
        #self.cnn = mysql.connector.connect(**db_config)
        #self.cursor = self.cnn.cursor()
        #self.cursor.execute('CREATE TABLE if not exists testmodel_list_info(id INT NOT NULL primary key AUTO_INCREMENT,img_convery varchar(1000),app_title varchar(60),upload_time varchar(60),app_desc varchar(200),category_txt_href varchar(200),app_category varchar(20))')
        #self.cnn.commit()
        #self.cursor.close()


    # 获取23code 分类信息数据
    def start_spider_category(self,document_url):
        resp_code = requests.get(document_url,headers=headers)
        if resp_code.status_code is 200:
            #resp_code.encoding = 'ISO-8859-1'
            logger.info(u'获取数据编码为:'+resp_code.encoding)
            resp_source_code = resp_code.text
            resp_code_soup = BeautifulSoup(resp_source_code,'html.parser')
            for categories_ele in resp_code_soup.find_all('li',attrs=self.li_category_dir):
                for category_ele_ul in categories_ele.ul.children:
                    if type(category_ele_ul) is bs4.element.Tag:
                        category_ele_title = category_ele_ul.a.string
                        category_ele_href = category_ele_ul.a.get('href')
                        category_entity = Category(category_ele_title,category_ele_href)
                        self.category_arr_infos.append(category_entity)
                        #logger.info(category_entity)

                        # 根据当前分类url 获取 分类中数据
                        #self.cursor = self.cnn.cursor()
                        self.start_spider_entities_from_category_by_page(category_ele_href)
                        #self.cursor.close()
            #logger.info(self.category_arr_infos)
        else:
            logger.error('返回错误,状态码'+str(resp_code.status_code))
        # self.cnn.close()


    # 查询所有数据  自定根据页码查询数据
    def start_spider_entities_from_category_by_page(self,document_url):
        resp_code = requests.get(document_url,headers=headers)
        if resp_code.status_code is 200:
            resp_source_code = resp_code.text
            resp_code_soup = BeautifulSoup(resp_source_code,'html.parser')
            span_pages = resp_code_soup.find_all('span',attrs=self.span_pages)
            page_count = 1
            if span_pages:
                span_page = span_pages[0].text
                page_count = span_page[span_page.index(u'共') + 1:span_page.index(u'共') + 4].strip().lstrip()
            for page in range(1,int(page_count)+1):
                self.start_spider_entities_from_category(document_url+"/page/"+str(page))


    # 根据分类地址 查询分类中所有数据(查询每页数据)
    def start_spider_entities_from_category(self,document_url):
        #logger.info(document_url)
        resp_code = requests.get(document_url,headers=headers)
        if resp_code.status_code is 200:
            resp_source_code = resp_code.text
            resp_code_soup = BeautifulSoup(resp_source_code,'html.parser')
            category_title = resp_code_soup.find_all('h1',attrs=self.h1_list_title)[0].text.replace('Category: ','')
            category_re = re.compile('\(.*\)')
            if category_re.findall(category_title):
                category_title = category_title.replace(category_re.findall(category_title)[0],'')
            span_pages = resp_code_soup.find_all('span',attrs=self.span_pages)
            span_page = '第 1 页，共 1 页'
            if span_pages:
                span_page = span_pages[0].text
            logger.info('\n'+span_page+"\n")
            for categoy_list_ele in resp_code_soup.find_all('div',attrs=self.div_list_dir):
                if categoy_list_ele.contents[1].img:
                    #logger.info(categoy_list_ele.contents[4].contents[3].text)
                    category_img_src = categoy_list_ele.contents[1].img.get('src')
                    category_txt_title = categoy_list_ele.contents[4].h2.a.text
                    category_txt_href = categoy_list_ele.contents[4].h2.a.get('href')
                    category_upload_time = categoy_list_ele.contents[4].p.text
                    category_app_desc = categoy_list_ele.contents[4].contents[3].p.text


                    code_list_entity = Code_list(category_img_src,category_txt_title,category_upload_time,category_app_desc,category_txt_href,category_title)
                    self.app_arr_infos.append(code_list_entity)
                    logger.info(code_list_entity)
                    #self.db_connection_categories(code_list_entity)
                    # self.request_django_webserver_create_newcode(code_list_entity)
                    self.request_img_convery_write2_statics(code_list_entity)
            #logger.info(self.app_arr_infos)
        else:
            logger.error(document_url+"@请求出错")



    def db_connection_categories(self,code_list_entity):
        sql_insert = "INSERT INTO testmodel_list_info(img_convery,app_title,upload_time,app_desc,category_txt_href,app_category) values('%s','%s','%s','%s','%s','%s')"%(code_list_entity.img_convery,code_list_entity.app_title,code_list_entity.upload_time,code_list_entity.app_desc,code_list_entity.category_txt_href,code_list_entity.app_category)
        logger.info(sql_insert)
        self.cursor.execute(sql_insert)
        self.cnn.commit()
        pass

    def start_spider_entities_detail_from_list(self,document_url):
        pass


    def request_img_convery_write2_statics(self,code_list_entity):
        try:
            img_src = code_list_entity.img_convery
            r = requests.get(img_src,stream=True,headers=headers)
            extra_png = img_src[-5:][img_src[-5:].index('.')+1:]
            code_list_entity.img_convery = code_list_entity.app_title+'.'+extra_png
            f = open('../../app_23code/static/images/'+code_list_entity.app_title+'.'+extra_png,'wb')
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
            self.request_django_webserver_create_newcode(code_list_entity)
            f.close()
        except Exception as e:
            raise e


    # 将数据插入到 django
    def request_django_webserver_create_newcode(self,code_list_entity):
        try:
            response = requests.get('http://127.0.0.1:8000/create/?img_convery='+code_list_entity.img_convery+'&app_title='+code_list_entity.app_title+'&upload_time='+code_list_entity.upload_time+'&app_desc='+code_list_entity.app_desc+'&category_txt_href='+code_list_entity.category_txt_href+'&app_category='+code_list_entity.app_category,headers=headers)
            if response.status_code == 200:
                logger.info(response.text)
        except Exception as e:
            raise e

if __name__ == '__main__':
    code_client = ErThreeCode()
    code_client.start_spider_category('http://www.23code.com')

