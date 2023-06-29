from bot import Update, CallbackContext
from .cmd import start, help

def start_command(update: Update, context:CallbackContext) -> None:
    start.command(update, context)

def help_command(update: Update, context:CallbackContext) -> None:
    help.command(update, context)
