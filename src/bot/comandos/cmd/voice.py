from bot import Update, CallbackContext, Translator, ChatAction, gtts
from gtts import gTTS

translator = Translator()


class Voice:
    def __init__(self, update, context) -> None:
        self.update = update
        self.context = context

    def enviar_nota(self, text, path="./src/assets/notes/"):
        info = translator.translate(text)
        file = path + "record.mp3"
        self.context.bot.sendChatAction(chat_id=self.update.effective_chat.id,
                                        action=ChatAction.RECORD_AUDIO)

        if info.src == 'en':
            voice = gTTS(text=text, lang='en', slow=False)
            voice.save(file)
            with open(file, 'rb') as record:
                self.context.bot.send_voice(chat_id=self.update.effective_chat.id, voice=record)

        elif info.src == 'es':
            voice = gTTS(text=text, lang='es', slow=False)
            voice.save(file)
            with open(file, 'rb') as record:
                self.context.bot.send_voice(chat_id=self.update.effective_chat.id, voice=record)



def command(update: Update, context: CallbackContext) -> None:

    # Instanciando la clase Voice
    voice = Voice(update, context)

    message = str(update.effective_message.text).lower()
    message = str(update.effective_message.text).replace("/voice ", "")

    voice.enviar_nota(text=message)


def hashtag(update: Update, context: CallbackContext) -> None:
    message = str(update.effective_message.reply_to_message.text).lower()

    #Instanciando la clase Voice
    voice = Voice(update, context)
    
    voice.enviar_nota(message)