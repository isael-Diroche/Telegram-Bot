# Dependencias necesarias desde el script principal
from bot import Update, CallbackContext, ConversationHandler, wikipedia, Translator

# Codigo aqui
translator = Translator()

def command(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    # user = update.effective_user
    message = update.effective_message

    msg = str(message.text).lower()
    mensaje = msg.split()

    if mensaje[0] == "/buscar":
        msg = msg.replace("/buscar", "")
    else:
        pass

    try:
        print(f'Buscando en wikipedia {msg}')
        context.bot.send_chat_action(chat_id=chat.id, action='typing')
        result = wikipedia.summary(msg, sentences=3)
        result = translator.translate(text=result, dest='es')
        context.bot.sendMessage(chat_id=chat.id, text=result.text)

    except wikipedia.DisambiguationError:
        context.bot.sendMessage(chat_id=chat.id, text=f'puedes especificar que {msg} buscas?')

    except wikipedia.exceptions.PageError:
        context.bot.sendMessage(chat_id=chat.id, text=f'No se pudo encontrar informacion acerca de {msg}')

    return ConversationHandler.END
