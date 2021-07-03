from flask import Flask, jsonify, render_template, send_file
from deta import Deta

app = Flask(__name__, template_folder="./static", static_folder="./static/static")

deta = Deta('api_key')
sampleDB = deta.Base("sample")
sampleDrive = deta.Drive("sample")

@app.route("/api/")
def read_root():
    hoge = next(sampleDB.fetch({"name": "hogehoge"}))
    return jsonify(hoge)

@app.route("/api/items/{item_id}")
def read_item(item_id: int):
    sample = sampleDB.put({
        "userID": item_id,
        "name": "hogehoge"
    })
    return sample

@app.route("/")
def read_home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')