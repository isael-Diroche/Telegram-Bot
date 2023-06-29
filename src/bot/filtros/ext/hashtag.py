from bot import *

# YOUR CODE HERE


def get_random_chiste():
    response = requests.get('http://www.todo-chistes.com/chistes-al-azar')
    soup = BeautifulSoup(response.text, "html.parser")
    chiste = soup.find("div", "field-chiste").text
    return chiste


def filter_hashtag(update: Update, context: CallbackContext) -> None:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message

    msg = message.text

    for x in msg.split():
        if x == "#chiste":
            chiste = get_random_chiste()
            context.bot.sendMessage(chat_id=update.effective_chat.id,
                            text=chiste)
        else:
            pass


    print(f"esto es un hashtag {msg}")

