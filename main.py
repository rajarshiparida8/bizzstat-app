from flask import Flask, jsonify
import json
import threading
import schedule
import time
import BIZZStat

app = Flask(__name__)

@app.route("/")
def home():
    return "BIZZStat is running!"

@app.route("/news")
def get_news():
    with open("news_output.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

def run_scraper():
    BIZZStat.main()  # update your script to save output as news_output.json

def schedule_tasks():
    schedule.every(10).minutes.do(run_scraper)
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=schedule_tasks).start()

if __name__ == "__main__":
    app.run()
