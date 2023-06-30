# IMPORT MODULES
from telegram import CallbackQuery, Update, ParseMode, ChatAction, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler, CommandHandler, Updater, Dispatcher, Filters, CallbackQueryHandler, CallbackContext, MessageHandler
from src.bot.comandos.main import *
from googletrans import Translator
import os

from src.bot.main import Comando

TOKEN = os.getenv('TOKEN')

comando = Comando(Update, CallbackContext)

def main() -> None:
    updater = Updater(token=TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler(command="start", callback=comando.start))
    updater.dispatcher.add_handler(CommandHandler(command="help", callback=help_command))
    #updater.dispatcher.add_handler(CommandHandler(command="traduce", callback=traduce_command))
    #updater.dispatcher.add_handler(CommandHandler(command="voice", callback=voice_command))
    #updater.dispatcher.add_handler(CommandHandler(command="chiste", callback=chiste_command))

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
