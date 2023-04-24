import json

from get_Tonie.crawler import crawl

Tonies = []
for x in crawl():
    counter = counter + 1
    Tonies.append(x.__dict__)


with open("Tonies.json", "w", encoding="utf8") as file:
    json.dump(Tonies, file, indent=4, ensure_ascii=False)
