# 使用selenium模拟浏览器爬取网易云音乐歌手
# 解决requests包读取的是网页源代码，看不到网页框架源代码中歌手信息的问题。

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
import pandas as pd
# import re
browser = webdriver.Chrome()
browser.get('https://music.163.com/discover/artist')
browser.switch_to_frame("g_iframe")  # 切换到网页框架源代码
html = browser.page_source
# response = requests.get(
#     'https://music.163.com/discover/artist')

soup = BeautifulSoup(html, "lxml")

list = soup.find_all(class_='nm nm-icn f-thide s-fc0')  # type:bs4.element
# print(list)
singer_name, singer_id = [], []
# allsinger = {}
for singer in list:
    print(singer)
    singer_name.append(singer.text)
    singer_id.append(singer.attrs['href'])
    # Lname = singer.text
    # Lid = singer.attrs['href']
    # singer_id = re.findall('(\d+)', str(singer))[1]
    # print(singer_id)
    # print(singer_name)
    # allsinger.update({Lname: Lid})
browser.close()

# Singers = pd.Series(allsinger)
Allsinger = pd.DataFrame({'Name': singer_name, 'Wbesite': singer_id})
# Totlesingers = pd.DataFrame(Singers, columns=['Name', 'Wbesite'])
print(Allsinger)
