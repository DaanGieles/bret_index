import requests
import json
from flask import Flask, render_template
from datetime import datetime
import calculations
app = Flask(__name__)


@app.route('/')
def index():
    date = datetime.now().strftime('%Y-%m-%d')
    forecast= calculations.load_forecast()
    bret_index = calculations.determine_bret_index(forecast)

    if bret_index>0.4:
        text = 'Go out and have a beer!'
    else:
        text = 'Stay home and watch a movie'

    return render_template('index.html',forecast=forecast,date=date,bret_index = bret_index, text=text)
if __name__ == '__main__':
    app.run()
    