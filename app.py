from urllib.request import urlopen
#import requests as req #windows py3
#import urllib.request #windows
from bs4 import BeautifulSoup

#1 getting web page:
web_page = 'https://www.hawaiianhumane.org/dog-adoptions/'

#query the website and return the html to the variable page:
page = urlopen(web_page)
#page = req.get(web_page)
#urllib.request.Request(web_page) #windows
#print(page)

soup = BeautifulSoup(page, 'html.parser')
# soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)

title_box = soup.find('h1', attrs={'class': 'entry-title'})
print('AGE BELOW')
print(title_box)
title = title_box.text
print(title)

# price_box = soup.find('span', attrs={'class': 'Fw(b)'})
# price = price_box.text
# print(price)

import csv
from datetime import datetime

with open('index.csv', 'a') as csv_file: 
     writer = csv.writer(csv_file) 
     writer.writerow([title, datetime.now()]) 



     