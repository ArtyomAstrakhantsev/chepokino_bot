import sys
import requests
from lxml import html
from bs4 import BeautifulSoup


s = requests.Session()
s.headers.update({
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'cookie': 'PHPSESSID=ck33bqion3h0konuf63v7p5c73; yandex_gid=118936; _csrf_csrf_token=tvWk0Kaz3Fdvp9BaYGEw5aNu6YP5faGVpCGSg2pBeU0; mda_exp_enabled=1; user-geo-region-id=118936; user-geo-country-id=2; desktop_session_key=11b37d12b98feba412195576aa24c9eada3c7fdd3d14f908baa84acc1b038f1f09615dfa5f4baab009e7c09d4cd2ebf44aad8fb602876f1535b2138786256a16482d15a8dc585f75f3e86386a8f89946c51283b2136b67e97574b23eca7b2706; desktop_session_key.sig=NNJZ7mElOJu-4I2ZmpT2P4Z83yA; yandexuid=8943112421560689524; uid=32275811; _ym_uid=1572729953547011769; mda=0; _ym_uid=1572729953547011769; _ym_d=1574185459; yuidss=8943112421560689524; yp=1583135612.oyu.8943112421560689524#1580630012.yu.8943112421560689524; gdpr=0; i=DbfFtqv5cF3xeVl1WiKjLLnMdV7OXqo55iVqdg3SCA73DkbwW/lF0WWOWHmPGXT56g9P31AuNgOc8LPs2y0EK5N3QKI=; location=1; my_perpages=%5B%5D; tc=2; crookie=Hk0K7PVw0jBVybLF244i4nUy/prk0TJea8wR4e/eeZi8+DVMTV+bpJDbfrtQviSgoZoFFGDEIITCjdmd7/uRfUebthE=; cmtchd=MTU4Njk0NTUwMzY1MQ==; mobile=no; yandex_ugc_rating_status=no; yandex_ugc_rating_status.sig=pw4cVz6AAY2ipArQXugmwejk7uw; sso_status=sso.passport.yandex.ru:synchronized; ya_sess_id=noauth:1587156861; ys=udn.cDrQkNGA0YLRkdC8INCQ0YHRgtGA0LDRhdCw0L3RhtC10LI%3D#c_chck.3052894158; mda2_beacon=1587156861754; _ym_d=1587156868'
        })

def open_page_best_film(s):
    url = 'https://www.kinopoisk.ru/lists/top250/' 
    r = s.get(url)
    return r.text


def contain_movies_name(text):
    soup = BeautifulSoup(text, 'lxml')
    film_name = soup.find('div', {'class': 'selection-film-item-meta_theme_desktop'})
    return film_name is not None

while True:
    data = open_page_best_film(s)
    if contain_movies_name(data):
        with open('page_film.html', 'w', encoding='UTF-8') as output_file:
            output_file.write(data)
    else:
        break