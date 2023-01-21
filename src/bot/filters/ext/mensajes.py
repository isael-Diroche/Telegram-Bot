# IMPORT MODULES
import re
import random
from src.bot.filters.questions import *
import src.bot.filters

from bot import *
import src.bot.filters.main

# YOUR CODE HERE
grupo_id = [-1001705096084]

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
    funcion = src.bot.filters.main.Funciones(update, context, chat, user, message)

    if id_usuario not in usuarios:
       print("El usuario requiere ser registrado\n", user)
       registrar_usuario_firebase(datos=user)

    else:
        print("Si esta!")

    msg = text.split()

    for x in msg:
        if x == "#":
            context.bot.sendMessage(chat_id=chat.id, text="Aqui una lista de los # que puedes utilizar")

        elif x == "bot":
            def get_response(user_input):
                split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
                response = check_all_messages(split_message)
                return response

            def message_probability(user_message, recognized_words, single_response= False, required_word=[]):
                message_certainty = 0
                has_required_words = True

                for word in user_message:
                    if word in recognized_words:
                        message_certainty += 1

                percentage = float(message_certainty) / float (len(recognized_words))

                for word in required_word:
                    if word not in user_message:
                        has_required_words = False
                        break
                if has_required_words or single_response:
                    return int(percentage * 100)
                else:
                    return 0

            def check_all_messages(message):
                    highest_prob = {}

                    def response(bot_response, list_of_words, single_response = False, required_words = []):
                        nonlocal highest_prob
                        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

                    response(saludos[random.randrange(3)], saludos_user, single_response = False)
                    response(carreras, carreras_user, single_response = True)
                    response(redes_sociales, redes_sociales_user, single_response = True,)
                    response(admision, admision_user, single_response = True)
                    response(info, info_user, single_response = True)
                    response(ubicacion, ubicacion_user, single_response = True)
                    response(valores, valores_user, single_response = True)
                    response(contacto, contacto_user, single_response = True)
                    response(transporte, transporte_user, single_response = True)
                    response(biblioteca, biblioteca_user, single_response = True)
                    response(residencia, residencia_user, single_response = True)

                    best_match = max(highest_prob, key=highest_prob.get)
                    #print(highest_prob)

                    return unknown() if highest_prob[best_match] < 1 else best_match

            def unknown():
                unknown = ['Puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'Búscalo en google a ver que tal', 'No te entiendo']
                
                response = unknown[random.randrange(3)]
                return response

            context.bot.sendMessage(chat_id=chat.id, text=f"{get_response(str(message.text))}")

    print(f"message: {user.first_name} - {text}")
