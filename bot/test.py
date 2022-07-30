import telebot
import os

# Create bot

bot = telebot.TeleBot(token=os.environ['TOKEN'])

# Send message
bot.send_message(353032690, 'Hi! I\'m a Bot! by Mauricio Abregú')