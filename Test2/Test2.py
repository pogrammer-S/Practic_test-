import os
from dotenv import load_dotenv
import telebot

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message)

bot.polling()