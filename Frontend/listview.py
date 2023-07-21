import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/tonies")
def get_api():
    url = "http://127.0.0.1:8000/tonies"
    r = requests.get(url)
    json = r.json()

    return render_template("start.html", json=json)


@app.route("/tonies/<tonies_id>")
def get_detail(tonies_id):
    url = "http://127.0.0.1:8000/tonies/" + str(tonies_id)
    r = requests.get(url)
    json = r.json()

    return render_template("detail.html", json=json)


if __name__ == "__main__":
    app.run(port=6868, debug=True)
