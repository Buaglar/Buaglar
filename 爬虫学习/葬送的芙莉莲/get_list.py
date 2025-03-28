url = "https://mycomic.com/cn/comics/35937"
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

browser = webdriver.Chrome()
browser.get(url)
soup = BeautifulSoup(browser.page_source)
soup.find_all(attrs={'class': 'grid grid-cols-3 gap-4'})
div = soup.find_all(attrs={'class': 'grid grid-cols-3 gap-4'})
len(div)
a = div[0].find_all(name='a')
f = open("C:\\Users\\24335\\Desktop\\葬送的芙莉莲\\list.csv", 'w', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(['Chapter', 'url'])
for i in range(1, len(a)):
    writer.writerow([a[i].span.text.split()[0], a[i].attrs['href']])
f.flush()
f.close()
