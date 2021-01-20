import requests
from bs4 import BeautifulSoup
import wikipediaapi
import pandas as pd

wiki = wikipediaapi.Wikipedia('en')


# returns NavigableString of key phrase
def finder(URL: str, key_phrase: str, whitelist: list):
    res = [None]
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    text_elements = [t for t in soup.find_all(text=True) if
                     t.parent.name in whitelist]
    for elem in text_elements:
        text = str(elem)
        if key_phrase in text:
            res = elem
            break
    return res


# returns index of key phrase
def wikiFinder(pagename: str, key_phrase: str, minus: int, plus: int) -> int:
    page = wiki.page(pagename)
    summary = page.summary
    i = summary.find(key_phrase)
    res = summary[i - minus: i + plus]
    return res


def worldPop() -> str:
    URL = "https://www.worldometers.info/world-population/#:~:text=7.8%20Billion%20(2021),Nations%20estimates%20elaborated%20by%20Worldometer."
    key = "current world population"
    whitelist = ['p']
    elem = finder(URL, key, whitelist)
    pop = elem.nextSibling
    return "The current world population is " + pop.contents[0]


def US() -> str:
    URL = "https://www.worldometers.info/world-population/us-population/"
    key = "current population of"
    whitelist = ['li']
    elem = finder(URL, key, whitelist)
    pop = elem.nextSibling.nextSibling.nextSibling
    area = "3.797 million mi²"
    return "The current US population is " + pop.contents[
        0] + ". \nUS has area about " + area


def CA() -> str:
    pop = wikiFinder("California", "million residents", 5, 7)
    area = "163,696 square miles (423,970 km2)"
    return "CA has population over " + pop + ". CA has area about " + area


def SF() -> str:
    pop = wikiFinder("San Francisco Bay Area", "Home to approximately", -22,
                     34)
    area = "6,900 square miles (18,000 km2)"
    return "The SF Bay Area has population about " + pop + ". Area of about " \
           + area


def Belmont() -> str:
    return "Belmont has population about 30,000 and area about 5 sq miles."


def minWage() -> str:
    wage = wikiFinder("Minimum wage in the United States",
                      "federal minimum wage is", 0, 40)
    return "The " + wage


def countryPop() -> str:
    URL = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.select_one('table', class_="wikitable")

    ranks = []
    countries = []
    pops = []
    percents = []
    rows = table.find_all('tr')[:11]
    for rank, row in enumerate(rows):
        cells = row.find_all('td')
        if len(cells) > 1:
            ranks.append(rank)
            c = cells[0].select_one('a')
            countries.append(c.text)
            pops.append(cells[1].text)
            percents.append(cells[2].text)

    d = {'Country': countries, 'Population': pops, 'Percent of World': percents}
    df = pd.DataFrame(data=d, index=ranks)
    return df.to_html(classes="")


def worldCities() -> str:
    URL = "https://en.wikipedia.org/wiki/List_of_largest_cities"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", class_="wikitable")

    ranks = []
    cities = []
    countries = []
    pops = []
    rows = table.find_all('tr')[:12]
    for rank, row in enumerate(rows, start=-1):
        cells = row.find_all('td')
        if len(cells) > 1:
            ranks.append(rank)
            cities.append(cells[0].text[:-1])
            countries.append(cells[1].text[:-1])
            pops.append(cells[3].text[:-1])

    d = {'City': cities, 'Country': countries, 'Population': pops}
    df = pd.DataFrame(data=d, index=ranks)
    return df.to_html(classes="")


def USCities() -> str:
    URL = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", class_="wikitable sortable")

    ranks = []
    cities = []
    states = []
    pops = []
    areas = []
    rows = table.find_all('tr')[:11]
    for rank, row in enumerate(rows, start=0):
        cells = row.find_all('td')
        if len(cells) > 1:
            ranks.append(rank)
            cities.append(cells[1].text[:-1])
            states.append(cells[2].text[:-1])
            pops.append(cells[3].text[:-1])
            areas.append(cells[6].text[:-1])

    d = {'City': cities, 'State': states, 'Population': pops, 'Area': areas}
    df = pd.DataFrame(data=d, index=ranks)
    return df.to_html(classes="")


# from <a> format
def make_link(link_elem):
    t = link_elem.get('title')
    link, tex = wiki.page(t).fullurl, link_elem.text
    # target _blank to open new window
    return '<a target="_blank" href="{}" title="{}">{}</a>'.format(link, t, tex)


def pol_link(person):
    elems = person.find_all('a')
    name = elems[0]
    party = elems[1]
    text = person.text.split(")")[1]
    return make_link(name) + " (" + make_link(party) + ")" + text


def GOP() -> str:
    URL = "https://en.wikipedia.org/wiki/United_States_House_of_Representatives"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", class_="infobox vcard")

    roles = []
    names = []
    rows = table.find_all('tr')
    for row in rows[10:13]:
        role = row.find_all('th')[0].select_one('a')
        role = make_link(role)
        roles.append(str(role))

        person = row.find_all('td')[0]
        name = pol_link(person)
        names.append(name)

    counts = rows[19].text.replace('\n', '')
    dems = counts.find("Democratic (")
    reps = counts.find("Republican (")
    vac = counts.find("Vacant (")
    info = "435 voting members"
    info += '<p style="margin-bottom: 0">' + counts[dems:dems + 16] + ', ' \
            + counts[reps:reps + 16] + ', ' + counts[vac:vac + 10]
    roles.append("Structure")
    names.append(info)

    d = {'Role': roles, 'Name': names}
    df = pd.DataFrame(data=d, dtype=str)
    # df.style.format({'Role': change_link})
    return df.to_html(classes="", escape=False, header=False, index=False)


def Senate() -> str:
    URL = "https://en.wikipedia.org/wiki/United_States_Senate"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find("table", class_="infobox vcard")

    roles = []
    names = []
    rows = table.find_all('tr')
    for row in rows[10:13]:
        role = row.find_all('th')[0].select_one('a')
        role = make_link(role)
        roles.append(str(role))

        person = row.find_all('td')[0]
        name = pol_link(person)
        names.append(name)

    counts = rows[19].text.replace('\n', '')
    dems = counts.find("Democratic (")
    reps = counts.find("Republican (")
    vac = counts.find("Vacant (")
    info = counts[dems:dems + 15] + ', ' + counts[reps:reps + 15] + \
           ', ' + counts[vac:vac + 10]
    roles.append("Political Groups")
    names.append(info)

    d = {'Role': roles, 'Name': names}
    df = pd.DataFrame(data=d, dtype=str)
    # df.style.format({'Role': change_link})
    return df.to_html(classes="", escape=False, header=False, index=False)


def scotus() -> str:
    URL = "https://en.wikipedia.org/wiki/List_of_justices_of_the_Supreme_Court_of_the_United_States"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.findAll("td", class_="plainlist", limit=2)[1]

    rows = table.find_all('dd')
    labels = ["Chief justice", 'Associate justices']
    res = ""
    names = []
    for i, row in enumerate(rows):
        if i == 0:
            names.append('<p id="text">' + make_link(row.contents[0]) + '</p>')
        else:
            add = '<p id="text">' + make_link(row.contents[0]) + '</p>'
            res += add
    names.append(res)
    d = {'Role': labels, 'Name': names}
    df = pd.DataFrame(data=d, dtype=str)
    return df.to_html(classes="", escape=False, header=False, index=False)

# print(worldPop())
# print(USPop())
# print(CAPop())
# print(minWage())
# print(countryPop())
# print(worldCities())
# print(USCities())
# print(GOP())
scotus()

