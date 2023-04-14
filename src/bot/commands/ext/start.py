# Dependencias necesarias desde el script principal
from bot import Update, CallbackContext, ParseMode

# Codigo aqui

'''def start_command(self):
        get_members = self.context.bot.get_chat_member(chat_id=self.chat.id, user_id=self.user.id)
        puesto = translator.translate(str(get_members.status), dest="es").text
        get_members = puesto
        print(f"{get_members}")
        get_members_count = self.context.bot.get_chat_members_count(self.chat.id)

        comandos = [
            ("/start", "Inicio del bot"),
            
            ("/menu", "Abrir un menu"),
            ("/busqueda", "Buscar informacion en la web"),
            ("/traduce", "Traducir algun texto ingles/español"),
            ("/text", "Convierte texto en un archivo .txt"),
            ("/file", "Devuelve el link de un archivo"),
            ("/rename", "Cambia el nombre de un archivo (PDF only)"),
            
        ]
        mensaje_start = "Hola {} gracias por activarme,\npor lo que veo aqui hay {} miembros y tu eres {} del grupo.\n\nSupongo que quieres saber las cosas en las que puedo ayudarte por lo que aqui te dejo mi  <a href='https://telegra.ph/Firulais-Documentacion-05-27'>documentacion</a>. \n\ncontacta con el desarrollador @IsaelDiroche".format(
            self.user.first_name, get_members_count, get_members)
        buttons = [[
            bot.InlineKeyboardButton(text="contactar programador", callback_data="btn_contacto")
        ]]

        self.context.bot.sendMessage(chat_id=self.chat.id, text="🤖")
        self.context.bot.sendMessage(chat_id=self.chat.id,
                                     text=mensaje_start,
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=InlineKeyboardMarkup(buttons))

        self.context.bot.setMyCommands(comandos)
'''

def command(update, context) -> None:
    comandos = [
        ("/start", "Inicio del bot"),
        ("/help", "Pedir ayuda al bot"),
        ("/reporte", "Reportar algun cambio o mejora"),

    ]

    msg = "Hola fulano gracias por activarme,\npor lo que veo aqui hay que se yo cuantos miembros y tu eres aguien nose del grupo.\n\nSupongo que quieres saber las cosas en las que puedo ayudarte por lo que aqui te dejo mi  <a href='https://telegra.ph/Firulais-Documentacion-05-27'>documentacion</a>. \n\ncontacta con el desarrollador @IsaelDiroche"
    context.bot.sendMessage(chat_id = update.effective_chat.id,
                            text = msg,
                            parse_mode=ParseMode.HTML)