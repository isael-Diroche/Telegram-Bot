from bot import Update, CallbackContext, ParseMode


def command(update: Update, context: CallbackContext) -> None:
    nombre = update.effective_user.first_name
    mensaje = update.effective_message.text

    msg = "Gracias por notificar eso <b>{}</b>, mi programador isael tratara de corregirlo lo mas proto posible porque no tiene mas nada que hacer que hacerle caso a tu pendeja de reporte".format(nombre)

    # Mensaje para el usuario que escriba el reporte
    context.bot.sendMessage(chat_id = update.effective_chat.id,
                            text = msg,
                            parse_mode=ParseMode.HTML)
    
    reporte = update.effective_message.text
    reporte_msg = reporte.replace("/reporte ", "")

    # Mensaje para el admin que recibira el reporte
    context.bot.sendMessage(chat_id = 1641249828,
                            text = "Tienes un nuevo reporte \n{} dice: {}".format(nombre, reporte_msg))