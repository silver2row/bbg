from flask import Flask, render_template
app = Flask(__name__)
import datetime

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        "time": timeString,
    }
    return render_template("mainOne.html", **templateData)

if __name__ == "__main__":
    app.run(host="192.168.7.2", port=5000, debug=True)

