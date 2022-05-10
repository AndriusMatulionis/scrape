import requests
from bs4 import BeautifulSoup
import sqlite3
from time import sleep


def average(lst):
    return format(sum(lst) / len(lst), '.2f')

headers = {'User-Agent': 'Mozilla/5.0'}

count = 1
for i in range(1, 2): #number of pages
    sleep(2)
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=drones&_sacat={0}'    # f'{0}  formatuoja adreso paskutini puslapio skaiciu, kuris per cikla gali keistis.
    data = requests.get(url, headers=headers).text.strip()
    soup = BeautifulSoup(data, 'html.parser')
    products = soup.find_all('div', class_='s-item__info clearfix')
    array_to_get_avarage = []
    displayDictList = []
    for product in products:

        Location = product.find('span', class_='s-item__location s-item__itemLocation')
        if Location is None:
            print('element not found')
        else:
            Price = product.find('span', class_='s-item__price').text
            if "to" in Price:
                comapre_at_price = float(Price.split('to')[0].strip().strip('$').replace(',', ''))
            else:
                comapre_at_price = float(Price.strip().strip('$').replace(',', ''))
            if comapre_at_price > 100:
                array_to_get_avarage.append(comapre_at_price)
                Quality = getattr(product.find('span', class_='SECONDARY_INFO'), 'text', None)
                if Quality is None:
                    print('element not found')
                else:

                    Product = product.h3.text
                    productDict = {'id': count, 'product_name': Product, 'location': Location.getText().split()[1],
                                   'quality': Quality, 'price': comapre_at_price}
                    count += 1
                    displayDictList.append(productDict)

    print(average(array_to_get_avarage))
    print(max(array_to_get_avarage))

    try:
        sqliteConnection = sqlite3.connect('scrape_data.db')

        cursor = sqliteConnection.cursor()
        for d in displayDictList:
            cursor.execute('INSERT INTO DATA VALUES (?,?,?,?,?)', [d["id"], d["product_name"],
                                                                d["location"], d["quality"], d["price"]])
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Closed')




