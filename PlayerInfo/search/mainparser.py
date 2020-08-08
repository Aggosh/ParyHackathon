from .steampars import steam_pars
from .telegramparse import telegram_pars
import sys

sys.path.append("..")  # Adds higher directory to python modules path.
from Profile.models import Profile


def create_new_profile(nickname):
    steam_url = steam_pars(nickname)
    telegram_url = telegram_pars(nickname)
    new_profile = Profile(nickname=nickname, steam_url=steam_url, telegram_url=telegram_url)
    new_profile.save()