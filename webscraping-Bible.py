import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



chapters = list(range(1,22))   
random_chapter = random.choice(chapters)

if random < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)


webpage = 'https://ebible.org/asv/JHN'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

soup = BeautifulSoup(webpage, 'html.parser')

#print(soup.title.text)

page_versus = soup.findAll('div', class_='main')

for versus in page_versus:
    verse_list = versus.text.split('.')

mychoice = random.choice(verse_list[-5])

verse = f'Chapter: {random_chapter} Verse: {mychoice}'

print(verse)

import keys
from twilio.rest import Client

client = Client(keys.accountSID,keys.authToken)

TwilioNumber = '+17136093244'
mycellphone = '+17136093244'

textmessage = client.message.create(to_=mycellphone, from_=TwilioNumber, body=verse)