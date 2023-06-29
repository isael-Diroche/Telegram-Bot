from bot import Update, CallbackContext, ParseMode, Translator

translator = Translator()


class Funcion():
    
    def __init__(self, update, context) -> None:
        self.update = update
        self.context = context

    @staticmethod
    def get_start_message(update, context):
        user_name = update.effective_user.first_name
        user_id = update.effective_user.id
        get_members = context.bot.get_chat_member(update.effective_chat.id, user_id)
        puesto = translator.translate(str(get_members.status), dest="es").text
        get_members = puesto 
        get_members_count = context.bot.get_chat_members_count(update.effective_chat.id)

        msg = "Hola {}({}) gracias por activarme, por lo que veo aqui hay {} usuarios. Si necesitas ayuda en algo no dudes en consultarme, si quieres saber lo que puedo hacer puedes usar el comando /help o darle un vistazo a la <a href='https://telegra.ph/Firulais-Documentacion-05-27'>documentacion</a> por @IsaelDiroche".format(user_name, get_members, get_members_count)
        return msg 

def command(update: Update, context: CallbackContext):
    funcion = Funcion(update, context)

    chat_id = update.effective_chat.id
    cb = context.bot
    msg = funcion.get_start_message(update, context)

    comandos = [
        ("/start", "Inicio del bot"),
        ("/help", "Pedir ayuda al bot"),]

    cb.setMyCommands(comandos)
    cb.sendMessage( chat_id = chat_id,
                    text = "msg",
                    parse_mode = ParseMode.HTML)
