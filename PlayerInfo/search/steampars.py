import json
import requests
from bs4 import BeautifulSoup


def steam_pars(nickname):
    session = requests.Session()
    html = session.get(
        "https://steamcommunity.com/search/users/?l=ukrainian#text=%s" % nickname
    )
    cookies = html.cookies.get_dict()["sessionid"]
    r = session.get(
        f"https://steamcommunity.com/search/SearchCommunityAjax?text={nickname}&filter=users&sessionid=%s&steamid_user=false&page=1s"
        % cookies
    )
    parsed_json = json.loads(r.text)
    html = parsed_json["html"]
    soup = BeautifulSoup(html, "html.parser")
    try:
        url = soup.find("a", class_="searchPersonaName").get("href")
        return url
    except:
        return None
