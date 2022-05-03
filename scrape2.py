import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd

count = 1
product_type = 'dji+mavic+air'


url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=dji+mavic+air2s&_sacat=0&LH_TitleDesc=0&_odkw=drones&_osacat=0'

def get_data(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    return soup 

def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        NR = count
        product = {
            'Nr': count,
            'Product': item.find('h3', class_='s-item__title').text,
            'Price': item.find('span', class_='s-item__price').text,
            'Location': item.find('span', class_='s-item__location s-item__itemLocation').text,
            'Link': item.find('a', class_='s-item__link')['href'], 
        }           
        productslist.append(product)
    return productslist   

def output(productslist):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv('out1.csv', encoding='utf-8', index=False, sep=';', columns=columns)
    print('Saved to CSV')
    return

soup = get_data(url)
productslist = parse(soup)
output(productslist)
print(parse(soup))

    
      
    