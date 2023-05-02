from get_Tonie.crawler import crawl
from get_Tonie.tonie_class import Session

with Session() as session:
    for x in crawl():
        session.add(x)
        break
    session.commit()
