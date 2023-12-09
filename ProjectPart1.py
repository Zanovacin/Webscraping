from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import keys 
from twilio.rest import Client


url = 'https://finance.yahoo.com/crypto/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

#Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies 
# and display as a formatted output one currency at a time. 
# The output should display the name of the currency, the symbol (if applicable),
#  the current price and % change in the last 24 hrs and corresponding price (based on % change)

crypto_rows = soup.findAll('tr',attrs={"class":"simpTblRow Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) Bdbc($tableBorderBlue):h H(32px) Bgc($lv2BgColor)"})
#print(crypto_rows)

rank = 0
for rec in crypto_rows[:5]:

    rank += 1
    td = rec.findAll('td')
    symbol = td[0].text
    name = td[1].text
    current_price = round(float((td[2]).text.replace(",","")),2)
    change = float(td[4].text.strip('+').strip('%'))
    old_price = round(current_price / (1 + change),2)
    
    print(f'Rank:', rank)
    print(f'Symbol:', symbol)
    print(f'Name:', name)
    print(f'Current Price:', '$',current_price)
    print(f'% Change:', change )
    print(f'Old Pirce:', '$',old_price)
    print()
    input()
    

    
    


client = Client(keys.accountSID, keys.authToken)

TwilioNumber = "+18556122793"

myCellPhone = "+17136093244"

message = "Ethereum has reached or surpassed $2,000!"


textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body=message)

if current_price >= 2000:
    print(textmessage.status)
