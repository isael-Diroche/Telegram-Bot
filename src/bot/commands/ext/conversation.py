# IMPORT MODULES

import bot
import src.bot.commands.main
from bot import *
from src.bot.commands.main import *
from src.conexion import *

# YOUR CODE HERE

def verificar_tareas():  # Con esta funcion retornamos los unique_id de las tareas en la base de datos
    result = firebase.get('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/gestion_tareas', '')

    ids = []
    for key in result:
        ids.append(result[key]['idUnique'])

    return ids

def traduce_conversation(update, context):
    chat = update.message.chat
    message = update.message

    context.bot.sendMessage(chat_id=chat.id, text="Dime lo que quieres traducir", reply_to_message_id=message.message_id)

    return bot.TRADUCIR

def busca_conversation(update, context):
    chat = update.effective_chat
    message = update.effective_message

    context.bot.sendMessage(chat_id=chat.id, text="Que quieres que busque por ti en Wikipedia?", reply_to_message_id=message.message_id)

    return bot.BUSCAR

def archivar_conversation(update, context):

    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user

    file_id = message.document.file_id
    var = context.bot.get_file(file_id)

    datos = {
        'id': 'null',
        'titulo': f'{message.document.file_name}',
        'idUsuario': f'{user.id}',
        'idMateria': 'null',
        'fileid': f'{file_id}',
        'fileLink': f'{var.file_path}',
        'idUnique': f'{message.document.file_unique_id}'
    }
    idunique = verificar_tareas()

    if datos['idUnique'] not in idunique:

        try:
            registrar_tarea_firebase(datos=datos)
            especial = src.bot.commands.main.ComandosEspeciales(update, context)
            especial.archivar_documento()
        except:
            print("no se pudieron guardar")


    else:
        print("Ya esta esta tarea")
        pass
