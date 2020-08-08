import requests
import json


def twitch_pars(nickname):
    headers = {
        "Accept": "application/vnd.twitchtv.v5+json",
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",
    }
    r = requests.get(
        "https://api.twitch.tv/kraken/users?login=%s" % nickname, headers=headers
    )

    json_ = json.loads(r.text)
    if json_["_total"] == 1:
        return nickname
    else:
        return None
