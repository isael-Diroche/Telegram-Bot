# IMPORT MODULES

from bot import *

# YOUR CODE HERE

def messages(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    message = update.effective_message
    text = str(message.text).lower()
    
    print(f"from: {user.first_name}\n msg: {text}")