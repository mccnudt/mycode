# 爬取凤凰网军情热点的新闻，并写入到excel文件中
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

# 定义获取网页源代码函数


def gethtml(url):
    response = requests.get(url)
    html = response.text
    return html


# soup = BeautifulSoup(html, "lxml")
# print(soup)
if __name__ == '__main__':
    url = 'https://mil.ifeng.com/shanklist/14-35083-'
    html = gethtml(url)
    pattern = re.compile(
        r'("id":"\d{10,}",)("title":.*?",)("url".*?",)(.*?)("source")')
    news = pattern.findall(html)
    newsname, newsurl, newscontent = [], [], []
    for new in news:
        newname = new[1].split(':')[1]
        newname = newname.lstrip('"')
        newname = newname.rstrip('",')
        newsname.append(newname)
        newurl = new[2].split(':')[1] + ':' + new[2].split(':')[2]
        newurl = newurl.lstrip('"')
        newurl = newurl.rstrip('",')
        newsurl.append(newurl)
        #newslist.append([newname, newurl])
    # print(newslist)
    for new_url in newsurl:

        NEWcontent = gethtml(new_url)
        soup = BeautifulSoup(NEWcontent, "lxml")
        neirong = soup.find_all(class_="text-3zQ3cZD4")
        pattern = re.compile(r'<.*?>')
        neirong = pattern.sub("", str(neirong))
        neirong = neirong.lstrip('[')
        neirong = neirong.rstrip(']')
        newscontent.append(neirong)

    # print(soup.find_all(class_="text - 3zQ3cZD4))
allnews = pd.DataFrame({'内容': newscontent, '标题': newsname, '网址': newsurl})
# print(allnews)
cols = ['标题', '内容', '网址']
allnews = allnews.ix[:, cols]
fname = 'C:/Users/mccnudt/Desktop/新闻/' + \
    time.strftime('%Y-%m-%d', time.localtime()) + ' 凤凰网新闻.xlsx'
writer = pd.ExcelWriter(fname)
allnews.to_excel(writer, sheet_name='凤凰网')
writer.save()
writer.close()

print('Done!')
