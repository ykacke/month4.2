import requests
from bs4 import BeautifulSoup


URL = "https://remanga.org/"


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15",
}


def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request



def get_data(html):
    bs = BeautifulSoup(html, features="html.parser")
    items = bs.find_all("div", class_="Grid_gridItem__aPUx1 p-1")
    manga_list = []
    for item in items:
        title = item.find("h4", class_="Typography_h6__VMBDX Typography_lineClamp-2__A03jO Typography_lineClamp__Pa1wi").get_text(strip=True)
        rating = item.find("p", class_="Typography_caption___iNir Typography_color-textSecondary__iFFB7 flex items-center").get_text(strip=True)
        manga_list.append({
            "title": title,
            "rating": rating,

        })
    return manga_list

def parsing_manga():
    response = get_html(URL)
    if response.status_code == 200:
        manga_list2 = []
        for page in range(1,2):
            response = get_html("https://remanga.org/manga/", params={'page': page})
            manga_list2.extend(get_data(response.text))
        return  manga_list2
    else:
        raise Exception("error in parsing")