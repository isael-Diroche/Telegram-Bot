# IMPORT MODULES

from bot import Update, CallbackContext, random, re
from src.bot.filters.questions import *
from bs4 import BeautifulSoup
import requests



# YOUR CODE HERE

def get_precio_dolar():
    respuesta = requests.get('https://www.google.com/finance/quote/USD-DOP?sa=X&ved=2ahUKEwih-Pibm6z-AhVbQzABHeeiBXwQmY0JegQIBRAc')
    soup = BeautifulSoup(respuesta.text, "html.parser")
    precio = soup.find('div', class_='kf1m0').text
    return precio

def messages(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    message = update.effective_message
    chat = update.effective_chat

    text = str(message.text).lower() 
    msg = text.split()

    for x in msg:
        if x == "bot":

            for y in msg:
                if y == "hola":
                    context.bot.sendMessage(chat_id = chat.id, 
                                            text = f"Hola {user.first_name}")
                
                if y == "precio":
                    for z in msg:
                        if z == "dolar":
                            precio = get_precio_dolar()
                            context.bot.sendMessage(chat_id = chat.id, 
                                                    text = f"El precio del dolar equivale a {precio} pesos dominicanos")

            def get_response(user_input):
                split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input)
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

            context.bot.sendMessage(chat_id=chat.id, text=f"{get_response(message.text)}")
        else:
            pass

    
    print(f"from: {user.first_name}\n msg: {text}\n{message.text}")