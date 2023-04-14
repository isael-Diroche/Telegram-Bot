# Dependencias necesarias desde el script principal
from bot import Update, CallbackContext, Translator, gTTS

# Codigo aqui

translator = Translator()

'''
    def comando_voice(self, message):
        self.context.bot.sendChatAction(chat_id=self.chat.id, action='upload_voice')
        try:
            message = str(message.reply_to_message.text).lower()

        except:
            message = str(message.text).lower()
            message = str(message).replace("/voice", "")

        info = translator.translate(message)
        try:
            if info.src == 'en':  # et
                voice = gTTS(text=message, lang='en', slow=False)
                voice.save("./src/static/notes/nota.mp3")
                with open('./src/static/notes/nota.mp3', 'rb') as video:
                    self.context.bot.send_voice(chat_id=self.chat.id, voice=video)

            elif info.src == 'es':
                voice = gTTS(text=message, lang='es', slow=False)
                voice.save("./src/static/notes/nota.mp3")
                with open('./src/static/notes/nota.mp3', 'rb') as video:
                    self.context.bot.send_voice(chat_id=self.chat.id, voice=video)

        except Exception as ex:
            self.context.bot.sendMessage(chat_id=self.chat.id,
                                         text="Ocurrio un error al enviar el audio {}: {}".format(self.user.first_name, ex))
'''

def command(update: Update, context: CallbackContext) -> None:
    notes_path = "./src/static/notes/nota.mp3"
    chat_id = update.effective_chat.id

    context.bot.sendChatAction(chat_id=update.effective_chat.id,
                               action='upload_voice')
    try:
        message = str(update.effective_message.reply_to_message.text).lower()

    except:
        message = str(update.effective_message.text).lower()
        message = str(update.effective_message.text).replace("/voice", "")

    info = translator.translate(message)

    try:
        if info.src == 'en':
            voice = gTTS(text=message, lang='en', slow=False)
            voice.save(notes_path)
            with open(notes_path, 'rb') as video:
                context.bot.send_voice(chat_id=chat_id, voice=video)

        elif info.src == 'es':
            voice = gTTS(text=message, lang='es', slow=False)
            voice.save(notes_path)
            with open(notes_path, 'rb') as video:
                context.bot.send_voice(chat_id=chat_id, 
                                       voice=video)

    except Exception as ex:
        context.bot.sendMessage(chat_id=chat_id,
                                text="Ocurrio un error al enviar el audio {}: {}".format(update.effective_user.first_name, ex))

