# Dependencias necesarias desde el script principal
from bot import Update, CallbackContext

from .ext import start, ayuda, reporte, contacto, traduce, texto_a_voz

# Codigo aqui

def start_command(update: Update, context:CallbackContext) -> None:
    start.command(update, context)

def help_command(update: Update, context: CallbackContext) -> None:
    ayuda.command(update, context)

def report_command(update: Update, context: CallbackContext) -> None:
    reporte.command(update, context)

def traducir_command(update: Update, context: CallbackContext) -> None:
    traduce.command(update, context)

def voice_command(update: Update, context: CallbackContext) -> None:
    texto_a_voz.command(update, context)

def contact_command(update: Update, context: CallbackContext) -> None:
    contacto.command(update, context)

# Nuevos comandos en camino

def chiste_command(update: Update, context: CallbackContext) -> None:

#def broma_command(update: Update, context: CallbackContext) -> None:

#def archivar_command(update: Update, context: CallbackContext) -> None:

#def buscar_command(update: Update, context: CallbackContext) -> None:

