import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

Token='6028092658:AAHVLnUYolGzqIW2mCphMwhJTH13oqbOiI0'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я чат-бот "Первокурсник". Чем могу помочь?')

def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    response = get_response(text)
    update.message.reply_text(response)

def get_response(text: str) -> str:
    if "расписан" in text:
        return "Для просмотра расписания советую перейти на сайт omgtu.ru."
    elif "аудитор" in text or "где находится" in text:
        return "План аудиторий находится на сайте omgtu.ru."
    elif "учебник" in text:
        return "Учебники вы можете взять в библиотеке ОмГТУ."
    elif "лекц" in text or "материал" in text:
        return "Лекцию мы можете найти в определенных аудиториях в определенное время, согласно расписаниб."
    elif "препод" in text:
        if "препод" in text and "лучший" in text:
            return "Артемий Андреевич, разумеется."
        else:
            return "Информацию о преподавателях вы можете найти на сайте ОмГТУ, или познакомиться с ними лично."

    elif "помощь" in text or "консультация" in text:
        return "Если вам нужна помощь, звоните 01."
    else:
        return "Задай нормальный вопрос."

def main() -> None:

    updater = Updater(token=Token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()