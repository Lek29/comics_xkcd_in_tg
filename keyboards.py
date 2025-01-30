from telebot import types

def first_keys():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Новый комикс')
    button2 = types.KeyboardButton('Все комиксы')
    button3 = types.KeyboardButton('Случайный комикс')
    button4 = types.KeyboardButton('Комикс номер ...')
    keyboard.add(button1, button2, button3, button4)
    return keyboard