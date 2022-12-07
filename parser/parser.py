import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = "https://kg.kinoafisha.info/bishkek/"


@csrf_exempt
def get_html(url, params=""):
    req = requests.get(url)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all(
        "div", class_="movieList_item movieItem movieItem-grid grid_cell3"
    )
    manas_flm = []

    for item in items:
        manas_flm.append(
            {
                "title": item.find("a").get("href"),
                "title_text": item.find("a", class_="movieItem_title").get_text(),
                "image": item.find("img").get("data-picture"),
            }
        )
    return manas_flm


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        manas_flm1 = []
        html = get_html(f"https://kg.kinoafisha.info/bishkek/")
        manas_flm1.extend(get_data(html.text))
        return manas_flm1
    else:
        raise Exception("Error in parser func........")
