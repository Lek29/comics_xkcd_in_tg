# XKCD Comics Bot
Этот проект представляет собой Telegram-бота для отправки случайных комиксов XKCD.

## Функционал
- Получение случайного комикса

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
  
4. Запуск бота

     `python main.py`

## Файлы проекта

- `main.py` — Основной файл для запуска бота.

- `utils.py` — Функции для скачивания комиксов.

- `.env` — Файл с конфиденциальными данными (не загружать в публичный репозиторий!).
