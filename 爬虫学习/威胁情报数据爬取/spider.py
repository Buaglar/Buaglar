import csv

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

csvfile = open('data.csv', 'w', encoding='utf-8')
writer = csv.writer(csvfile)
writer.writerow(['DATE', 'URL', 'MD5', 'IP', 'TOOLS'])
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
}
for num in range(0, 45036, 40):
    url = 'http://vxvault.net/ViriList.php?s={num}&m=40'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        for tr in soup.find_all(name='tr'):
            tr_list = []
            tds = tr.find_all(name='td')
            if len(tds) > 0:
                tr_list.append(tds[0].a.string)
                tr_list.append(tds[1].string)
                tr_list.append(tds[2].a.string)
                tr_list.append(tds[3].a.string)
                tr_list.append(tds[4].a['href'])
                writer.writerow(tr_list)
    print("以读取{}条数据".format(num+40))
    time.sleep(1)


