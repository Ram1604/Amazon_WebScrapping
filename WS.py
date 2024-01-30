import requests 
from bs4 import BeautifulSoup

#capturing HTML from webpage
headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.'} 
URL = "https://www.amazon.in/Apple-iPhone-15-256-GB/dp/B0CHX6N27Y/ref=sr_1_1_sspa?crid=1UHQHOQNPDPLR&keywords=apple+15&qid=1706520727&sprefix=apple+15%2Caps%2C434&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
r = requests.get(URL, headers=headers)
#print(r.text)
print(r.status_code)

#prasing content
soup = BeautifulSoup(r.text, 'lxml')
#print(soup.prettify())

title_element = soup.select_one('#productTitle')
title = title_element.text.strip()
print(title)

price_element = soup.select_one('.a-price-whole')
price = price_element.text.strip()
print(price)