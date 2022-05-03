import bs4 as bs
import requests
import pandas as pd

url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=2017+patrick+mahomes+psa+10+auto&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1&_ipg=100'

def get_data(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    return soup

def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        
        try:
            bids = item.find('span', class_='s-item__bids s-item__bidCount').text
        except:
            bids = ''

        product = {
            'title': item.find('h3', class_='s-item__title s-item__title--has-tags').text,
            'soldprice': float(item.find('span', class_='s-item__price').text.replace('$', '').replace(',','').strip()),
            'solddate': item.find('span', class_='s-item__title--tagblock__COMPLETED').find('span', class_='POSITIVE').text,
            'bids': bids,
            'link': item.find('a', class_='s-item__link')['href'],
            }
        productslist.append(product)
    return productslist

def output(productslist):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv('2017_Patrick_Mahomes_Rookies.csv', index=False)
    return productslist
    print(productsdf ('Saved to CSV'))
    



#soup = get_data(url)
#productslist = parse(soup)
#output(productslist)
#print(parse(soup))