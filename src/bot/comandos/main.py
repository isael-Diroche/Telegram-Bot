from bot import Update, CallbackContext
from .cmd import start, help, traduce, voice

def start_command(update: Update, context:CallbackContext) -> None:
    start.command(update, context)

def help_command(update: Update, context:CallbackContext) -> None:
    help.command(update, context)

def traduce_command(update: Update, context:CallbackContext) -> None:
    traduce.command(update, context)

def voice_command(update: Update, context:CallbackContext) -> None:
    voice.command(update, context)
