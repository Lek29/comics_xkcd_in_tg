import os
from dotenv import load_dotenv
from utils import  send_random_comic
import telebot


def handle_start(bot: telebot.TeleBot):
    bot.register_message_handler(lambda message: send_random_comic(bot, message.chat.id), commands=['start'])


def main():
    load_dotenv()

    token_tg = os.environ['TG_TOKEN']
    bot = telebot.TeleBot(token_tg)

    handle_start(bot)

    bot.polling()

if __name__ == '__main__':
    main()
