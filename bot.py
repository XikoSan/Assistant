
import openai
import telebot
from config import BOT_TOKEN, OPENAI_APY_KEY

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_APY_KEY


# Greetings
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
                     "Hello, I`m your basic assistant. Can i help you?")


# Processing text message
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = generate_gpt_response(message.text)
    bot.send_message(message.chat.id, response)


# Function generate GPT response
def generate_gpt_response(user_input):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150,
            n=1,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,
                 f"Hi, You said: {message.text}")


# Started bot
if __name__ == '__main__':
    bot.polling(non_stop=True)
