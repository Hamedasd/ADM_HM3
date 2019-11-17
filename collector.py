import csv , os, glob , random, time , codecs
import pandas as pd
import requests, urllib
from bs4 import BeautifulSoup
import time
import random
from collector_utils import WRITER
# here are the links to collect
# first we need to prepare all of the links in a list
url_1 = 'https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies1.html'
url_2 = 'https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies2.html'
url_3 = 'https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies3.html'

# collect all of the urls in a list named url_list
# It's the collection of all urls

url_list = []
for url in  [url_1 , url_2 , url_3]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    for link in soup.find_all('a'):
        url_list.append(link.get('href'))
        
        
 for i ,link in enumerate(url_list):
    try:
        response = requests.get(link)
    except requests.exceptions.RequestException as e:
        E.append(e)
        time.sleep(random.choice(range(1,4)))
        response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    WRITER(i , soup)
    time.sleep(random.choice(range(1,4)))       
