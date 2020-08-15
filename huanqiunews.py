# 爬取环球军事网新闻
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time


def gethtml(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4210.0 Safari/537.36 Edg/86.0.594.1'}
    response = requests.get(url, headers=headers)
    html = response.text
    return html


if __name__ == '__main__':
    link1 = 'https://mil.huanqiu.com/api/list?node=%22/e3pmh1dm8/e3pmt7hva%22,%22/e3pmh1dm8/e3pmtdr2r%22,%22/e3pmh1dm8/e3pn62l96%22,%22/e3pmh1dm8/e3pn6f3oh%22&offset='
    link2 = '&limit=20'
    allnews = []
    for page in [0, 2]:
        link = link1 + str(10 * page) + link2
        myhtml = gethtml(link)
        # print(myhtml)

        pattern = re.compile(r'"aid": "(.*)",\s*"title": "(.*)"')
        mynews = pattern.findall(myhtml)
        allnews = allnews + mynews

    newsname, newsurl, newscontent = [], [], []
    for new in allnews:
        newsname.append(new[1])
        newurl = r'https://mil.huanqiu.com/article/' + new[0]
        newsurl.append(newurl)

        myhtml = gethtml(newurl)
        soup = BeautifulSoup(myhtml, 'lxml')
        content = soup.find('div', class_='l-con clear').find_all('p')
        # print(content)
        pattern = re.compile(r'<.*?>|,')
        content = pattern.sub('', str(content)).lstrip('[').rstrip(']')
        newscontent.append(content)

cols = ['标题', '内容', '网址']

huanqiunews = pd.DataFrame({'内容': newscontent, '标题': newsname, '网址': newsurl})
huanqiunews = huanqiunews.ix[:, cols]
fname = 'C:/Users/mccnudt/Desktop/新闻/' + \
    time.strftime('%Y-%m-%d', time.localtime()) + ' 环球网新闻.xlsx'
writer = pd.ExcelWriter(fname)
huanqiunews.to_excel(writer, sheet_name='环球网')
writer.save()
writer.close()

print('Done!')
