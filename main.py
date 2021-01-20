from flask import Flask, render_template
from scraper import *
from companies import *

app = Flask(__name__)
# cmd alt l to format
# pip freeze > requirements.txt


@app.route("/")
def index():
    texts = [worldPop(), US(), CA(), minWage(), SF(), Belmont()]
    tables = [countryPop(), worldCities(), USCities()]
    tableTitles = ["Largest countries by population",
                   "Largest cities in the world by population",
                   "Largest US cities by population"]
    return render_template("index.html", texts=texts, tables=tables,
                           titles=tableTitles)


@app.route("/names")
def names():
    tables = [GOP(), Senate(), scotus()]
    titles = ["US House of Representatives", "US Senate", "US Supreme Court"]
    return render_template("names.html", tables=tables, titles=titles)


@app.route("/companies")
def companies():
    tables = [GOOG(), AMZN(), FB(), MSFT(), AAPL()]
    big_five = ["Google", "Amazon", "Facebook", "Microsoft", "Apple"]
    return render_template("companies.html", tables=tables, big_five=big_five)


if __name__ == "__main__":
    app.run(debug=True)
