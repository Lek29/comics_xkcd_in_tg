from utils import (download_all_comics, check_and_download_new_comics,
                   download_specific_comic, download_comic)
import telebot
import os
from dotenv import load_dotenv
from heandler import handle_start, handle_messages


def main():
    # while True:
    #     user_choice = input(
    #         "Выберите действие:\n"
    #
    #         "2 - Скачать все комиксы\n"
    #         "3 - Скачать случайный комикс\n"
    #         "4 - Скачать новый комикс (если есть)\n"
    #         "5 - Скачать комикс по номеру\n"
    #         "0 - Выход\n"
    #         "Ваш выбор: "
    #     )
    #     if user_choice == '2':
    #         download_comic('all')
    #     elif user_choice == '3':
    #         download_comic('random')
    #     elif user_choice == '4':
    #         download_comic('new')
    #     elif user_choice == '5':
    #         comic_number = input('Введите номер комикса: ')
    #         download_specific_comic(comic_number)
    #     elif user_choice == '0':
    #         break
    #     else:
    #         print("Неверный выбор. Попробуйте снова.")

    load_dotenv()

    token_tg = os.environ['TOKEN_TG']
    bot = telebot.TeleBot(token_tg)

    handle_start(bot)
    handle_messages(bot)


    bot.polling()

if __name__ == '__main__':
    main()
