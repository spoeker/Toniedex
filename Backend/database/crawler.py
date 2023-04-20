import re
import time
from urllib.parse import urljoin

from bs4 import BeautifulSoup

# import requests
from helium import start_chrome

from database.tonie_class import Tonie


def crawl():
    url = "https://tonies.com/de-de/tonies/?page=999"
    # tonie_list = []
    time.sleep(2)
    r = start_chrome(url, headless=True)
    selector = BeautifulSoup(r.page_source, "html.parser")
    for product in selector.select(".ProductCollection__Wrapper-sc-11gm1d0-0"):
        tonie_url = urljoin(url, product.select_one("a").attrs["href"])
        r_2 = start_chrome(tonie_url, headless=True)
        selector_2 = BeautifulSoup(r_2.page_source, "html.parser")
        title = selector_2.select_one(".hdJxSy").text
        figure = selector_2.select_one(".lbAbeF").text
        description = selector_2.select_one(".bUGcJn span").text
        titlelist = []
        runtime = selector_2.select(".iBpcit p")[0].text
        age_recommendation = selector_2.select(".iBpcit p")[1].text
        material = selector_2.select(".iBpcit p")[2].text

        # image filtern
        div = selector_2.find(attrs={"aria-label": "2 of 4"})
        image = div.select_one("img").get("srcset")
        image = re.findall("https[^\s]*1336[^\s]*", image)[0]

        # verschiedene Bilder Crawlen
        # for png in selector_2.findAll("img", attrs={"srcset": True}):
        # print(png["srcset"])
        # image.append(png)

        # verschiedenen Tracks von der Titelliste crawlen
        for track in selector_2.select(".cTIvYe"):
            track = track.text
            titlelist.append(track)

        crawled = Tonie(
            title,
            figure,
            description,
            titlelist,
            runtime,
            age_recommendation,
            material,
            image,
        )
        yield crawled
