from random import randint
import requests


def fetch_comic(comic_number=None):
    latest_number = fetch_latest_comic_number()
    if not latest_number:
        return None

    random_number = randint(1, latest_number)
    url = f'https://xkcd.com/{random_number}/info.0.json'

    response = requests.get(url)
    response.raise_for_status()

    comic = response.json()

    return {
        'title': comic['title'],
        'img_url': comic['img'],
        'alt_text': comic['alt'],
        'transcription': comic.get('transcript', 'Транскрипт отсутствует.'),
        'comic_number': comic['num']
    }


def fetch_latest_comic_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['num']


def send_random_comic(bot, chat_id):
    comic = fetch_comic()
    if comic:
        bot.send_photo(chat_id, comic['img_url'], caption=f'{comic["title"]}\n{comic["alt_text"]}')
    else:
        bot.send_message(chat_id, 'Ошибка загрузки комикса')





