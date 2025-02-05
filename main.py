import os
from random import randint
from dotenv import load_dotenv
from utils import (
    send_random_comic,
    fetch_latest_comic_number,
    fetch_comic
)
import telebot


def main():
    load_dotenv()

    group_chat_id = os.environ['GROUP_CHAT_ID']
    token_tg = os.environ['TG_TOKEN']
    bot = telebot.TeleBot(token_tg)

    latest_comic_number = fetch_latest_comic_number()
    random_comic_number = randint(1, latest_comic_number)
    comic = fetch_comic(random_comic_number)

    send_random_comic(bot, group_chat_id, comic)
    print("Комикс успешно опубликован.")

    bot.polling()


if __name__ == '__main__':
    main()
