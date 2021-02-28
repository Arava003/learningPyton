import vk_api
from vk_api.bot_longpoll import VkBotEventType
from vk_api.bot_longpoll import VkBotLongPoll
import random


vk_session = vk_api.VkApi(token="4aab3b82508a3249edf51657128dc5273ff18e239927280ed506584c01b36a9d47fd61c97dccf0df9e8bc")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "202933208")


def message_send_hi(text):
    vk.messages.send(
                peer_ids=event.object["peer_id"],
                random_id=random.random(),
                message=text
            )


for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.object["text"]:
            message_send_hi("Привет пользователь!")