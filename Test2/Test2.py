import os
from dotenv import load_dotenv
import telebot

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.from_user.id, message.text)

bot.polling()