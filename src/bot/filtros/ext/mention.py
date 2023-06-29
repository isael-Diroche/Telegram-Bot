# IMPORT MODULES

import bot
from bot import Update, CallbackContext

# YOUR CODE HERE

def filter_mention(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message

    msg = message.text

    ft = bot.Filtrar(update, context)

    for x in msg.split():
        if x == "@isael_diroche":
            user = "isael"
            ft.user_alert(user=user, from_user=user.first_name, from_group=chat.title)

    print(f"esto es un mention {msg.split()}")



