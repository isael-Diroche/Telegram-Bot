# Dependencias necesarias desde el script principal
from bot import Update, CallbackContext, chistesESP

# Codigo aqui
def command(update:Update, context:CallbackContext):
    try:
        chiste = chistesESP.get_random_chiste()
        context.bot.sendMessage(chat_id=update.effective_chat.id,
                                text=chiste)

    except:
        context.bot.sendMessage(chat_id=update.effective_chat.id,
                                text='Soy un bot no un comendiante :v')