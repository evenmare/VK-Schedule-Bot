import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from private import token as token

class MyVkBotLongPoll(VkLongPoll):
    def listen(self):
        while True:
            try:
                for event in self.check():
                    yield event
            except Exception as e:
                print('Longpoll Error (VK):', e)

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = MyVkBotLongPoll(vk)