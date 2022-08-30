import telegram
from constants import TOKEN, GROUP_CHAT_ID, CHAT_ID

def send_grocery_list(groceries):
    bot = telegram.Bot(TOKEN)
    bot.send_message(text = groceries, chat_id = GROUP_CHAT_ID)
 