import json
import time

# from urllib import request
import requests

from get_Tonie.tonie_class import Titlelist, Tonie


def crawl():
    time.sleep(3)
    url = "https://tonies.com/_next/data/XIOvwhAiwmwJBkFb9cRmz/de-de/tonies.json?locale=de-de&slug=tonies&page=999"
    r = requests.get(url)
    main_json = r.json()
    page_dic = main_json["pageProps"]["page"]["productList"]["normalizedProducts"]
    netkey_parts = url.split("/", 6)
    netkey_url = (
        netkey_parts[0]
        + "/"
        + netkey_parts[1]
        + "/"
        + netkey_parts[2]
        + "/"
        + netkey_parts[3]
        + "/"
        + netkey_parts[4]
        + "/"
        + netkey_parts[5]
    )

    for x in page_dic:
        value = x["path"].rstrip("/")

        new_url = netkey_url + value + ".json"

        r_2 = requests.get(new_url)
        tonie_json = r_2.json()
        tonie_dic = tonie_json["pageProps"]["product"]
        data = {}

        data["title"] = tonie_dic["name"]

        data["figure"] = tonie_dic["series"]["label"]
        data["description"] = tonie_dic["description"]
        data["image"] = tonie_dic["images"][1]["src"]
        data["runtime"] = tonie_dic.get("runTime", "Keine Laufzeitangabe")
        data["age_recommendation"] = tonie_dic.get("ageMin", "Keine Altersangabe")
        data["titlelist"] = []

        for i, track in enumerate(
            tonie_dic.get("tracks", []),
            start=1,
        ):
            data["titlelist"].append(Titlelist(title_nr=i, title=track))

        yield Tonie(**data)
