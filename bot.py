
import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


# Greetings
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
                     "Hello, I`m your basic assistant. Can i help you?")


# Started bot
if __name__ == '__main__':
    bot.infinity_polling()
