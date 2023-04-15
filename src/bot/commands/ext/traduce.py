# Dependencias necesarias desde el script principal
from bot import Update, CallbackContext, ConversationHandler, Translator, ParseMode

# Codigo aqui

translator = Translator()

def command(update:Update, context:CallbackContext):

    message = update.effective_message
    mensaje = str(message.text).split()
    chat = update.effective_chat

    try:
        msg = str(message.reply_to_message.text).lower()
    except:
        msg = str(message.text).lower()

    if mensaje[0] == "/traduce":
        msg = msg.replace("/traduce", " ")
    elif mensaje[0] == "#traduce":
        msg = msg.replace("#traduce", " ")
    else:
        pass

    info = translator.translate(msg)
    if info.src == 'en':
        traduccion = translator.translate(text=msg, dest='es')

        context.bot.sendMessage(chat_id=chat.id, 
                                parse_mode=ParseMode.HTML,
                                text=f'<pre>{traduccion.text}</pre>')

    elif info.src == 'es':
        traduccion = translator.translate(msg, dest='en')
        context.bot.sendMessage(chat_id=chat.id,
                                parse_mode=ParseMode.HTML,
                                text=f"<pre>{traduccion.text}</pre>")
    else:
        context.bot.sendMessage(chat_id=chat.id, 
                                     text=f'No puedo traducir {msg}, lo siento 😢')

    return ConversationHandler.END