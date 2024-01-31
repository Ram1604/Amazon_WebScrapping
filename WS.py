#Importing Libraries
import requests 
from bs4 import BeautifulSoup

#Capturing HTML from Webpage
headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.'} 
URL = "https://www.amazon.in/dp/B0CHX3RP9R?ref=ods_ucc_kindle_B0CHX3RP9R_nrc_ucc"
r = requests.get(URL, headers=headers)
print(r.status_code)

#prasing content
soup = BeautifulSoup(r.text, 'lxml')
print(soup.prettify())

title_element = soup.select_one('#productTitle')
title = title_element.text.strip()
print(title)

price_element = soup.select_one('.a-price-whole')
price = price_element.text.strip()
print(price)

with open('output.txt', 'w') as file:
    # Write output to the file
    file.write(title + '  -  ' + price)
