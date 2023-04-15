# Dependencias necesarias desde el script principal
from bot import Update, CallbackContext, ParseMode
from bs4 import BeautifulSoup
import requests

# Codigo aqui

def frase_aleatoria():
    respuesta = requests.get('https://frasesmotivacion.net/frase-aleatoria')
    soup = BeautifulSoup(respuesta.text, "html.parser")
    chiste = soup.find("blockquote").text
    return chiste

def command(update:Update, context:CallbackContext):
    msg = frase_aleatoria()
    
    context.bot.sendMessage(chat_id=update.effective_chat.id, 
                            text=f'{msg}')

