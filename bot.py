# IMPORT MODULES
from telegram import CallbackQuery, Update, ParseMode, ChatAction, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler, CommandHandler, Updater, Dispatcher, Filters, CallbackQueryHandler, CallbackContext, MessageHandler
from src.bot.comandos.main import *
from src.bot.comandos.cmd.traduce import *


from googletrans import Translator
from bs4 import BeautifulSoup
import requests
import gtts
import os


TOKEN = os.getenv('TOKEN')


def main() -> None:
    updater = Updater(token=TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler(command="start", callback=start_command))
    updater.dispatcher.add_handler(CommandHandler(command="help", callback=help_command))
    updater.dispatcher.add_handler(CommandHandler(command="traduce", callback=traduce_command))
    updater.dispatcher.add_handler(CommandHandler(command="voice", callback=voice_command))
    #updater.dispatcher.add_handler(CommandHandler(command="chiste", callback=chiste_command))

    # FILTROS PRINCIPALES   
    # updater.dispatcher.add_handler(MessageHandler(filters=Filters.entity("mention"), callback=mention.filter_mention))
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.entity("hashtag"), callback=hashtag))

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
