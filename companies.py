import pandas as pd
from yahoo_fin import stock_info as si


def GOOG() -> str:
    page = 'https://en.wikipedia.org/wiki/Google'
    infobox = pd.read_html(page, attrs={"class": "infobox"},
                           skiprows=[0, 1, 2, 3, 8, 17, 18])
    df = infobox[0]
    df.columns = ["Google", "GOOG"]
    try:
        stock = round(si.get_live_price("GOOG"), 2)
    except:
        stock = "error"
    df.at[5, "Google"] = "Stock price"
    df.at[5, "GOOG"] = stock
    return df.to_html(classes="", index=False)


def AMZN() -> str:
    page = 'https://en.wikipedia.org/wiki/Amazon_(company)'
    infobox = pd.read_html(page, attrs={"class": "infobox"},
                           skiprows=[0, 1, 2, 3, 4, 5, 6, 11, 13, 21, 22, 23])
    df = infobox[0]
    df.columns = ["Amazon", "AMZN"]
    try:
        stock = round(si.get_live_price("AMZN"), 2)
    except:
        stock = "error"
    df.at[5, df.columns[0]] = "Stock price"
    df.at[5, df.columns[1]] = stock
    return df.to_html(classes="", index=False)


def AAPL() -> str:
    page = 'https://en.wikipedia.org/wiki/Apple_Inc.'
    infobox = pd.read_html(page, attrs={"class": "infobox"},
                           skiprows=[0, 1, 2, 3, 4, 5, 10, 11, 13, 21, 22])
    df = infobox[0]
    df.columns = ["Apple", "AAPL"]
    try:
        stock = round(si.get_live_price("aapl"), 2)
    except:
        stock = "error"
    df.at[5, df.columns[0]] = "Stock price"
    df.at[5, df.columns[1]] = stock
    return df.to_html(classes="", index=False)


def FB() -> str:
    page = 'https://en.wikipedia.org/wiki/Facebook,_Inc.'
    infobox = pd.read_html(page, attrs={"class": "infobox"},
                           skiprows=[0, 1, 2, 15, 16, 17, 18, 19])
    df = infobox[0]
    df.columns = ["Facebook", "FB"]
    try:
        stock = round(si.get_live_price("FB"), 2)
    except:
        stock = "error"
    df.at[4, df.columns[0]] = "Stock price"
    df.at[4, df.columns[1]] = stock
    return df.to_html(classes="", index=False)


def MSFT() -> str:
    page = 'https://en.wikipedia.org/wiki/Microsoft'
    infobox = pd.read_html(page, attrs={"class": "infobox"},
                           skiprows=[0, 1, 2, 3, 4, 6, 10, 12, 20, 21])
    df = infobox[0]
    df.columns = ["Microsoft", "MSFT"]
    try:
        stock = round(si.get_live_price("MSFT"), 2)
    except:
        stock = "error"
    df.at[5, df.columns[0]] = "Stock price"
    df.at[5, df.columns[1]] = stock
    return df.to_html(classes="", index=False)

