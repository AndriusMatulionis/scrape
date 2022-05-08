import requests
from bs4 import BeautifulSoup
import pandas as pd


count = 1
df = pd.DataFrame(columns=['Nr', 'Product', 'Price', 'Location', 'Quality'])   #pridedant nauja collum, apsirasom cia
columns = ['Nr', 'Product', 'Price', 'Location', 'Quality']   #pridedant nauja collum, apsirasom cia

for i in range(1, 5): # cia keiciam puslapiu kieki kiek scrapinam
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=drones&_sacat={0}'   # f'{0}  formatuoja adreso paskutini puslapio skaiciu, kuris per cikla gali keistis. 
    data = requests.get(url).text.strip()
    soup = BeautifulSoup(data, 'html.parser')
    products = soup.find_all('div', class_='s-item__info clearfix')
    

    for product in products:
        Nr = count
        Product = product.h3.text
        Price = product.find('span', class_='s-item__price').text
        Location = getattr(product.find('span', class_='s-item__location s-item__itemLocation'), 'text', None)
        Quality = getattr(product.find('span', class_='SECONDARY_INFO'), 'text', None)
        #pridedant nauja collum, apsirasom cia
        
   
        df = df.append(
            {'Nr': count, 
             'Product': Product, 
             'Price': Price,
             'Location': Location,
             'Quality': Quality},
            ignore_index=True)
        #pridedant nauja collum, apsirasom cia
        count += 1
        
df.to_csv('out.csv', encoding='utf-8', index=False, sep=';', columns=columns)
print(df)


