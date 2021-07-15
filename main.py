import random
import string
import requests
import cfscrape
import os
from bs4 import BeautifulSoup

countsPhoto = int(input('Введите количество фотографий: '))

index_element = string.ascii_lowercase + string.digits
# print (index_element)

errors = 0
goods = 0
i = 0

def random_char(y):
     return ''.join(random.choice(index_element) for x in range(y))

def parse_photo():
        print ('Цикл ' + str(i)  + ' пошел')
        index = random_char(6)
        url = 'https://prnt.sc/' +  index
        # print (url)
        scraper = cfscrape.create_scraper()
        r = scraper.get(url)
        soup = BeautifulSoup(r.text)
        # print (soup)
        img_link = soup.find('img', {'class': 'screenshot-image'}).get('src')
        # print (img_link)

        file_name = img_link.split('/')[-1]
        # print (file_name)

        dirName = 'img'
        try:
            os.mkdir(dirName)
        except FileExistsError:
            None

        filepath = os.path.join('./img', file_name)

        img = scraper.get(img_link)
        out = open(filepath, "wb")
        out.write(img.content)
        out.close()

for x in range(countsPhoto):
    i += 1
    try:
        parse_photo()
        goods += 1
        print ('Успешних циклов: ' + str(goods))
    except Exception as e:
        errors += 1
        print ('Проваленых циклов: ' + str(errors))
        None
