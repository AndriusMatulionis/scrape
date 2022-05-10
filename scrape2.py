from bs4 import BeautifulSoup
import requests
from csv import writer

with open('scraped1-2.csv', 'w', encoding='utf-8', newline='') as f:
    thewriter = writer(f)
    header = ['Product', 'Price', 'Location']
    thewriter.writerow(header)  

    for i in range(1, 2):
        url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=drones&_sacat={0}'
        page = requests.get(url).text.strip()
        soup = BeautifulSoup(page, 'html.parser')
        products = soup.find_all('div', class_='s-item__info clearfix')


        
        for product in products:
            Product = product.h3.text
            Price = product.find('span', class_='s-item__price').text
            Location = product.find('span', class_='s-item__location s-item__itemLocation')
            if Location is None:
                print('element not found')
                thewriter.writerow('element not found')
            else:
                thewriter.writerow(Location.text)    
            info = [Product, Price, Location]
            print(info)
            
