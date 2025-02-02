from random import randint
import requests


def fetch_comic(comic_number=None):
    try:
        if comic_number is None:
            url = f'https://xkcd.com/info.0.json'
        elif comic_number == 'random':
            random_number = randint(1, fetch_latest_comic_number())
            return fetch_comic(random_number)
        else:
            url = f'https://xkcd.com/{comic_number}/info.0.json'

        response = requests.get(url)
        response.raise_for_status()

        comic = response.json()

        title = comic['title']
        img_url = comic['img']
        alt_text = comic['alt']
        transcript = comic.get('transcript', 'Транскрипт отсуттвует.')

        return {
            'title': title,
            'img_url': img_url,
            'alt_text': alt_text,
            'transcription': transcript,
            'comic_number': comic.get('num', comic_number)
        }

    except requests.exceptions.HTTPError as http_err:
        print(f"Ошибка HTTP: {http_err}")
    except Exception as err:
        print(f"Произошла ошибка: {err}")


def fetch_latest_comic_number():
    latest_comic = fetch_comic()
    if latest_comic:
        return latest_comic['comic_number']
    return None


def fetch_random_comic():
    latest_number = fetch_latest_comic_number()
    random_number = randint(1, latest_number)
    return fetch_comic(random_number)


def send_random_comic(bot, chat_id):
    comic = fetch_random_comic()
    if comic:
        bot.send_photo(chat_id, comic['img_url'], caption=f'{comic["title"]}\n{comic["alt_text"]}')
    else:
        bot.send_message(chat_id, 'Ошибка загрузки комикса')





