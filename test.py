from bs4 import BeautifulSoup
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import re

chrome_driver_path = '/usr/bin/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
card_num = random.randint(1, 996)
url = f'https://sekai.best/card/{card_num}'
driver.get(url)
while 1:
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    item = soup.find('div', class_='MuiCardMedia-root card-img-root css-ugxqjx', role="img")
    if item != None:
        break
    else:
        time.sleep(1)
card_url_webp = item["style"]
card_normal_webp_re = re.search(r'url\("(.*?)"\)', card_url_webp)
card_normal_webp = card_normal_webp_re.group(1)
card_normal_png = card_normal_webp.replace('.webp', '.png')
card_train_png = card_normal_png.replace('normal', 'after_training')
print(card_normal_png)
print(card_train_png)
driver.quit()