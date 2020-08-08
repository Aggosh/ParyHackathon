import requests
from bs4 import BeautifulSoup


def telegram_pars(nickname):
    html = requests.get('https://t.me/%s' % nickname).text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        soup.find('div', class_='tgme_page_title')
        url = soup.find('a', class_='tgme_action_button_new').get('href')
        return (url)
    except:
        return None
