from utils import (download_all_comics, check_and_download_new_comics,
                   download_specific_comic, download_comic)
import telebot
import os
from dotenv import load_dotenv
from heandler import handle_start, handle_messages


def main():
    load_dotenv()

    token_tg = os.environ['TOKEN_TG']
    bot = telebot.TeleBot(token_tg)

    handle_start(bot)
    handle_messages(bot)


    bot.polling()

if __name__ == '__main__':
    main()
