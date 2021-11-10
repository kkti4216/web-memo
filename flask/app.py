from flask import *
import sqlite3
from datetime import datetime
from config import * 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    
    if request.method == "POST":
        item = {"time":datetime.now().isoformat(timespec='minutes'), "text":request.form["new_rec"]}
        if item["text"] != "":
            con.execute("insert into memo(time,text) values(:time,:text)",item)
    
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

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
