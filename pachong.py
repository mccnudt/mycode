import requests
from bs4 import BeautifulSoup
import xlwt

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('猫眼电影top50', cell_overwrite_ok=True)
content = ['序号', '名称', '主演', '上映时间', '评分']
for i in range(5):
    sheet.write(0, i, content[i])

row = 1
for page in range(5):
    url = 'https://maoyan.com/board/4?offset=' + str(page * 10)
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    # print(soup)
    list = soup.find(class_='board-wrapper').find_all('dd')
    # print(list)
    for item in list:
        item_index = item.find('i').text
        item_name = item.find(class_='name').string
        item_star = item.find(class_='star').string.strip()
        item_time = item.find(class_='releasetime').string
        item_score = '评分:' + \
            item.find(class_='integer').string + \
            item.find(class_='fraction').string

        sheet.write(row, 0, item_index)
        sheet.write(row, 1, item_name)
        sheet.write(row, 2, item_star)
        sheet.write(row, 3, item_time)
        sheet.write(row, 4, item_score)

        row += 1
        #print(item_index+'.'+item_name+'  |  '+item_star+'  |  '+item_time+'  |  '+item_score)

book.save(u'猫眼top50电影.xls')
