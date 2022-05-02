import requests
from bs4 import BeautifulSoup
import pandas as pd


count = 1
product_type = 'Samsung+Galaxy+S22+Ultra/S22+/S22+Full+Body+Hybrid+Shockproof+Case+Cover' #change product type here
df = pd.DataFrame(columns=['Nr', 'Product', 'Price'])


for i in range(1, 3): #number of pages
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw='+product_type+'&_ipg=240&_pgn='+str(i)+''
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    products = soup.find_all('div', class_='s-item__info clearfix')

    for product in products:
        Nr = count
        Product = product.h3.text
        Price = product.find('span', class_='s-item__price').text
        df = df.append(
            {'Nr': count, 'Product': Product, 'Price': Price},
            ignore_index=True)
        count += 1
columns = ['Nr', 'Product', 'Price']
df.to_csv('out.csv', encoding='utf-8', index=False, sep=';', columns=columns)
print(df)