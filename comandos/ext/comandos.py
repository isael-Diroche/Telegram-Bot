# IMPORT MODULES
from googletrans import Translator
from gtts import gTTS
import wikipedia
import os

import bot
from bot import *
from filtros.ext.filtro import Funciones
from database.ext.conexion import *

# YOUR CODE HERE
translator = Translator()
vcard = """BEGIN:VCARD
VERSION:3.0
ORG:Instituto Tecnologico de las americas
TITLE:Estudiante
TEL;TYPE=WORK,VOICE:+1(809)678-1819
ADR;TYPE=WORK,PREF:;;Villa altagracia;Santo Domingo;Republica Domnicana
BDAY:6 Septiembre 2002
EMAIL;PREF=1:isaeldiroche00@gmail.com
NOTE:Contactame para mas información
END:VCARD"""

class ComandosEspeciales:

    def __init__(self, update, context):
        self.update = update
        self.context = context
        self.chat = update.effective_chat
        self.user = update.effective_user
        self.message = update.effective_message

    def enviar_contacto(self, card):

        self.context.bot.sendContact(chat_id=self.chat.id,
                                     phone_number="+18096781819",
                                     first_name="Isael",
                                     last_name="Diroche",
                                     vcard=card,
                                     disable_notification=False)

        self.context.bot.sendLocation(chat_id=self.chat.id,
                                      latitude=18.673011566297106,
                                      longitude=-70.16772176699745,
                                      disable_notification=False)

    def start_command(self):
        get_members = self.context.bot.get_chat_member(chat_id=self.chat.id, user_id=self.user.id)
        puesto = translator.translate(str(get_members.status), dest="es")
        get_members = puesto.text
        get_members_count = self.context.bot.get_chat_members_count(self.chat.id)

        comandos = [
            ("/start", "Inicio del bot"),
            ("/help", "Pedir ayuda al bot"),
            ("/menu", "Abrir un menu"),
            ("/busqueda", "Buscar informacion en la web"),
            ("/traduce", "Traducir algun texto ingles/español"),
            ("/text", "Convierte texto en un archivo .txt"),
            ("/file", "Devuelve el link de un archivo"),
            ("/rename", "Cambia el nombre de un archivo (PDF only)"),
            ("/report", "Reportar algun cambio o mejora"),
        ]
        mensaje_start = "Hola {} gracias por activarme,\npor lo que veo aqui hay {} miembros y tu eres {} del grupo.\n\nSupongo que quieres saber las cosas en las que puedo ayudarte por lo que aqui te dejo mi  <a href='https://telegra.ph/Firulais-Documentacion-05-27'>documentacion</a>. \n\ncontacta con el desarrollador @isael_diroche".format(
            self.user.first_name, get_members_count, get_members)
        buttons = [[
            bot.InlineKeyboardButton(text="contactar programador", callback_data="btn_contacto")
        ]]

        self.context.bot.sendMessage(chat_id=self.chat.id, text="🤖")
        self.context.bot.sendMessage(chat_id=self.chat.id,
                                     text=mensaje_start,
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=InlineKeyboardMarkup(buttons))

        self.context.bot.setMyCommands(comandos)

    def archivar_documento(self):
        self.context.bot.copy_message(chat_id=-1001601095301,
                                      from_chat_id=self.chat.id,
                                      message_id=self.message.message_id,
                                      parse_mode=ParseMode.HTML,
                                      disable_notification=False,
                                      caption="<b>Titulo:</b>\n{}\n\n<b>Enviado por:</b>\n#{}\n".format(str(self.message.document.file_name).replace(".pdf", ""), self.user.first_name))

# ------------------------------------------------------------------------------------

def comando_start(update: Update, context: CallbackContext) -> None:
    especial = ComandosEspeciales(update, context)
    especial.start_command()

def comando_help(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    user = update.effective_user
    context.bot.sendMessage(chat_id=chat.id,
                            text=f"Hola {user.first_name}, si quieres  <b>ayuda</b> puedes revisar en la  <a href='https://telegra.ph/Firulais-Documentacion-05-27'>documentacion </a> o si lo que quieres es <b>reportar</b> un problema hacer un /reporte",
                            parse_mode=ParseMode.HTML)


def comando_menu(update: Update, context: CallbackContext) -> None:
    context.bot.sendMessage(chat_id=update.message.chat_id, text="MENU")


def comando_contacto(update: Update, context: CallbackContext) -> None:
    especial = ComandosEspeciales(update, context)
    especial.enviar_contacto(card=vcard)


def comando_voice(update: Update, context: CallbackContext) -> None:
    message = update.message
    funcion = Funciones(update, context)
    funcion.comando_voice(message)


def comando_rename(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message

    file_id, file_name, filename = range(3)

    try:
        file_id = message.reply_to_message.document.file_id
    except:
        pass

    new_name = str(message.text).replace("/rename ", "")
    var = context.bot.get_file(file_id)

    filename = f"comandos/media/documents/{new_name}.pdf"
    var.download(custom_path=f"{filename}")

    context.bot.sendChatAction(chat_id=chat.id, action="upload_document")
    context.bot.sendDocument(chat_id=chat.id,
                             caption=f"renombrado por {user.first_name} a {new_name}",
                             document=open(filename, 'rb'))
    os.remove(path=filename)


def comando_text_extract(update: Update, context: CallbackContext) -> None:
    context.bot.sendMessage(chat_id=update.message.chat_id, text="TEXT EXTRACT")


def comando_to_text(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message

    try:
        msg = message.reply_to_message.text
    except:
        msg = str(update.message.text)
        msg = msg.replace("/text ", "")

    try:
        try:
            with open(f"comandos/media/documents/archivo_{str(user.first_name).lower()}.txt", "w+") as texto:
                texto.write(msg)
                texto.close()

        except FileExistsError:
            with open(f"comandos/media/documents/archivo_{user.first_name}.txt", "w+") as texto:
                texto.write(msg)
                texto.close()

        context.bot.sendDocument(chat_id=chat.id,
                                 document=open(f"comandos/media/documents/archivo_{user.first_name}.txt", "rb"))

    except IndexError:
        context.bot.sendMessage(chat_id=chat.id,
                                text="Debe responder a un mensaje con este comando o  escribir el texto junto al comando.")


def comando_translate(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message

    mensaje = str(message).split()
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
        context.bot.sendMessage(chat_id=chat.id, parse_mode=ParseMode.HTML,
                                text=f'<u>aqui esta tu traduccion {user.first_name} (español) </u>\n\n<pre>{traduccion.text}</pre>')

    elif info.src == 'es':
        traduccion = translator.translate(msg, dest='en')
        context.bot.sendMessage(chat_id=chat.id, parse_mode=ParseMode.HTML,
                                text=f"<u>here's your traduction {user.first_name} (inglish) </u>\n\n<pre>{traduccion.text}</pre>")
    else:
        context.bot.sendMessage(chat_id=chat.id, text=f'No puedo traducir {msg}, lo siento 😢')

    return ConversationHandler.END


def comando_buscar(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    # user = update.effective_user
    message = update.effective_message

    msg = str(message.text).lower()
    mensaje = msg.split()

    if mensaje[0] == "/busca":
        msg = msg.replace("/busca", "")
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


def comando_file(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    message = update.effective_message

    try:
        # En caso de ser una imagen
        file_id = message.reply_to_message.photo[0].file_id
    except:
        # En caso de ser un documento
        file_id = message.reply_to_message.document.file_id

    var = context.bot.get_file(file_id)
    context.bot.sendMessage(chat_id=chat.id, parse_mode=ParseMode.HTML, text=f"<b>file id:</b>\n{file_id}\n\n<b>file path:</b>\n{var.file_path}")


def comando_reporte(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message

    message = str(message.text).replace("/reporte", "")

    context.bot.sendMessage(chat_id=chat.id, text="Reporte enviado")
    context.bot.sendMessage(chat_id=1641249828, parse_mode=ParseMode.HTML, text=f"<b>Nuevo reporte</b> \n\n<b>De:</b> {user.first_name}\n<b>Asunto:</b> {message}")


def all_messages(update: Update, context: CallbackContext) -> None:
    if bot.UPDATES:
        print(update)

# ------------------------------------------------------------------------------------
