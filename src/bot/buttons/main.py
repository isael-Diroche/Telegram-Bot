# IMPORT MODULES
from bot import *

# YOUR CODE HERE

def botones_eliminar(update, context):
    query = update.callback_query
    query.answer()
    query.message.delete()
