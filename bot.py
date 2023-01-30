# IMPORT MODULES
from telegram import CallbackQuery, Update, ParseMode, ChatAction, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler, CommandHandler, Updater, Dispatcher, Filters, CallbackQueryHandler, CallbackContext, MessageHandler

from googletrans import Translator
from firebase import firebase
import sqlite3
from gtts import gTTS
import os

#from migrations import migrate
from src.bot.filters.main import *
from src.bot.filters.ext import mention, hashtag
from src.bot.filters.ext.messages import messages
from src.bot.commands.main import *
from src.conexion import *

# YOUR CODE HERE

TOKEN = '1985333182:AAFKNzhBvBG6Gkp-uFx76021iqM7iqnRDo4'
#1865520485:AAGs-C7Buc0C3pUTry0HqA-DqKZt04fJBVE

TRADUCIR, BUSCAR= range(2)

UPDATES = True

def traduce_conversation(update, context):
    update.message.reply_text("Dime lo que quieres traducir")
    return TRADUCIR

def error(update, context):#
    errores = context.error
    print(f"Update: {update} \nEl error es el siguiente:\n{errores}")

def main() -> None:
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # COMANDOS PRINCIPALES
    dp.add_handler(CommandHandler(command="start", callback=start_command))
    dp.add_handler(CommandHandler(command="help", callback=help_command))
    dp.add_handler(CommandHandler(command="reporte", callback=report_command))
    dp.add_handler(CommandHandler(command="contacto", callback=contact_command))
    dp.add_handler(CommandHandler(command="traduce", callback=traducir_command))
    dp.add_error_handler(callback=error)

    # FILTROS PRINCIPALES 
    dp.add_handler(MessageHandler(filters=Filters.entity("mention"), callback=mention.filter_mention))
    dp.add_handler(MessageHandler(filters=Filters.entity("hashtag"), callback=hashtag.filter_hashtag))

    # IMPORTANTE!
    # dp.add_handler(MessageHandler(filters=Filters.all, callback=all_messages))

    entry_points = [
        #MessageHandler(filters=Filters.document.pdf or Filters.document.docx, callback=archivar_conversation),
        #CommandHandler(command="busca", callback=busca_conversation),
        #CommandHandler(command="traduce", callback=traduce_conversation),
        MessageHandler(filters=Filters.text, callback=messages),
        #CallbackQueryHandler(pattern='btn_cerrar', callback=botones_eliminar),
        #CallbackQueryHandler(pattern='btn_contacto', callback=comando_contacto),
    ]
    states = {
        #TRADUCIR: [MessageHandler(Filters.text, comando_translate)],
        #BUSCAR: [MessageHandler(Filters.text, comando_buscar)]
    }
    fallbacks = []

    dp.add_handler(ConversationHandler(entry_points=entry_points, states=states, fallbacks=fallbacks, per_message=False))
    updater.start_polling(0.1)
    print("Esto vivo!")
    updater.idle()

if __name__ == "__main__":
    #migrate()
    main()