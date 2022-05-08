import requests
from bs4 import BeautifulSoup
import pandas as pd


count = 1
df = pd.DataFrame(columns=['Nr', 'Product', 'Price', 'Location', 'Quality'])
columns = ['Nr', 'Product', 'Price', 'Location', 'Quality']

for i in range(1, 2): #number of pages
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=drones&_sacat={0}'    # f'{0}  formatuoja adreso paskutini puslapio skaiciu, kuris per cikla gali keistis. 
    data = requests.get(url).text.strip()
    soup = BeautifulSoup(data, 'html.parser')
    products = soup.find_all('div', class_='s-item__info clearfix')
    

    for product in products:
        Nr = count
        Product = product.h3.text
        Price = product.find('span', class_='s-item__price').text
        Location = product.find('span', class_='s-item__location s-item__itemLocation')
        if Location is None:
            print('element not found')
        else:
            print(Location.text)
        Quality = product.find('span', class_='SECONDARY_INFO')
        if Quality is None:
            print('element not found')
        else:
            print(Quality.text)
        
        print(product.text)
        #Shipping
'''''    
        df = df.append(
            {'Nr': count, 
             'Product': Product, 
             'Price': Price,
             'Location': Location,
             'Quality': Quality},
            ignore_index=True)
        
        count += 1
        
df.to_csv('out.csv', encoding='utf-8', index=False, sep=';', columns=columns)
print(df)
'''

asasdaSdASdasdasdasdadsad