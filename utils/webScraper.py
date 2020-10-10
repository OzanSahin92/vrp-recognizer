from pprint import pprint
import requests
from bs4 import BeautifulSoup

URL = 'https://www.germanplates.com/german-license-plate-codes'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('p')

for result in results:
    print(result.text)
