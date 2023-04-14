from bot import Update, CallbackContext, ParseMode


def command(update: Update, context: CallbackContext) -> None:
    nombre = update.effective_user.first_name
    #apellido = update.effective_user.last_name

    msg = "Hola <b>{}</b>, si necesitas ayuda con el uso de algunos comandos puedes consultar en la documentacion del bot <a href='https://telegra.ph/Firulais-Documentacion-05-27'>documentacion</a>".format(nombre)

    context.bot.sendMessage(chat_id = update.effective_chat.id,
                            text = msg,
                            parse_mode = ParseMode.HTML)