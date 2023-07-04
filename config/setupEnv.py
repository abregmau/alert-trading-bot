import configparser
import os
import logging


class botConfig:
    def __init__(self, cfg_name):
        
        # Init config
        CFG_FL_NAME = cfg_name
        USER_CFG_SECTION = "GENERAL_USER_CONFIG"
        config = configparser.ConfigParser()

        if not os.path.exists(CFG_FL_NAME):
            print("No configuration file (user.cfg) found! See README. Assuming environment variables...")

            # Config from environment variables
            config[USER_CFG_SECTION] = {
                "DEBUG": os.environ['DEBUG'],
                "ENVIRONMENT": os.environ['ENVIRONMENT'],
                "TELEBOT_KEY_PROD": os.environ['TELEBOT_KEY_PROD'],
                "TELEBOT_CHANNEL_PROD": os.environ['TELEBOT_CHANNEL_PROD'],
                "BINANCE_KEY_PROD": os.environ['BINANCE_KEY_PROD'],
                "BINANCE_SECRET_PROD": os.environ['BINANCE_SECRET_PROD'],
                "BINANCE_FUTURE_KEY_PROD": os.environ['BINANCE_FUTURE_KEY_PROD'],
                "BINANCE_FUTURE_SECRET_PROD": os.environ['BINANCE_FUTURE_SECRET_PROD'],
                "TELEBOT_KEY_DEV": os.environ['TELEBOT_KEY_DEV'],
                "TELEBOT_CHANNEL_DEV": os.environ['TELEBOT_CHANNEL_DEV'],
                "BINANCE_KEY_DEV": os.environ['BINANCE_KEY_DEV'],
                "BINANCE_SECRET_DEV": os.environ['BINANCE_SECRET_DEV'],
                "BINANCE_FUTURE_KEY_DEV": os.environ['BINANCE_FUTURE_KEY_DEV'],
                "BINANCE_FUTURE_SECRET_DEV": os.environ['BINANCE_FUTURE_SECRET_DEV'],
            }
        else:
            config.read(CFG_FL_NAME)

        self.environment = config.get(USER_CFG_SECTION, "ENVIRONMENT")
        loggingLevel = config.get(USER_CFG_SECTION, "LOGGING_LEVEL")
        if loggingLevel == "DEBUG":
            self.loggingLevel = logging.DEBUG
        elif loggingLevel == "INFO":
            self.loggingLevel = logging.INFO
        elif loggingLevel == "WARNING":
            self.loggingLevel = logging.WARNING
        elif loggingLevel == "ERROR":
            self.loggingLevel = logging.ERROR
        elif loggingLevel == "CRITICAL":
            self.loggingLevel = logging.CRITICAL
        else:
            self.loggingLevel == logging.WARNING

        if self.environment == "PRODUCTION":
            self.telebotKey = config.get(USER_CFG_SECTION, "TELEBOT_KEY_PROD")
            self.telebotChannel = config.get(USER_CFG_SECTION, "TELEBOT_CHANNEL_PROD")
            self.binanceSpotKey = config.get(USER_CFG_SECTION, "BINANCE_KEY_PROD")
            self.binanceSpotSecret = config.get(USER_CFG_SECTION, "BINANCE_SECRET_PROD")
            self.binanceFutureKey = config.get(USER_CFG_SECTION, "BINANCE_FUTURE_KEY_PROD")
            self.binanceFutureSecret = config.get(USER_CFG_SECTION, "BINANCE_FUTURE_SECRET_PROD")
        elif self.environment == "DEVELOPMENT":
            self.telebotKey = config.get(USER_CFG_SECTION, "TELEBOT_KEY_DEV")
            self.telebotChannel = config.get(USER_CFG_SECTION, "TELEBOT_CHANNEL_DEV")
            self.binanceSpotKey = config.get(USER_CFG_SECTION, "BINANCE_KEY_DEV")
            self.binanceSpotSecret = config.get(USER_CFG_SECTION, "BINANCE_SECRET_DEV")
            self.binanceFutureKey = config.get(USER_CFG_SECTION, "BINANCE_FUTURE_KEY_DEV")
            self.binanceFutureSecret = config.get(USER_CFG_SECTION, "BINANCE_FUTURE_SECRET_DEV")
        else:
            print("No environment configuration detected. Exiting...")
            exit()

        self.telegramUserId = config.get(USER_CFG_SECTION, "TELEGRAM_USER_ID")
        self.telegramUserHash = config.get(USER_CFG_SECTION, "TELEGRAM_USER_HASH")