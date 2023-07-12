# import vk_api
# import random 
# import requests 
# from vk_api.longpoll import VkLongPoll, VkEventType
# token = "vk1.a.GobUsG4Ifgb5kST13SEhApMDV5kcJgYajCqaARUkdBOiN7e8SB9Q0BBJroH9c5974vACrb2LqONrrpLK51EXzJKpBqPMxYm_6nfFMjEWgNnNRutcZS7u1RNe--DdwVEoEK0k_yvVfZ5kwolHa7VwW99Ayo3G_YPrDMhN7286-my5qs8OBq7iDyTUYhW1NbdIGcSKABeyuUJH3Bueh8triQ"
# vk_session = vk_api.VkApi(token=token) 
# vk = vk_session.get_api() 
# longpoll = VkLongPoll(vk_session)


# while True:
#     messages = vk_session.method("messages.getConversations", {"count": 20, "filter": "unanswered"})
#     if messages["count"] >= 1:
#         print(messages)
#         user_id = messages["items"][0]["last_message"]["from_id"]
#         message_id = messages["items"][0]["last_message"]["id"]
#         message_text = messages["items"][0]["last_message"]["text"]
#         if message_text.lower() == "привет":
#             vk_session.method("messages.send", {"peer_id": user_id, "random_id": message_id, "message": "Привет!Это если что пишет уже сам бот который пока что больше нихуя и не умеет"})
#         else:
#             vk_session.method("messages.send", {"peer_id": user_id, "random_id": message_id, "message": "не понял но наверное это очень интересно"})

    # def get_largest_planet(): 
    #     api_url = "https://swapi.dev/api/planets" 
    #     response = requests.get(api_url) 
    #     data = response.json() 
    #     largest = data["results"][0] 
    #     for planet in data["results"]: 
    #         if int(planet["diameter"]) > int(largest["diameter"]): 
    #             largest = planet 
    #     return largest["name"] 
 
    # for event in  longpoll.listen(): 
    #    if event.type == VkEventType.MESSAGE_NEW and event.to_me: 
    #         msg = event.text.lower() 
    #         user_id = event.user_id 
    #         random_id = random.randint(1,9999999) 
    #         if msg == "планеты": 
    #             response = f'Самая большая планета - {get_largest_planet()}' 
    #         else: 
    #             response = "Неизвестная команда. Вот что я умею: планеты: выдать планету с максимальным диаметром, корабли: выдавать корабль с максимальной скоростью" 
    #         vk.messages.send(peer_id = user_id, random_id = random_id, message=response)
    # def get_starships(): 
    #     response2 = requests.get("https://swapi.dev/api/starships/") 
    #     return response2.json()
    # def handle_message(message):
    #     if message == "корабли": 
    #         starships = get_starships()["results"] 
    #         fastest_starship = max(starships, key=lambda x: int(x["max_atmosphering_speed"])) 
    #         response = f'Максимальная скорость звездного корабля {fastest_starship["name"]} - {fastest_starship["max_atmosphering_speed"]} км/ч.' 
    #     else: 
    #         response = "Я не понимаю, что вы хотите." 
    #     return response 

