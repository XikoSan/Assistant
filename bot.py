
from openai import OpenAI
import telebot
from config import BOT_TOKEN, OPENAI_APY_KEY

bot = telebot.TeleBot(BOT_TOKEN)
client = OpenAI(api_key=OPENAI_APY_KEY)


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
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"


# Started bot
if __name__ == '__main__':
    bot.polling(non_stop=True)
