import json

import lxml.html
import requests


url = 'https://www.yugioh-card.com/uk/gameplay/detail.php?id=1155'

response = requests.get(url)
cards = list()
root = lxml.html.fromstring(response.content)
for row in root.xpath('//tbody/tr'):
    card_type = row.xpath('./td[1]')[0].text_content()
    card_name = row.xpath('./td[2]')[0].text_content()
    advanced = row.xpath('./td[3]')[0].text_content()
    # link, = row.xpath('./td[6]/a/@href')
    card = {
        'card_type': card_type,
        'card_name': card_name,
        'advanced': advanced,
    }
    cards.append(card)

with open('cards.json','w') as fp:
    json.dump(cards,fp)