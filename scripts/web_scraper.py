"""
webScraper.py is programmed for https://www.germanplates.com/german-license-plate-codes
scrapes the city codes and city names of the website
saves city codes, city names, country code, country name into a json file
this code specifically works for germany and the website in line 1
"""

import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.germanplates.com/german-license-plate-codes"
page = requests.get(URL, timeout=10)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("p")

vrpCodesGermany = []

COUNTER = 1
for result in results:
    if len(result.text.split("-", 1)) >= 2:
        vrpCodesGermany.append(
            {
                "model": "vrpAssigner.VrpLocation",
                "pk": COUNTER,
                "fields": {
                    "countryCode": "D",
                    "country": "Deutschland",
                    "cityCode": result.text.split("-", 1)[0]
                    .replace("\n", "")
                    .replace("\r", "")
                    .replace(" ", ""),
                    "city": result.text.split("-", 1)[1]
                    .replace("\n", "")
                    .replace("\r", "")
                    .strip(),
                },
            }
        )
        COUNTER += 1

with open("vrpCodesGermany.json", "w", encoding="UTF-8") as outfile:
    json.dump(vrpCodesGermany, outfile, ensure_ascii=False)
