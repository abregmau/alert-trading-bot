# Libraries for Telegram
from telethon import TelegramClient, events
from telegram import denmarkSignal

# Libraries for Binance
from modules import binanceFunctions
from modules import binanceClases


# General Libraries
import pickle
import logging
import asyncio
import threading
from queue import Queue
from binance.client import Client
from config import setupEnv

# Reading configuration variables
cfg_name = "./config/user.cfg"
confBot = setupEnv.botConfig(cfg_name)

# Configure logging
logging.basicConfig(format='[ %(asctime)s ]  %(message)s', filename='logBot.log', encoding='utf-8', level=confBot.loggingLevel)

# Configure Telegram
clientTelegramUser = TelegramClient('session', confBot.telegramUserId, confBot.telegramUserHash)

# Configure Binance
clientBinance = Client(confBot.binanceFutureKey, confBot.binanceFutureSecret, testnet=(not confBot.environment == "PRODUCTION"))

# Define funtions

@clientTelegramUser.on(events.NewMessage(chats=-771853770))
#@clientTelegramUser.on(events.NewMessage(chats=-1794357158))
async def my_event_handler(event):
    signal = denmarkSignal.readMessage(event.message)

    # Put the signal into the shared queue
    if(denmarkSignal.validateSignal(signal)):
        logging.debug(signal)
        signal_queue.put(signal)

def run_binance_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    listSignals = binanceClases.listSignals()
    
    async def signal_task():
        while True:
            if not signal_queue.empty():
                signal = signal_queue.get()
                logging.debug("Signal retrieve from queue")
                
                newSignal = binanceClases.signal(signal)
                listSignals.appendSignal(newSignal)
            
            listSignals.checkListStatus(clientBinance)
        
    loop.run_until_complete(signal_task())

# Shared queue for the signals
signal_queue = Queue()

# Start the price retrieval thread
binanceThread = threading.Thread(target=run_binance_thread, args=())
binanceThread.start()

# Start Telegram thread
clientTelegramUser.start()
clientTelegramUser.run_until_disconnected()