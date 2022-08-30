import telegram

TOKEN = "1404105180:AAEy2gTOA5T8xGhW83gkKO229ZNUqow1m10"
CHAT_ID = 644126558
GROUP_CHAT_ID = -750162787

def send_grocery_list(groceries):
    bot = telegram.Bot(TOKEN)
    bot.send_message(text = groceries, chat_id = GROUP_CHAT_ID)
 