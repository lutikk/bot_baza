import time

from vkbottle.bot import BotLabeler, Message



bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message()
async def greeting(message: Message):
    text = 'Извините я не понял вопроса\n' \
           'Для того что-бы узнать мой список команд напишите "Помощь"\n' \
           'Если остались вопросы то обращайтесь по телефону:\n' \
           '89221888888'
    return text