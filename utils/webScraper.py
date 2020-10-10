from pprint import pprint
import requests
from bs4 import BeautifulSoup
import json

URL = 'https://www.germanplates.com/german-license-plate-codes'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('p')

vrpCodesGermany = {}

for result in results:
    if len(result.text.split('-', 1)) >= 2:
        vrpCodesGermany[result.text.split('-', 1)[0]] = result.text.split('-', 1)[1]

with open('vrpCodesGermany.json', 'w') as outfile:
    json.dump(vrpCodesGermany, outfile)
