from .steampars import steam_pars
from .twitchparser import twitch_pars
import sys

sys.path.append("..")  # Adds higher directory to python modules path.
from Profile.models import Profile


def create_new_profile(nickname):
    steam_url = steam_pars(nickname)
    twitch = twitch_pars(nickname)

    new_profile = Profile(
        nickname=nickname,
        steam_url=steam_url,
        twitch=twitch,
    )
    new_profile.save()
