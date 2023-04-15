# IMPORT MODULES

from bot import Update, CallbackContext

# YOUR CODE HERE
class Filtrar:

    def __init__(self, update:Update, context:CallbackContext) -> None:
        self.update = update
        self.context = context

        self.chat = update.effective_chat
        self.user = update.effective_user
        self.message = update.effective_message

    def global_mention (self):
        self.context.bot.sendMessage(chat_id = self.chat.id, text="Global")

    def user_alert(self, user, from_user, from_group):
        map_user_id = {
            'isael': '1641249828',
            'bryan': '',
            'alex': '',
        }

        self.context.bot.sendMessage(chat_id=map_user_id[f'{user}'], text= f"Te acaba de mensionar un tal {from_user} en {from_group}")
    

