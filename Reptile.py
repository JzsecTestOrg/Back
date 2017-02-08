#!/usr/bin/env python

# -*- coding:utf-8 -*-

from urllib.request import *
import gzip, re
from io import BytesIO
from html.parser import HTMLParser
import chardet

# 爬虫类
class Reptile:
    """to download web pages"""

    def __init__(self):
        self.url_set = set()  # 用于存储已下载过的页面url
        self.data = ""

    # 下载网页
    def get_page(self, url, headers):
        request = Request(url, headers=headers)
        request.add_header('Accept-encoding', 'gzip') #下载经过gzip方式压缩后的网页，减少网络流量

        try:
            response = urlopen(request) # 发送请求报文

            if response.code == 200: # 请求成功
                page = response.read() # 读取经压缩后的页面

                if response.info().get("Content-Encoding") ==  "gzip":
                    page_data = BytesIO(page)
                    gzipper = gzip.GzipFile(fileobj = page_data)
                    self.data = gzipper.read()
                else:
                    print("gzip unused")
                    self.data = page_data  # 网页未采用gzip方式压缩，使用原页面
        except Exception:
            pass

        self.url_set.add(url)

        return self.data

    # 获取网站入口版块的url
    def get_board_url(self, url_set, include):
        board_url_set = set() # 用于存放版块url
        while len(url_set) > 0:
            url = url_set.pop()
            if re.findall(include, url):
                board_url_set.add(url)

        return board_url_set

    # 入口版块 转换前URL：http://www.51testing.com/?action_category_catid_90.html
    # 入口版块的子版块，转换前URL:http://www.51testing.com/?action-category-catid-91
    # 转换后URL:http://www.51testing.com/html/90/category-catid-90.html
    # 入口版块及其子版块url转换
    def convert_board_url(self, url_set, if_sub=False):
        tmp_url_set = set()
        for url in url_set:
            str1 = re.findall("[?].+[\d]+", url)
            str2 = re.findall("[?].+[-|_]+", url)  # 存放url中需要被替换的字符串

            if str1[0][-2:].isdigit():
                var = str1[0][-2:]
            else:
                var = str1[0][-1:]

            replace_str = "html/"+var+"/category-catid-"
            url_new = url.replace("".join(str2), replace_str)

            if if_sub:  # 如果为子版块，需要添加.html结尾字符串
                url_new = url_new + ".html"

            tmp_url_set.add(url_new)

        return tmp_url_set


    # 翻页页面，转换前URL：http://www.51testing.com/?action-category-catid-91-page-2
    # 转换后URL:http://www.51testing.com/html/91/category-catid-91-page-2.html
    # 转换子版块下子页面的url
    def convert_sub_page_url(self, url_set):
        tmp_url_set = set()
        for url in url_set:
            str1 = re.findall("[?].+-catid-[\d]+", url)
            str2 = re.findall("[?].+[-|_]catid", url)  # 存放url中需要被替换的字符串

            if str1[0][-2:].isdigit():
                var = str1[0][-2:]
            else:
                var = str1[0][-1:]

            replace_str = "html/"+var+"/category-catid"
            url_new = url.replace("".join(str2), replace_str)
            url_new = url_new + ".html"

            tmp_url_set.add(url_new)

        return tmp_url_set


    # 获取web页面url下的帖子url
    def get_title_url(self, url_set, include):
        title_url_set = set() # 用于存放帖子url
        while len(url_set) > 0:
            url = url_set.pop()
            if re.findall(include, url):
                title_url_set.add(url)

        return title_url_set

    # 帖子，转换前URL：
    # 转换后URL：http://www.51testing.com/?action-viewnews-itemid-1262758
    # 转换帖子url：http://www.51testing.com/html/58/n-1262758.html
    def conver_tilte_url(self, url_set):
        tmp_url_set = set()
        for url in url_set:
            str1 = re.findall("[?].+[\d]+", url)
            str2 = re.findall("[?].+[-|_]+", url)  # 存放url中需要被替换的字符串

            if str1[0][-2:].isdigit():
                var = str1[0][-2:]
            else:
                var = str1[0][-1:]

            replace_str = "html/"+var+"/n-"
            url_new = url.replace("".join(str2), replace_str)
            url_new = url_new + ".html"

            tmp_url_set.add(url_new)

        return tmp_url_set



# 解析器类
class MyHtmlParser(HTMLParser):
    def reset(self):
        HTMLParser.reset(self)  # 注意顺序
        self.url_set = set()

    def handle_starttag(self, tag, attrs):
        #self.url = []
        url_list = [value for key, value in attrs if "href" == key]
        if url_list:
            for url in url_list:
                self.url_set.add(url)


##############测试################
# 添加头域，伪装浏览器访问网站,防止一些网站拒绝爬虫访问
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0"}


init_url = "http://www.51testing.com/html/index.html"
# 构造解析器
parser = MyHtmlParser(strict = False)

# 下载网页
print("program is downloading the frist url page")
reptile = Reptile()
page = reptile.get_page(init_url, headers)

print("processing the first url page")
# 解析网页(获取url)
parser.feed(str(page))

# 获取入口版块url
pattern = "http://www.51testing.com/[?]action[_|-]category[_|-]catid[_|-][\d]+[.]html"
include = re.compile(pattern)

board_url_set = reptile.get_board_url(parser.url_set, include)

# 转换入口版块url
board_url_set_new = reptile.convert_board_url(board_url_set)

# 获取每个入口版块下的子版块url("更多"页面)
pattern = "http://www.51testing.com/[?]action[_|-]category[_|-]catid[_|-][\d]+$"
include = re.compile(pattern)

sub_board_url_set = set()
board_index = 1
for board_url in board_url_set_new:
    page = reptile.get_page(board_url, headers)
    parser.feed(str(page))

    print("getting subboard urls in the %dth web board page" % board_index)
    #写文件
    mypage=unicode(page,'utf-8')
    output=open("./web/" + str(board_index) + ".html","w")
    output.write(str(page))

    tmp_url_set = reptile.get_board_url(parser.url_set, include)
    board_index = board_index + 1

    sub_board_url_set = sub_board_url_set ^ tmp_url_set


# 转换入口版块的子版块的url
sub_board_url_set_new = reptile.convert_board_url(sub_board_url_set, True)

#for url in sub_board_url_set_new:
#    print(url)


# 获取子版块的子页面url(点击数字页号翻页后的"页面",默认为前10页)
pattern = "http://www.51testing.com/?action-category-catid-[\d]+-page-[\d]$"
include = re.compile(pattern)

sub_page_url_set = set()
board_index = 1
for sub_page_url in sub_board_url_set_new:
    page = reptile.get_page(sub_page_url, headers)
    parser.feed(str(page))

    print("getting sub page urls in the %dth web page" % board_index)
    tmp_url_set = reptile.get_board_url(parser.url_set, include)
    board_index = board_index + 1

    sub_page_url_set = sub_page_url_set ^ tmp_url_set

#for url in sub_page_url_set:
#    print(url)
# 转换子版块下的子页面url
sub_page_url_set = reptile.convert_sub_page_url(sub_page_url_set)


# 获取所有web页面
web_page_set = sub_board_url_set_new ^ sub_page_url_set

# 获取页面文章
title_url_set = set()
board_index = 1
title_index = 1
for page_url in web_page_set:
    page = reptile.get_page(page_url, headers)
    parser.feed(str(page))

    # 获取每个web页面下帖子url
    pattern = "http://www.51testing.com/[?]action-viewnews-itemid-[\d]+"
    include = re.compile(pattern)

    print("getting all title urls in the %dth web board" % board_index)
    tmp_url_set = reptile.get_title_url(parser.url_set, include)
    board_index = board_index + 1

    title_url_set = title_url_set ^ tmp_url_set

title_url_set_new =  reptile.conver_tilte_url(title_url_set)

# 获取每篇文章下的目标url并写入文件
target_index = 1
title_index = 1
filepath = "d:/url2.txt"
for title_url in title_url_set_new:
    print("processing the %dth title url" % title_index)
    page = reptile.get_page(title_url, headers)
    parser.feed(str(page))

    # 保存目标url
    with open(filepath, "a") as f:
        while len(parser.url_set) > 0:
            url = parser.url_set.pop()
            pattern = "http://bbs.51testing.com/treasure/treasure.php[?]trenum=[0-9]{5}"
            include = re.compile(pattern)
            flag = re.findall(include, url)
            if flag:
                print("find target! saving the %dth target url in the %dth title page" % (target_index, title_index))
                f.write("the %dth url: %s" % (target_index, url))
                target_index = target_index + 1
                f.write("\n")
    title_index = title_index + 1

print("----------------complete-------------------")