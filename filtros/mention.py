# IMPORT MODULES
import filtros.ext.filtro


# YOUR CODE HERE

def filtro_mention(update, context):
    chat = update.message.chat
    user = update.message.from_user
    message = update.message

    text = str(message.text).lower().split()

    funcion = filtros.ext.filtro.Funciones(update, context, chat, user, message)

    for x in text:
        if x == "@isael_diroche":
            user_id = 1641249828
            funcion.alertar_usuario(user_id=user_id)

        elif x == "@brpolanco":
            user_id = 1484400775
            funcion.alertar_usuario(user_id=user_id)

        elif x == "@isael_automatize_bot":
            context.bot.sendMessage(chat_id=chat.id, text="Me acaban de mencionar a mi :V")

        else:
            pass