from bot import Update, CallbackContext, ParseMode, ConversationHandler, ChatAction
from googletrans import Translator

translator = Translator()

class Traduce:
    def __init__(self, update, context) -> None:
        self.update = update
        self.context = context

    def Traducir(self, text):
        info = translator.translate(text)
        
        # Mostrar el estado de escribiendo mientras traduce el texto
        self.context.bot.sendChatAction(self.update.effective_chat.id, ChatAction.TYPING)
        
        if info.src == 'en':
            traduccion = translator.translate(text=text, dest='es').text
            return traduccion

        elif info.src == 'es':
            traduccion = translator.translate(text, dest='en').text
            return traduccion

        else:
            return "No se pudo traducir eso, lo siento 😢"


def command(update:Update, context:CallbackContext) -> ConversationHandler.END:
    message = update.effective_message
    message = str(message.text)
    chat_id = update.effective_chat.id
    msg = str(message).lower()

    # Instanciando la clase Traducir
    traducir = Traduce(update, context)
    
    # Removiendo el texto /traduce del mensaje para no traducir el comando
    msg = msg.replace("/traduce", " ")
    
    msg = ''.join(msg)
    

    response = traducir.Traducir(text=msg)

    context.bot.sendMessage(chat_id=chat_id,
                            parse_mode=ParseMode.HTML,
                            text="<pre>{}</pre>".format(response))
    
def hashtag(update:Update, context:CallbackContext) -> None:
    mensaje = str(update.effective_message.reply_to_message.text).split
    chat_id = update.effective_chat.id
    msg = str(mensaje).lower()
    
    # Instanciando la clase Traducir
    traducir = Traduce(update, context)
    
    # Removiendo el texto #traduce del mensaje
    msg = msg.replace("#traduce", " ")

    response = traducir.Traducir(text=msg)

    context.bot.sendMessage(chat_id=chat_id,
                            parse_mode=ParseMode.HTML,
                            text="<pre>{}</pre>".format(response))


    
        