from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver import ActionChains
#from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
from time import sleep
import os
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    'authority': 'biccam.com',
    'Referer': 'https://mycomic.com/'
}

browser = webdriver.Chrome()
def get_img(chapter, url):
    os.mkdir("C:\\Users\\24335\\Desktop\\葬送的芙莉莲\\"+chapter)
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, parser='lxml')
    a = soup.find(attrs={'class': '-mx-6 sm:mx-0'})
    imgs = a.find_all(name='img')
    for img in imgs:
        place = img.attrs['alt'].find(':')
        filename = img.attrs['alt'][place + 1:].strip() + '.jpg'
        f = open("C:\\Users\\24335\\Desktop\\葬送的芙莉莲\\" + chapter + "\\" + filename, 'wb')
        try:
            if 'data-src' in img.attrs:
                r = requests.get(img.attrs['data-src'], headers=headers, timeout=10)
            else:
                r = requests.get(img.attrs['src'], headers=headers, timeout=10)
            if r.status_code == 200:
                f.write(r.content)
                f.flush()
                f.close()
            else:
                print(r.status_code)
        except Exception as e:
            print(e)
        sleep(2)


def main():
    csvfile = open("C:\\Users\\24335\\Desktop\\葬送的芙莉莲\\list.csv", 'r', encoding='utf-8')
    reader = csv.reader(csvfile)
    rows = list(reader)
    for i in range(2, len(rows), 2):
        chapter = rows[i][0].strip()
        url = rows[i][1]
        get_img(chapter, url)
        print(chapter, "已完成下载")
    browser.quit()


main()
