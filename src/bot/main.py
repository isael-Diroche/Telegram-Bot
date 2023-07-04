from telegram import Update, ParseMode, ChatAction
from telegram.ext import CallbackContext, ConversationHandler

from googletrans import Translator
from bs4 import BeautifulSoup
from gtts import gTTS
import requests

translator = Translator()

class Comando:
    def __init__(self) -> None:
        pass
    
    def actualizarComandos(self, context) -> None:
        comandos = [
            ("/start", "Inicio del bot"),
            ("/help", "Pedir ayuda al bot"),
            ("/traduce", "Traducir ingles / español"),
            ("/voice", "Convertir texto a voz"),
            ("/chiste", "Enviar un chiste"),
            ("/motivame", "Envia un mensaje motivador"),
        ]
        
        context.bot.setMyCommands(comandos)
        
    def start(self, update, context) -> None:
        user_name = update.effective_user.first_name
        user_id = update.effective_user.id
        get_members = context.bot.get_chat_member(update.effective_chat.id, user_id)
        status = str(get_members.status)
        get_members = translator.translate(status, dest="es").text
        
        get_member_count = context.bot.get_chat_member_count(update.effective_chat.id)
    
        msg = "Hola {}({}) gracias por activarme, por lo que veo aqui hay {} usuarios. Si necesitas ayuda en algo no dudes en consultarme, si quieres saber lo que puedo hacer puedes usar el comando /help o darle un vistazo a la <a href='https://github.com/isael-Diroche/TeleHelpBot/tree/main#comandos'>documentacion</a> por @IsaelDiroche".format(user_name, get_members, get_member_count)

        try:
            context.bot.sendMessage(chat_id = update.effective_chat.id,
                                    text = msg,
                                    parse_mode = ParseMode.HTML)
            
            self.actualizarComandos(context)
        except:
            with Exception as ex:
                context.bot.sendMessage(chat_id = update.effective_chat.id, text=ex)
    
    def help(self, update, context) -> None:
        chat_id = update.effective_chat.id
        user_name = update.effective_user.first_name
        msg = """Hola {} te voy a mostrar los comandos que poseo.\n\n/start\n/help\n\nPor ahora esos son todos si necesitas mas informacion acerca de puedes consultar la <a href="https://telegra.ph/Firulais-Documentacion-05-27">documentacion</a> del las funcionalidades. Tambien puedes reportar algun error en el bot o mejora en los <a href="https://github.com/isael-Diroche/TeleHelpBot/issues">issues</a> del repositorio de TeleHelpBot""".format(user_name)

        context.bot.sendMessage(chat_id = chat_id,
                                text = msg,
                                parse_mode = ParseMode.HTML)
        
    def traduce(self, update, context) -> ConversationHandler.END:
        message = str(update.effective_message.text).lower()
        chat_id = update.effective_chat.id
        
        try:
            message = str(update.effective_message.reply_to_message.text).lower()
        except:
            message = str(update.effective_message.text).replace("#traduce ", "")
            
        info = translator.translate(message)
        
        # Mostrar el estado de escribiendo mientras traduce el texto
        context.bot.sendChatAction(chat_id = update.effective_chat.id,
                                   action = ChatAction.TYPING)
        
        if info.src == 'en':
            traduccion = translator.translate(message, dest='es').text
            context.bot.sendMessage(chat_id=chat_id,
                                    parse_mode=ParseMode.HTML,
                                    text="<pre>{}</pre>".format(traduccion))

        elif info.src == 'es':
            traduccion = translator.translate(message, dest='en').text
            context.bot.sendMessage(chat_id=chat_id,
                                    parse_mode=ParseMode.HTML,
                                    text="<pre>{}</pre>".format(traduccion))

        else:
            context.bot.sendMessage(chat_id=chat_id,
                                    parse_mode=ParseMode.HTML,
                                    text="Lo siento, no puedo traducir eso 😔")

    def voice(self, update, context) -> None:
        message = str(update.effective_message.text).lower()
        chat_id = update.effective_chat.id    
        path="./src/assets/notes/"
                
        try:
            message = str(update.effective_message.reply_to_message.text).lower()
        except:
            message = str(update.effective_message.text).replace("#voice ", "")

        info = translator.translate(message)
        file = path + "record.mp3"
        
        context.bot.sendChatAction(chat_id=update.effective_chat.id,
                                        action=ChatAction.RECORD_AUDIO)

        if info.src == 'en':
            voice = gTTS(text=message, lang='en', slow=False)
            voice.save(file)
            with open(file, 'rb') as record:
                context.bot.send_voice(chat_id=update.effective_chat.id, voice=record)

        elif info.src == 'es':
            voice = gTTS(text=message, lang='es', slow=False)
            voice.save(file)
            with open(file, 'rb') as record:
                context.bot.send_voice(chat_id=update.effective_chat.id, voice=record)

    def chiste(self, update, context) -> None:
        message = str(update.effective_message.text).lower()
        chat_id = update.effective_chat.id
        
        # Mostrar el estado de escribiendo mientras traduce el texto
        context.bot.sendChatAction(chat_id = update.effective_chat.id,
                                   action = ChatAction.TYPING)
        
        response = requests.get('http://www.todo-chistes.com/chistes-al-azar')
        soup = BeautifulSoup(response.text, "html.parser")
        chiste = soup.find("div", "field-chiste").text
        
        context.bot.sendMessage(chat_id, chiste)
        
    
    def motivame(self, update, context) -> None:
        message = str(update.effective_message.text).lower()
        chat_id = update.effective_chat.id

        # Mostrar el estado de escribiendo mientras traduce el texto
        context.bot.sendChatAction(chat_id = update.effective_chat.id,
                                   action = ChatAction.TYPING)
        
        respuesta = requests.get('https://frasesmotivacion.net/frase-aleatoria')
        soup = BeautifulSoup(respuesta.text, "html.parser")
        frase = soup.find("blockquote").text
        
        context.bot.sendMessage(chat_id, frase)
        
        
        
        
        
    
    
# Comandos con el filtro de hashtag (#)    
class Hashtag(Comando):
    
    def main(self, update, context):    
        msg = str(update.effective_message.text).lower()
        msg = str(msg).split()
            
        for x in msg:
            if x == "#start":
                self.start(update, context)
                
            elif x == "#traduce":
                self.traduce(update, context)
                
            elif x == "#voice":
                self.voice(update, context)
                
            else:
                pass
    