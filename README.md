# XKCD Comics Bot
Этот Telegram-бот отправляет случайные комиксы из [XKCD](https://xkcd.com/). Просто добавьте бота в группу или чат, и он будет радовать вас случайными комиксами!

## Функционал
- Получение случайного комикса XKCD.
- Отправка комикса в Telegram-группу или чат.

## Установка и настройка
1. Клонирование репозитория.
   
    - ` git clone https://github.com/yourusername/xkcd-bot.git`
  
    - `cd xkcd-bot`
   
3. Установка зависимостей.

    Создайте виртуальное окружение (опционально) и установите зависимости:
  
      `python -m venv venv`

      `source venv/bin/activate  # Для Linux/macOS`

      `venv\Scripts\activate  # Для Windows`

      `pip install -r requirements.txt`
    
3. Настройка переменных окружения

    Создайте файл .env в корне проекта и добавьте в него токен Telegram-бота:

      `TOKEN_TG=YOUR_TELEGRAM_BOT_TOKEN`
   
      `GROUP_CHAT_ID=YOUR_GROUP_CHAT_ID`
  
5. Запуск бота

     `python main.py`

## Файлы проекта

- `main.py` — Основной файл для запуска бота.

- `utils.py` — Вспомогательные функции.

- `.env` — Файл с конфиденциальными данными (не загружать в публичный репозиторий!).
