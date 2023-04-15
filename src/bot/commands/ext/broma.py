# Dependencias necesarias desde el script principal
from bot import Update, CallbackContext, pyjokes, Translator

# Codigo aqui
translator = Translator()

def command(update:Update, context:CallbackContext):
    try:
        broma = pyjokes.get_joke()
        broma_traducida = translator.translate(text=broma, dest='es')
        context.bot.sendMessage(chat_id=update.effective_chat.id,
                                text=broma_traducida.text)

    except:
        context.bot.sendMessage(chat_id=update.effective_chat.id,
                                text='No me se ninguno 😒')