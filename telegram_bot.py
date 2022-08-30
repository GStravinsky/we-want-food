import telegram

TOKEN = ""
CHAT_ID = 0
GROUP_CHAT_ID = 0

def send_grocery_list(groceries):
    bot = telegram.Bot(TOKEN)
    bot.send_message(text = groceries, chat_id = GROUP_CHAT_ID)
 