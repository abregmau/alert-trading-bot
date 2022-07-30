import configparser
import os

CFG_FL_NAME = "user.cfg"
USER_CFG_SECTION = "telegramBot_user_config"

class botConfig:
    def __init__(self):
        # Init config
        config = configparser.ConfigParser()
        config["DEFAULT"] = {
            "token": "XXXXXXXXXXXXXXXXXXXXX",
        }

        if not os.path.exists(CFG_FL_NAME):
            print("No configuration file (user.cfg) found! See README. Assuming default config...")
            config[USER_CFG_SECTION] = {}
        else:
            config.read(CFG_FL_NAME)

        # Token to access the HTTP API
        self.TOKEN = config.get(USER_CFG_SECTION, "token")