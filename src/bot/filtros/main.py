from bot import Update, CallbackContext, hashtag, Traduce


def hashtag(update, context) -> None:
    message = str(update.effective_message.text).lower()
    reply = str(update.effective_message.reply_to_message.text)
    
    for x in message.split():
        if x == "#traduce":
            
            break
        
        elif x == "#mmg":
            print("mmg ute")
            
        else:
            pass
    