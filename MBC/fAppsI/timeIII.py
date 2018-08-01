from flask import Flask, render_template
app = Flask(__name__)
import datetime

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%m-%d-%Y %H:%M")
    templateData = {
        "time": timeString,
    }
    return render_template("mainTwo.html", **templateData)

if __name__ == "__main__":
    app.run(host="192.168.1.18", port=5000, debug=True)

