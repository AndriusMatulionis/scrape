import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=drones&_sacat=0'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')


print('Classes of each table:')
count = 1
products = soup.find_all('div', class_='s-item__info clearfix')
location = soup.find_all('div', class_='s-item__info clearfix')
df = pd.DataFrame(columns=['Nr', 'Product', 'Price', 'Location'])

for product in products:
    Nr = count
    Product = product.h3.text
    Price = product.find('span', class_='s-item__price').text
    Location = product.find('span', class_='s-item__location s-item__itemLocation')
    df = df.append(
        {'Nr': count, 'Product': Product, 'Price': Price, 'Location': Location},
        ignore_index=True)
    count += 1
print(df)




#s-item__location s-item__itemLocation
