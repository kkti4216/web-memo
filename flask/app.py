from ensurepip import bootstrap
from flask import *
import sqlite3
import flask_bootstrap
from datetime import datetime
from config import *

app = Flask(__name__)
bootstrap = flask_bootstrap.Bootstrap(app)

@app.route("/", methods=["GET"])
def main():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row

    res = con.execute("select * from memo")
    memo = []
    while True:
        row = res.fetchone()
        if row == None: break
        memo.append({"id":str(row["id"]).rjust(3,"0"), "time":row["time"], "text":row["text"]})
    memo.reverse()
    app.logger.info(memo)
    con.commit()
    con.close()

    return render_template("index.html", memo=memo)

@app.route("/regist/", methods=["POST"])
def post():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row

    item = {"time":datetime.now().isoformat(timespec='minutes'), "text":request.form["new_rec"]}
    if item["text"] != "":
        con.execute("insert into memo(time,text) values(:time,:text)",item)

    con.commit()
    con.close()

    return redirect("/")

@app.route("/delete/", methods=["POST"])
def delete():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row

    item = {"id":request.form["del_rec"]}
    app.logger.info("[delete] {}".format(item["id"]))
    con.execute("delete from memo where id=:id",item)

    con.commit()
    con.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
