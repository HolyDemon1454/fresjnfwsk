# import requests

# url = "https://swapi.dev/api/"

# response = requests.get(url)
# responseJson = response.json()


# starships_api = responseJson.get('starships')
# people_api = responseJson.get("people") #ссылка на ip с информацией о всех персонажей
# planets_api = responseJson.get("planets")

# def check_starships(url):
#     for i in range(1, 6):
#         response = requests.get(url + "/" + str(i)).json()
#         print(response.get("name"),response.get("max_atmosphering_speed"))

# def check_people(url):
#     for i in range(1, 6):
#         response = requests.get(url + "/" + str(i)).json()
#         print(response.get("name"),response.get("height"))

# def check_planets(url):
#     for i in range(1, 6):
#         response = requests.get(url + "/" + str(i)).json()
#         print(response.get("name"),response.get("diameter"))

# check_planets(planets_api)
# check_people(people_api)
# check_starships(starships_api)




# password = "password"

# def check_pass(password):
    
