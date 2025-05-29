from bs4 import BeautifulSoup
import requests

def getPrice(Link = 'https://www.tgju.org'):

    response = requests.get(Link)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', {'class' : 'container'})

    if len(items) == 0:
        print("Nothing Found!")

    else:

        titles = items[0].find_all('h3')
        prices = items[0].find_all('span', {'class', 'info-price'})

    title = []
    price = []

    for t in titles:
        t = t.getText()
        t = t.replace('\n', '')
        title.append(t)

    for p in prices:
        p = p.getText()
        p = p.replace('\n', '')
        price.append(p)


    text = dict(zip(title, price))

    return text
