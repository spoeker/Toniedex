import uvicorn
from fastapi import FastAPI

from Backend.get_Tonie.tonie_class import Session, Titlelist, Tonie

app = FastAPI()


@app.get("/tonies")
def get_table():
    with Session() as session:
        result = session.query(Tonie).all()
        result = [i.__dict__ for i in result]
        return result


@app.get("/tonies/{tonie_id}")
def get_detail(tonie_id):
    with Session() as session:
        result = session.query(Tonie).filter(Tonie.tonie_id == tonie_id).first()
        titlelist = (
            session.query(Titlelist).filter(Titlelist.tonie_id == tonie_id).all()
        )
        titlelist = [i.__dict__ for i in titlelist]
        return result.__dict__, titlelist


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
