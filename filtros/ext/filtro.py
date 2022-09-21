# IMPORT MODULES

import bot
from bot import *
from filtros.hashtag import *
from filtros.mention import *

from datetime import timezone, datetime, timedelta

import pyjokes
import chistesESP

# YOUR CODE HERE
translator = Translator()

class Funciones:

    def __init__(self, update, context, chat, user, message):
        self.update = update
        self.context = context
        self.chat = chat
        self.user = user
        self.message = message

    def alertar_usuario(self, user_id):
        self.chat.id = str(self.chat.id).replace("-100", "")
        self.context.bot.sendMessage(chat_id=user_id,
                                     text=f'Te acaban de mensionar en {self.chat.title}\nel usuario {self.user.first_name} \n<a href="https://t.me/c/{str(self.chat.id)}/{str(self.message.message_id)}">enlace del mensaje</a>',
                                     parse_mode=ParseMode.HTML)

    def recibir_imagen(self, archivo):
        self.context.bot.sendChatAction(chat_id=self.chat.id, action='upload_photo')

        map_file_id = {
            "horario": "AgACAgEAAxkDAAIp4WKRmN4StpE_RU9Hhb-6zEU3-cBBAALFqjEbbUcJRJbwqTMM3AyUAQADAgADcwADJAQ",
            "horario-kelvyn": "AgACAgEAAx0CUEEdpwABBWWGYytLCGLFzpspvQ6M4mxQGr1zEs8AAreqMRs22ThF6ZjgvFzXnAUBAAMCAANzAAMpBA",
            "horario-bryan": "AgACAgEAAxkBAAIqvmKZOULq-7Q45I0uC-Xs3kS_SNMoAALLqTEbJIpBREKWEiBN4nC_AQADAgADcwADJAQ",
            "pensum": "AgACAgEAAxkBAAIqwmKZOaxEjLw5cWEl6xfrMxd5ck3KAAICqjEbD2NoRAABrvALEEXAcQEAAwIAA3MAAyQE",
            "calendario": "AgACAgEAAx0CUEEdpwABBU6wYx0qgIqynBRNDXLmsVxy1ZqsPc0AAtWrMRvxAuhEHndRV5OGCroBAAMCAANzAAMpBA"}
        buttons = [[
            bot.InlineKeyboardButton(text="eliminar mensaje", callback_data="btn_cerrar")
        ]]

        file_id = map_file_id[archivo]
        self.context.bot.sendPhoto(chat_id=self.chat.id, photo=file_id, reply_markup = bot.InlineKeyboardMarkup(buttons))

        self.context.bot.deleteMessage(chat_id=self.chat.id, message_id=self.message.message_id)


    def recibir_broma(self):
        try:
            broma = pyjokes.get_joke()
            broma_traducida = translator.translate(text=broma, dest='es')
            self.context.bot.sendMessage(chat_id=self.chat.id, text=broma_traducida.text)

        except:
            self.context.bot.sendMessage(chat_id=self.chat.id, text='Soy un bot no un comendiante :v')

    def recibir_chiste(self):
        try:
            chiste = chistesESP.get_random_chiste()
            self.context.bot.sendMessage(chat_id=self.chat.id, text=chiste)

        except:
            self.context.bot.sendMessage(chat_id=self.chat.id, text='Soy un bot no un comendiante :v')

    def recibir_hora(self):
        now_utc = datetime.now(timezone('UTC'))
        fecha = now_utc.astimezone(timezone("America/Santo_Domingo"))
        self.context.bot.sendMessage(chat_id=self.chat.id, text=f"son las: {fecha.strftime('%I:%M:%S %p')}")

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
                voice.save("comandos/media/audio/nota.mp3")
                with open('comandos/media/audio/nota.mp3', 'rb') as video:
                    self.context.bot.send_voice(chat_id=self.chat.id, voice=video)

            elif info.src == 'es':
                voice = gTTS(text=message, lang='es', slow=False)
                voice.save("comandos/media/audio/nota.mp3")
                with open('comandos/media/audio/nota.mp3', 'rb') as video:
                    self.context.bot.send_voice(chat_id=self.chat.id, voice=video)

        except Exception as ex:
            self.context.bot.sendMessage(chat_id=self.chat.id,
                                         text="Ocurrio un error al enviar el audio {}: {}".format(self.user.first_name, ex))
