from get_Tonie.tonie_class import Session, Tonie


def get_table():
    with Session() as session:
        result = session.query(Tonie).all()
        return result


def get_detail(tonie_id: int):
    with Session() as session:
        result = session.query(Tonie).filter(Tonie.tonie_id == tonie_id).first()
        return result
