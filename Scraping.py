
# coding: utf-8

# In[ ]:


import os
import cv2
import imutils
import nltk 
import string
import re
import pickle
import numpy as np
import pandas as pd


# In[ ]:


#menginport library beautifulsoup4
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import pandas as pd
#mengakses halaman web yang ingin diakses

page_link = "https://id.wikipedia.org/wiki/Teknologi_komunikasi_digital"
base_link = "https://id.wikipedia.org"
page_response = urlopen(page_link)
soup = BeautifulSoup(page_response, "html.parser")
links = soup.find_all("a",href=True)
import csv
import pandas as pd
urls =[]
isiteks = []

x = dict()

for link in links:
    if re.search('/wiki/',str(link['href'])) and ':' not in link['href'] and link['href'] != '/wiki/Halaman_Utama':
        x[link['href']] = 0
        

for link in links: 
    #expression untuk mengekstrak url dari html link
    if re.search('/wiki/',str(link['href'])) and ':' not in link['href'] and link['href'] != '/wiki/Halaman_Utama' and x[link['href']] == 0:
        print(link['href'])
        x[link['href']] = 1
        #url lengkap
        url_a = base_link + link['href'] 
#         print(url_a )
        directlink = url_a
#         base_link = 'https://id.wikipedia.org'
        page_response = requests.get(url_a)   
        soup = BeautifulSoup(page_response.content, "html.parser")
        paragraf = ''
        for i in range(0, len(soup.findAll('p'))):
            newparagraf = soup.find_all('p')[i].text
#             judul= soup.find_all("h1",href=True)

            paragraf = paragraf + newparagraf
   
        isiteks.append({'directlink' : url_a, 'paragraf' : paragraf})

df = pd.DataFrame(isiteks, columns=['directlink','paragraf'])
df.to_csv('dataset/Teknologi_komunikasi_digital.csv', index=True, encoding='utf-8', sep = ',')

