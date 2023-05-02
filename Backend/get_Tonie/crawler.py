import re
import time
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from helium import start_chrome
from tqdm import tqdm

from get_Tonie.tonie_class import Titlelist, Tonie


def crawl():
    url = "https://tonies.com/de-de/tonies/?page=999"

    with start_chrome(url, headless=True) as r:
        time.sleep(3)

        selector = BeautifulSoup(r.page_source, "html.parser")
        urlfinder = selector.select(".ProductCollection__Wrapper-sc-11gm1d0-0")
        pbar = tqdm(total=len(urlfinder), dynamic_ncols=True)
        for product in urlfinder:
            data = {}
            tonie_url = urljoin(url, product.select_one("a").attrs["href"])
            with start_chrome(tonie_url, headless=True) as r_2:
                time.sleep(2)
                selector_2 = BeautifulSoup(r_2.page_source, "html.parser")
                data["title"] = selector_2.select_one(".hdJxSy").get_text()
                data["figure"] = selector_2.select_one(".lbAbeF").get_text()
                data["description"] = selector_2.select_one(".bUGcJn span").get_text()
                data["titlelist"] = []

                check_runtime = selector_2.select(".iBpcit p")[0].get_text()
                if "Minuten" not in check_runtime:
                    data["runtime"] = "Keine Laufzeit"
                    data["age_recommendation"] = check_runtime
                else:
                    data["runtime"] = check_runtime
                    data["age_recommendation"] = selector_2.select(".iBpcit p")[
                        1
                    ].get_text()

                # image filtern
                div = selector_2.find_all("img", attrs={"srcset": True})
                image = div[-1].get("srcset")
                data["image"] = re.findall("https[^\s]*1336[^\s]*", image)[-1]

                # verschiedenen Tracks von der Titelliste crawlen

                for track in selector_2.select(".cTIvYe"):
                    track = track.get_text()
                    title_nr = int(track.split(" - ")[0])
                    title = track.split(" - ")[-1]
                    track = Titlelist(title_nr=title_nr, title=title)
                    data["titlelist"].append(track)

                crawled = Tonie(**data)

                yield crawled
                pbar.update(1)
