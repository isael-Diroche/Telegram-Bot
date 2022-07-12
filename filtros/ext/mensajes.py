# IMPORT MODULES
from bot import *
import filtros.ext.filtro

# YOUR CODE HERE
grupo_id = [-1001705096084, -1001795333102, -1001147710430, -1001346444711]

def active_user():  # Con esta funcion retornamos los id_user de los usuarios que se encuentren en la base de datos
    # firebase = firebase.FirebaseApplication("https://pythonbdtest-50a94-default-rtdb.firebaseio.com/", None)
    result = firebase.get('https://pythonbdtest-50a94-default-rtdb.firebaseio.com/usuarios', '')

    ids = []
    for key in result:
        ids.append(result[key]['user_id'])

    return ids

def mensaje_entrada(update, context) -> None:
    user = update.effective_user
    chat = update.effective_chat
    message = update.effective_message

    if int(chat.id) not in grupo_id:
        context.bot.sendMessage(chat_id=chat.id, text="Quien me metio en esta mielda de grupo")
        time.sleep(2)
        context.bot.sendMessage(chat_id=chat.id, text="me voy de aqui cñ")
        time.sleep(1)
        context.bot.leave_chat(chat_id=chat.id)
    else:
        pass
    mensaje = f'Hola {user.first_name} bienvenido al Grupo de Software 😁. Es un gusto que estés con nosotros así que dejame invitarte a ser parte de nuestra comunidad.'

    Buttons = [[
        InlineKeyboardButton("Telegram Chanel", url="https://t.me/+qWbRKtnAYnwwOTMx")
    ], [
        InlineKeyboardButton("Discord server", url="https://discord.gg/CVqutUFey3")
    ], [
        InlineKeyboardButton("Figma team", url="https://www.figma.com/team_invite/redeem/0OER3J4ypKHBiLjV1ZcZUr")
    ], [
        InlineKeyboardButton("Github Organization", url="https://github.com/GrupoSofware")
    ]]

    context.bot.sendMessage(
        chat_id=chat.id,
        text=mensaje,
        reply_markup=InlineKeyboardMarkup(Buttons)
    )

def mensaje_salida(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    chat = update.effective_chat
    message = update.effective_message

    get_members_count = context.bot.get_chat_members_count(chat_id=chat.id)

    context.bot.sendMessage(chat_id=chat.id, text=f'Uno menos, mas espacio\n ahora solo somos {get_members_count}')

def borrar_mensaje(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    chat = update.effective_chat
    message = update.effective_message

    is_bot_can_delete = context.bot.get_me()
    print(is_bot_can_delete)
    try:
        context.bot.delete_message(chat_id=chat.id, message_id=update.message.message_id)
        context.bot.sendMessage(chat_id=chat.id, text="Sin malaspalabras {} sea respetuoso 😟".format(user.first_name))
    except:
        context.bot.sendMessage(chat_id=chat.id, text="No soy admin, por eso no te borro eso")

def mensajes(update: Update, context: CallbackContext) -> None:
    usuarios = active_user()
    user = update.effective_user
    chat = update.effective_chat
    message = update.effective_message

    id_usuario = user.id
    text = str(message.text).lower()
    funcion = filtros.ext.filtro.Funciones(update, context, chat, user, message)

    if id_usuario not in usuarios:
       print("El usuario requiere ser registrado\n", user)
       registrar_usuario_firebase(datos=user)

    else:
        print("Si esta!")

    msg = text.split()
    for x in msg:
        if x == "#":
            context.bot.sendMessage(chat_id=chat.id, text="Aqui una lista de los # que puedes utilizar")

        elif x == "hola":
            context.bot.sendMessage(chat_id=chat.id, text=f"Hola {user.first_name}")

        elif x == "adios":
            context.bot.sendMessage(chat_id=chat.id, text=f"Adios {user.first_name}")

        elif x == "isael":
            user_id = 1641249828
            funcion.alertar_usuario(user_id)

        elif x == "bryan":
            user_id = 1484400775
            funcion.alertar_usuario(user_id)

        elif x == 'bot':
            for y in msg:
                if y == 'hora':
                    funcion.recibir_hora()

                elif y == 'broma':
                    funcion.recibir_broma()

                elif y == 'chiste':
                    funcion.recibir_chiste()

                elif y == 'horario':

                    for z in msg:

                        if z == "isael":
                            funcion.recibir_imagen("horario")

                        elif z == "bryan":
                            funcion.recibir_imagen("horario-bryan")

                        elif z == "kelvyn":
                            funcion.recibir_imagen("horario-kelvyn")

                        else:
                            pass

                elif y == 'pensum':
                    funcion.recibir_imagen("pensum")

                elif y == 'traduce':
                    update.message.reply_text("Dime que quieres que traduzca?")
                    return bot.TRADUCIR

        else:
            pass

    print(f"message: {user.first_name} - {text}")
