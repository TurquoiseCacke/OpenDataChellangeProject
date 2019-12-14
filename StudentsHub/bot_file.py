from telegram import *
from telegram.ext import *
import sqlite3
from config import getToken, getDbName


def startHandler(update: Update, context: CallbackContext):
    pass


def textHandler(update: Update, context: CallbackContext):
    database = sqlite3.connect(db)
    cursor = database.cursor()
    cursor.execute(f"select * from users where user_id='{update.effective_chat.id}'")
    users_data = cursor.fetchone()
    if users_data:
        action, lang = users_data[1:3]
    else:
        action = lang = None

    if action:
        pass
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='No actions')


def imageHandler(update: Update, context: CallbackContext):
    print(update)
    for photo in update.message.photo:
        context.bot.send_photo(photo=photo.file_id, chat_id=update.effective_chat.id)


bot_token = getToken()
db = getDbName() + '.db'


def main():
    updater = Updater(token=bot_token, use_context=True)

    updater.dispatcher.add_handler(MessageHandler(Filters.photo, imageHandler))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, textHandler))
    updater.dispatcher.add_handler(CommandHandler('start', startHandler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()