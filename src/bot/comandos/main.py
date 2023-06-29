from bot import Update, CallbackContext
from .cmd import start

def start_command(update: Update, context:CallbackContext) -> None:
    start.command(update, context)

