import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
# from course import get_course
token = "vk1.a.GobUsG4Ifgb5kST13SEhApMDV5kcJgYajCqaARUkdBOiN7e8SB9Q0BBJroH9c5974vACrb2LqONrrpLK51EXzJKpBqPMxYm_6nfFMjEWgNnNRutcZS7u1RNe--DdwVEoEK0k_yvVfZ5kwolHa7VwW99Ayo3G_YPrDMhN7286-my5qs8OBq7iDyTUYhW1NbdIGcSKABeyuUJH3Bueh8triQ"
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)



for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text
        user_id = event.user_id
        msg_id = event.message_id
        if msg.lower() == "привет":
            vk.messages.send(user_id=user_id, random_id=msg_id,message="Привет,не рад тебя видеть")
        # elif msg.lower() == "-k":
        #     response = f"{get_course("R01235")} pублей за 1 доллар\n" \
        #                f"{get_course("R01239")} pублей за 1 евро\n" \
        #                f"{get_course("R01375")} pублей за 1 юаней\n"
        #     vk.messages.send(user_id=user_id, random_id=msg_id,message= response)
        else:
            vk.messages.send(user_id=user_id, random_id=msg_id,message="Да пошёл ты...")


