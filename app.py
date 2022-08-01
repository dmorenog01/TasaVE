from flask import Flask, render_template
import requests

app = Flask(__name__)
API_URL = "https://bcv-api.herokuapp.com/"

@app.route("/")
def index():
    api_response = requests.get(API_URL).json()
    info = {
        "rate": api_response["rate"],
        "date": api_response["rate-date"]
    }
    return render_template("index.html", information=info)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/donate")
def donate():
    return render_template("donate.html")

if __name__ == "__main__":
    app.run(threaded=True, port=5000)