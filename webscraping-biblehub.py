import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


webpage = 'https://ebible.org/asv/JHN'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

soup = BeautifulSoup(webpage, 'html.parser')

verses_list = soup.findAll('p',class_='reg')

verse_list = [v.text.split('.') for v in verses_list]

print(random.choice(random.choice(verse_list)))

