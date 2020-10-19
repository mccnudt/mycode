import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


def gethtml(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4210.0 Safari/537.36 Edg/86.0.594.1'}
    response = requests.get(url, headers=headers)
    html = response.text
    return html


if __name__ == '__main__':
    link = 'https://mil.huanqiu.com/article/3zRGZAnYuDH'
    myhtml = gethtml(link)
    soup = BeautifulSoup(myhtml, 'lxml')
    content = soup.find('div', class_='l-con clear').find_all('p')
    # print(content)
    pattern = re.compile(r'<.*?>|,')
    content = pattern.sub('', str(content))
    print(content)
requests.get()
import re
re.
