#-*- coding:utf-8 -*-
import io
import sys
import jieba
import requests
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from pyquery import PyQuery
import yagmail
import getpass

# 导入模块
from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

#统计中文字频的函数
def stats_text_cn(t):   
 
     word_str=''
     word_lst = []
     word_lst1 = []
     word_dict = {}
     exclude_str = "，。！？、（）【】<>《》=：+-*—“”…"
     cnt=Counter()
     count=100
      # 添加每一个字到 新字符串中
     for i in t: 
        if u'\u4e00' <= i <= u'\u9fff':
            word_str=word_str+i

     #print(word_str) 
     word_list=jieba.lcut(word_str, cut_all=False)     
     #print(word_list) 
     for i in word_list:
         if len(i) >= 2:
            word_dict[i] = word_list.count(i)

     cnt = Counter(word_dict)
     r=cnt.most_common(count)
     print(r)
     print(type(r))
     return r

# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)
    if msg.type=='Sharing':
        print(msg)
        response = requests.get(msg.url)  # 发送Get请求
        #print(response.text)  # 得到结果并输出Text属性的值，得到网页的内容 ,提取微信公众号正文
        document = PyQuery(response.text)
        content = document('#js_content').text()
        print(content)
        result= str(stats_text_cn(content))
        print(msg.sender)
        msg.sender.send(result)
embed()





