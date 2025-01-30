import telebot

from keyboards import first_keys
from utils import send_comic

def handle_start(bot: telebot.TeleBot):
    @bot.message_handler(commands=['start'])
    def start_buttons(message):
        bot.send_message(message.chat.id, 'Выбери команду',
                        reply_markup=first_keys()
                        )

def handle_messages(bot: telebot.TeleBot):
    @bot.message_handler(func=lambda messages: True)
    def handler_messages(message):
        chat_id = message.chat.id
        if message.text == 'Новый комикс':
            send_comic(bot, chat_id)
        elif message.text == 'Все комиксы':
            bot.send_message(chat_id, ' Скачивание всех комиксов не поддерживается в чате')
        elif message.text == 'Случайный комикс':
            send_comic(bot, chat_id, 'random')
        elif message.text == 'Комикс номер ...':
            bot.send_message(chat_id, 'Введите номер комикса:')
        elif message.text.isdigit():
            send_comic(bot, chat_id, int(message.text))
        else:
            bot.send_message(chat_id, "Неизвестная команда.")