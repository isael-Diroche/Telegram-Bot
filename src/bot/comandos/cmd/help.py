from bot import Update, CallbackContext, ParseMode


def command(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_name = update.effective_user.first_name
    msg = """Hola {} te voy a mostrar los comandos que poseo.\n\n/start\n/help\n\nPor ahora esos son todos si necesitas mas informacion acerca de puedes consultar la <a href="https://telegra.ph/Firulais-Documentacion-05-27">documentacion</a> del las funcionalidades. Tambien puedes reportar algun error en el bot o mejora en los <a href="https://github.com/isael-Diroche/TeleHelpBot/issues">issues</a> del repositorio de TeleHelpBot""".format(user_name)

    context.bot.sendMessage(chat_id = chat_id, text = msg, parse_mode = ParseMode.HTML)