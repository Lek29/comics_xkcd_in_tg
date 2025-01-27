import requests
from utils import download_images

def fetch_comic(comic_number=1):
    try:
        if comic_number:
            url = f'https://xkcd.com/{comic_number}/info.0.json'
        else:
            url = 'https://xkcd.com/info.0.json'

        response = requests.get(url)
        response.raise_for_status

        comic = response.json()
        
        title = comic['title']
        img_url = comic['img']
        alt_text = comic['alt']
        transcript = comic.get('tarscript', 'Транскрипт отсуттвует.')

        download_images(img_url, 'comics', prefix=f'xkcd_{comic_number or "latest"}')

    except requests.exceptions.HTTPError as http_err:
        print(f"Ошибка HTTP: {http_err}")
    except Exception as err:
        print(f"Произошла ошибка: {err}")




def main():
    fetch_comic()


if __name__ == '__main__':
    main()
