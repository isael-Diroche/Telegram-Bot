# IMPORT MODULES

from bot import Update, CallbackContext, Translator, ParseMode, ConversationHandler

# YOUR CODE HERE
translator = Translator()

vcard = """BEGIN:VCARD
VERSION:3.0
ORG:Instituto Tecnologico de las americas
TITLE:Estudiante
TEL;TYPE=WORK,VOICE:+1(809)678-1819
ADR;TYPE=WORK,PREF:;;Villa altagracia;Santo Domingo;Republica Domnicana
BDAY:6 Septiembre 2002
EMAIL;PREF=1:isaeldiroche00@gmail.com
NOTE:Contactame para mas información
END:VCARD"""

class Command:

    def __init__(self, update:Update, context:CallbackContext) -> None:
        self.update = update
        self.context = context

        self.chat = update.effective_chat
        self.user = update.effective_user
        self.message = update.effective_message



    def start(self):
        comandos = [
            ("/start", "Inicio del bot"),
            ("/help", "Pedir ayuda al bot"),
            ("/traducir", "Traducir algun texto ingles/español"),
            ("/report", "Reportar algun cambio o mejora"),
        ]

        msg = "Hola fulano gracias por activarme,\npor lo que veo aqui hay que se yo cuantos miembros y tu eres aguien nose del grupo.\n\nSupongo que quieres saber las cosas en las que puedo ayudarte por lo que aqui te dejo mi  <a href='https://telegra.ph/Firulais-Documentacion-05-27'>documentacion</a>. \n\ncontacta con el desarrollador @IsaelDiroche"
        self.context.bot.sendMessage(chat_id = self.chat.id,
                                    text = msg)

    def help(self):
        msg = "este es el comando de ayuda"
        self.context.bot.sendMessage(chat_id = self.chat.id,
                                    text = msg)

    def report(self):
        msg = "Reporte enviado! gracias por tu comentario {}".format(self.user.first_name)
        reporte_msg = (self.message.text).replace("/report ", "")
        report = "El usuario {} desde {} envio un reporte:\n{}".format(self.user.full_name, self.chat.title, reporte_msg)

        #Respondiendo al usuario que hace el reporte
        self.context.bot.sendMessage(chat_id = self.chat.id,
                                    text = msg)

        #Enviando el reporte al administrador principal del bot
        self.context.bot.sendMessage(chat_id = 1641249828,
                                    text = report)

    def traducir(self):
        mensaje = str(self.message.text).split()
        try:
            msg = str(self.message.reply_to_message.text).lower()
        except:
            msg = str(self.message.text).lower()

        if mensaje[0] == "/traduce":
            msg = msg.replace("/traduce", " ")
        elif mensaje[0] == "#traduce":
            msg = msg.replace("#traduce", " ")
        else:
            pass

        info = translator.translate(msg)
        if info.src == 'en':
            traduccion = translator.translate(text=msg, dest='es')
            self.context.bot.sendMessage(chat_id=self.chat.id, 
                                        parse_mode=ParseMode.HTML,
                                        text=f'<pre>{traduccion.text}</pre>')

        elif info.src == 'es':
            traduccion = translator.translate(msg, dest='en')
            self.context.bot.sendMessage(chat_id=self.chat.id,
                                        parse_mode=ParseMode.HTML,
                                        text=f"<pre>{traduccion.text}</pre>")
        else:
            self.context.bot.sendMessage(chat_id=self.chat.id, text=f'No puedo traducir {msg}, lo siento 😢')

        return ConversationHandler.END

    def voice(self):
        pass

    def contact(self, card):
        self.context.bot.sendContact(chat_id=self.chat.id,
                                     phone_number="+18096781819",
                                     first_name="Isael",
                                     last_name="Diroche",
                                     vcard=card,
                                     disable_notification=False)

def start_command(update: Update, context: CallbackContext) -> None:
    cm = Command(update, context)
    cm.start()

def help_command(update: Update, context: CallbackContext) -> None:
    cm = Command(update, context)
    cm.help()

def report_command(update: Update, context: CallbackContext) -> None:
    cm = Command(update, context)
    cm.report()

def traducir_command(update: Update, context: CallbackContext) -> None:
    cm = Command(update, context)
    cm.traducir()

def voice_command(update: Update, context: CallbackContext) -> None:
    cm = Command(update, context)
    #no hace nada

def contact_command(update: Update, context: CallbackContext) -> None:
    cm = Command(update, context)
    cm.contact(card=vcard)