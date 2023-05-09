from get_Tonie.crawler import crawl
from get_Tonie.tonie_class import Session, Tonie

counter = 0

with Session() as session:
    for x in crawl():
        exist_tonie = (
            session.query(Tonie)
            .filter(Tonie.title == x.title, Tonie.figure == x.figure)
            .one_or_none()
        )
        if exist_tonie:
            x.tonie_id = exist_tonie.tonie_id

            for i, title in enumerate(exist_tonie.titlelist):
                x.titlelist[i].tonie_id = exist_tonie.tonie_id
                x.titlelist[i].list_id = title.list_id

            session.merge(x)

        else:
            session.add(x)
    session.commit()
