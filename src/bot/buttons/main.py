# IMPORT MODULES
from bot import *

# YOUR CODE HERE

def detele_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.message.delete()
