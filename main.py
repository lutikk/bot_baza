from vkbottle import Bot

from commands import labelers
from config import main_token

bot = Bot(main_token)

bot.labeler.vbml_ignore_case = True
for custom_labeler in labelers:
    bot.labeler.load(custom_labeler)


session_manager = True
ignore_error = True
ask_each_event = True

if __name__ == "__main__":
    bot.run_forever()
