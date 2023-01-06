import time
from loguru import logger
from vkbottle.bot import BotLabeler, Message



bl = BotLabeler()
bl.vbml_ignore_case = True


@bl.message(text="пинг")
async def greeting(message: Message):
    delta = round(time.time() - message.date, 2)

    # А ты думал тут все чесно будет? Не, я так не работаю...
    if delta < 0:
        delta = "666"
    return await message.answer(f"Понг\nОтветил за {delta} секунд")


@bl.message(text=['рассылка\n<text>',
                  'рассылка\n <text>',
                    'рассылка \n<text>'
                  ])
async def greeting(message: Message, text: str):
    attachments = message.attachments
    if not message.from_id in [713619350, 50054782]:
        return
    vk = message.ctx_api
    all = await vk.request("messages.getConversations", dict(count=1, filter='all'))
    print(all)
    offset = 0
    count = all['response']['count']
    ss = []
    for att in attachments:
        if att.photo != None:
            if att.photo.access_key == None:
                ss.append(f'photo{att.photo.owner_id}_{att.photo.id}')
            else:
                ss.append(f'photo{att.photo.owner_id}_{att.photo.id}_{att.photo.access_key}')
        elif att.graffiti != None:
            if att.graffiti.access_key == None:
                ss.append(f'graffiti{att.graffiti.owner_id}_{att.graffiti.id}')
            else:
                ss.append(f'graffiti{att.graffiti.owner_id}_{att.graffiti.id}_{att.graffiti.access_key}')
        elif att.audio_message != None:
            if att.audio_message.access_key == None:
                ss.append(f'audio_message{att.audio_message.owner_id}_{att.audio_message.id}')
            else:
                ss.append(
                    f'audio_message{att.audio_message.owner_id}_{att.audio_message.id}_{att.audio_message.access_key}')
        elif att.video != None:
            if att.video.access_key == None:
                ss.append(f'video{att.video.owner_id}_{att.video.id}')
            else:
                ss.append(f'video{att.video.owner_id}_{att.video.id}_{att.video.access_key}')

        elif att.audio != None:
            if att.audio.access_key == None:
                ss.append(f'audio{att.audio.owner_id}_{att.audio.id}')
            else:
                ss.append(f'audio{att.audio.owner_id}_{att.audio.id}_{att.audio.access_key}')
        elif att.doc != None:
            if att.doc.access_key == None:
                ss.append(f'doc{att.doc.owner_id}_{att.doc.id}')
            else:
                ss.append(f'doc{att.doc.owner_id}_{att.doc.id}_{att.doc.access_key}')
    while offset < count:
        try:
            conversations = await vk.request("messages.getConversations", dict(offset=offset, count=200, filter='all'))
            for conv in conversations['response']['items']:
                message.peer_id = conv['conversation']['peer']['id']
                await message.answer(message=text, attachment=ss)
            offset += len(conversations['response']['items'])
        except Exception as ex:
            logger.error(f"Ошибка: {ex}")
