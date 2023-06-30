from bot import *
from .comandos.cmd.start import Start

class Comando:
    def __init__(self, update, context) -> None:
        self.start = Start(update, context)
        
    def start(self, update, context):
        res = self.start
        res.ge
        # context.bot.sendMessage(update.effective_chat.id, "hola")
    