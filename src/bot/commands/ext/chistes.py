# Dependencias necesarias desde el script principal
from bs4 import BeautifulSoup
import requests
from bot import Update, CallbackContext

def get_random_chiste():
    response = requests.get('http://www.todo-chistes.com/chistes-al-azar')
    soup = BeautifulSoup(response.text, "html.parser")
    chiste = soup.find("div", "field-chiste").text
    return chiste

def command(update:Update, context:CallbackContext):
    chiste = get_random_chiste()
    context.bot.sendMessage(chat_id=update.effective_chat.id,
                            text=chiste)