import telebot
from config import setup_env

cfg_name = "./config/user.cfg"
confBot = setup_env.botConfig(cfg_name)

bot = telebot.TeleBot(confBot.telebotKey)

bot.send_message(353032690, 'Say Start Plis!')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "¿Me ha llamado maestro?")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

#bot.polling()
bot.infinity_polling(timeout=10, long_polling_timeout = 5)