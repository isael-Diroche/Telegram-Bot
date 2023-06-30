# IMPORT MODULES
from telegram import CallbackQuery, Update, ParseMode, ChatAction, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler, CommandHandler, Updater, Dispatcher, Filters, CallbackQueryHandler, CallbackContext, MessageHandler

from googletrans import Translator
from bs4 import BeautifulSoup
import requests
import gtts
import os

from src.bot.main import Comando, Hashtag

TOKEN = os.getenv('TOKEN')
comando = Comando()
hashtag = Hashtag()

def main() -> None:
    updater = Updater(token=TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler(command="start", callback=comando.start))
    updater.dispatcher.add_handler(CommandHandler(command="help", callback=comando.help))
    updater.dispatcher.add_handler(CommandHandler(command="traduce", callback=comando.traduce))
    updater.dispatcher.add_handler(CommandHandler(command="voice", callback=comando.voice))
    #updater.dispatcher.add_handler(CommandHandler(command="chiste", callback=comando.chiste))

    # FILTROS PRINCIPALES   
    # updater.dispatcher.add_handler(MessageHandler(filters=Filters.entity("mention"), callback=mention.filter_mention))
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.entity("hashtag"), callback=hashtag.main))

    entry_points = []
    states = {}
    fallbacks = []

    updater.dispatcher.add_handler(ConversationHandler(
        entry_points=entry_points, states=states, fallbacks=fallbacks, per_message=False))
    updater.start_polling(0.1)
    print("Esto vivo!")
    updater.idle()


if __name__ == "__main__":
    main()
