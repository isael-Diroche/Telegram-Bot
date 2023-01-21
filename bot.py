# IMPORT MODULES

from telegram import CallbackQuery, Update, ParseMode, ChatAction, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler, CommandHandler, Updater, Dispatcher, Filters, CallbackQueryHandler, CallbackContext, MessageHandler

import datetime, time

from src.bot.commands.main import *
from src.conexion import *
from src.bot.filters.ext.mensajes import *
from src.bot.filters.main import *
from src.bot.buttons.main import *
from src.bot.commands.ext.conversation import *

# YOUR CODE HERE

# TOKEN = os.environ['TOKEN']
TOKEN = "1985333182:AAFKNzhBvBG6Gkp-uFx76021iqM7iqnRDo4"
#1865520485:AAGs-C7Buc0C3pUTry0HqA-DqKZt04fJBVE

TRADUCIR, BUSCAR= range(2)

UPDATES = True

def traduce_conversation(update, context):
    update.message.reply_text("Dime lo que quieres traducir")

    return TRADUCIR

def error(update, context):
    errores = context.error
    print(f"Update: {update} \nEl error es el siguiente:\n{errores}")

def main() -> None:
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # COMANDOS PRINCIPALES
    dp.add_handler(CommandHandler(command="start", callback=comando_start))
    dp.add_handler(CommandHandler(command="help", callback=comando_help))
    dp.add_handler(CommandHandler(command="menu", callback=comando_menu))
    dp.add_handler(CommandHandler(command="rename", callback=comando_rename))
    dp.add_handler(CommandHandler(command="text", callback=comando_to_text))
    dp.add_handler(CommandHandler(command="text_extract", callback=comando_text_extract))
    dp.add_handler(CommandHandler(command="voice", callback=comando_voice))
    dp.add_handler(CommandHandler(command="file", callback=comando_file))
    dp.add_handler(CommandHandler(command="reporte", callback=comando_reporte))

    # FILTROS PRINCIPALES
    dp.add_handler(MessageHandler(filters=Filters.entity("mention"), callback=filtro_mention))
    dp.add_handler(MessageHandler(filters=Filters.entity("hashtag"), callback=filtro_hashtag))

    # IMPORTANTE!
    # dp.add_handler(MessageHandler(filters=Filters.all, callback=all_messages))

    entry_points = [
        MessageHandler(filters=Filters.document.pdf or Filters.document.docx, callback=archivar_conversation),
        CommandHandler(command="busca", callback=busca_conversation),
        CommandHandler(command="traduce", callback=traduce_conversation),
        MessageHandler(filters=Filters.text, callback=mensajes),
        CallbackQueryHandler(pattern='btn_cerrar', callback=botones_eliminar),
        CallbackQueryHandler(pattern='btn_contacto', callback=comando_contacto),
    ]
    states = {
        TRADUCIR: [MessageHandler(Filters.text, comando_translate)],
        BUSCAR: [MessageHandler(Filters.text, comando_buscar)]
    }
    fallbacks = []

    dp.add_handler(ConversationHandler(entry_points=entry_points, states=states, fallbacks=fallbacks, per_message=False))
    updater.start_polling(0.1)
    print("Esto vivo!")
    updater.idle()

def migrate() -> None:
    # conexion = Conexion()

    try:  # PRIMERO traer todos los usuarios desde la nuve

        result = firebase.get('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/usuarios', '')

        nombre = []
        apellido = []
        lenguaje = []
        es_bot = []
        username = []
        user_id = []

        for key in result:
            nombre.append(result[key]['nombre'])
            apellido.append(result[key]['apellido'])
            lenguaje.append(result[key]['lenguaje'])
            es_bot.append(result[key]['es_bot'])
            username.append(result[key]['username'])
            user_id.append(result[key]['user_id'])

        insertar(longitud=len(nombre),
                 id_user=user_id,
                 languaje_code=lenguaje,
                 is_bot=es_bot,
                 user_name=username,
                 first_name=nombre,
                 last_name=apellido)

        print("Success!")
    except Exception as ex:
        print("No se pudieron migrar los datos de los usuarios debido al siguiente error ", ex)

    try:  # Segundo traer todas las materias desde la nube
        result_materias = firebase.get('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/materias', '')

        materia_id = []
        materia_nombre = []
        codigo = []
        image = []

        for key in result_materias:
            materia_id.append(result_materias[key]['id'])
            materia_nombre.append(result_materias[key]['nombre'])
            codigo.append(result_materias[key]['codigo'])
            image.append(result_materias[key]['image'])

        insertar_materia(longitud=len(materia_nombre),
                         id_materia=materia_id,
                         nombre=materia_nombre,
                         codigo=codigo,
                         image=image)

        print("Success!")
    except Exception as ex:
        print("no se pudieron migrar los registros de las materias", ex)

    try:  # TERCERO traer todas las tareas desde la nuve

        result_tareas = firebase.get('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/gestion_tareas', '')

        id_tarea = []
        titulo = []
        id_materia = []
        id_file = []
        id_usuario = []
        file_link = []
        id_unique = []

        for key in result_tareas:
            id_tarea.append(result_tareas[key]['id'])
            titulo.append(result_tareas[key]['titulo'])
            id_file.append(result_tareas[key]['fileid'])
            id_materia.append(result_tareas[key]['idMateria'])
            id_usuario.append(result_tareas[key]['idUsuario'])
            file_link.append(result_tareas[key]['fileLink'])
            id_unique.append(result_tareas[key]['idUnique'])

        insertar_tarea(longitud=len(titulo),
                       id_tarea=id_tarea,
                       titulo=titulo,
                       id_materia=id_materia,
                       id_file=id_file,
                       id_usuario=id_usuario,
                       filelink=file_link,
                       id_unique=id_unique)

        print("Success!")
    except Exception as ex:
        print("No se pudo realizar el registro de las tareas debido al siguiente error: ", ex)

    # Finalmente imprimir
    print("Los datos han sido migrados")

if __name__ == "__main__":
    migrate()
    main()
