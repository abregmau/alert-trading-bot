import telebot
import os
import time

# Create bot

bot = telebot.TeleBot(token=os.environ['TOKEN'])
i=0

bot.send_message(353032690, 'Start!')

# Send message
while(True):
    text= 'Hi! I\'m a Bot! by Mauricio Abregú ' + str(i)
    bot.send_message(353032690, text)
    i+=1
    time.sleep(30)