# IMPORT MODULES

from bot import *

# YOUR CODE HERE

def filter_hashtag(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message

    msg = message.text

    print(f"esto es un hashtag {msg}")

