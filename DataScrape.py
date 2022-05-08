import requests
from bs4 import BeautifulSoup
import pandas as pd


count = 1
product_type = 'drones' #change product type here
df = pd.DataFrame(columns=['Nr', 'Product', 'Price'])


for i in range(1, 20): #number of pages
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw='+product_type+'&_pgn='+str(i)+''
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    products = soup.find_all('div', class_='s-item__info clearfix')

    for product in products:
        item = product.h3.text
        condition = getattr(product.find('span', class_='SECONDARY_INFO'), 'text', None)
        price = product.find('span', class_='s-item__price').text
        location = getattr(product.find('span', class_='s-item__location s-item__itemLocation'), 'text', None)
        shipping_price = getattr(product.find('span', class_='s-item__shipping s-item__logisticsCost'), 'text', None)
        df = df.append(
            {'Nr': count, 'Product': item, 'Condition': condition, 'Location': location, 'Price': price, 'Shipping price': shipping_price},
            ignore_index=True)
        count += 1
columns = ['Nr', 'Product', 'Condition', 'Location', 'Price', 'Shipping price']
df.to_csv('out.csv', encoding='utf-8', index=False, sep=';', columns=columns)
print(df)
