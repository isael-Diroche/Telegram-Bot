# Dependencias necesarias desde el script principal
from bot import Update, CallbackContext 

# Codigo aqui

def command(update:Update, context:CallbackContext) -> None:
    vcard = """BEGIN:VCARD
                VERSION:3.0
                ORG:Instituto Tecnologico de las americas
                TITLE:Estudiante
                TEL;TYPE=WORK,VOICE:+1(809)678-1819
                ADR;TYPE=WORK,PREF:;;Villa Altagracia;Santo Domingo;Republica Domnicana
                BDAY:6 Septiembre 2002
                EMAIL;PREF=1:isaeldiroche00@gmail.com
                NOTE:Contactame para mas información
                END:VCARD"""
    
    context.bot.sendContact(chat_id=update.effective_chat.id,
                            phone_number="+18096781819",
                            first_name="Isael",
                            last_name="Diroche",
                            vcard=vcard,
                            disable_notification=False)