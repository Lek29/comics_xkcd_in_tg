import os
import requests
from urllib.parse import urlsplit, unquote, urlparse
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


def download_images(image_url, save_directory, prefix='image'):
    os.makedirs(save_directory, exist_ok=True)
    print(f'Сохранение в папку: {os.path.abspath(save_directory)}')
    response = requests.get(image_url)
    response.raise_for_status()
    file_extention = get_file_extention(image_url)
    file_name = os.path.join(save_directory, f'{prefix}{file_extention}')
    with open(file_name, 'wb') as file:
        file.write(response.content)
        print(f'скачано: {file_name}')


def get_file_extention(url):
    parsed_url = urlsplit(url)
    path = parsed_url.path
    decoded_path = unquote(path)
    _, file_extention = os.path.splitext(decoded_path)
    return file_extention

def fetch_latest_comic_number():
    latest_comic = fetch_comic()
    if latest_comic:
        return latest_comic['comic_number']
    return None


def download_all_comics(save_directory='comics'):
    latest_comic_number = fetch_latest_comic_number()

    for comic_number in range(1, latest_comic_number + 1):
        comic_data = fetch_comic(comic_number)
        if comic_data:
            img_url = comic_data['img_url']
            download_images(img_url, save_directory, prefix=f'xckg_{comic_number}')
            print(f'Скачан новый комикс {comic_number}: {comic_data["title"]}')


def check_and_download_new_comics(save_directory='comics'):
    latest_comic_number = fetch_latest_comic_number()

    latest_comic_filename = os.path.join(save_directory, f'xkcd_{latest_comic_number}')
    if not os.path.exists(latest_comic_filename):
        print(f'Найден новый комикс: {latest_comic_filename}')
        new_comic = fetch_comic(latest_comic_number)
        if new_comic:
            img_url = new_comic['img_url']
            download_images(img_url, save_directory, prefix=f'xkcd_{latest_comic_number}')
            print(f'Скачан новый новый комикс {latest_comic_number}: {new_comic["title"]}')
    else:
        print('Новых комиксов нет')


def download_specific_comic(comic_number, save_directory='comics'):
    comics = fetch_comic(comic_number)

    if comics is None:
        print(f'Ошибка: комикс {comic_number} не найден.')
        return

    img_url = comics['img_url']

    if not img_url:
        print(f'Ошибка: у комикса {comic_number} нет изображения.')
        return

    download_images(img_url, save_directory, prefix=f'xkcd_{comics["comic_number"]}')
    print(f'Скачан комикс {comic_number}: {comics["title"]}')

def download_comic(choice=None, save_directory='comics'):
    if choice == 'all':
        download_all_comics(save_directory)
    elif choice == 'new':
        check_and_download_new_comics(save_directory)
    elif choice == 'random':
        comics = fetch_comic(randint(1, fetch_latest_comic_number()))
        if comics:
            url_img = comics['img_url']
            download_images(url_img, save_directory, prefix=f'xkcd_{comics["comic_number"]}')
            print(f'Скачан комикс {comics["comic_number"]}: {comics["title"]}')

def send_comic(bot, chat_id, comic_number=None):
    comic = fetch_comic(comic_number)
    if comic:
        bot.send_photo(chat_id, comic['img_url'], caption=f'{comic["title"]}\n{comic["alt_text"]}')
    else:
        bot.send_message(chat_id, 'Ошибка загрузки комикса')

