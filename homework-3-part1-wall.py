# Sheridan Wall
# Nov. 3, 2020
# Homework 3 Part 1

# pip install requests
import requests

# url = "https://pokeapi.co/api/v2/pokemon/55/"
# url = "https://pokeapi.co/api/v2/version/"
url = "https://pokeapi.co/api/v2/pokemon/"


response = requests.get(url, allow_redirects=True)
data = response.json()
# print(data.keys())
# version --> dict_keys(['count', 'next', 'previous', 'results'])

#print(data.keys())
# id_55 --> dict_keys(['abilities', 'base_experience', 'forms', 'game_indices', 'height', 'held_items', 'id', 'is_default', 'location_area_encounters', 'moves', 'name', 'order', 'species', 'sprites', 'stats', 'types', 'weight'])

#type --> Sheridans-MacBook-Air:documents sheridanwall$ python homework-3-part1-wall.py 
# dict_keys(['count', 'next', 'previous', 'results'])



# What is the URL to the documentation?
url_documentation = "https://pokeapi.co/docs/v2#pokemon-section"

# What pokemon has the ID of 55?
url_55 = "https://pokeapi.co/api/v2/pokemon/55/"
response = requests.get(url_55, allow_redirects=True)
data = response.json()
print(data['name']) 
# Golduck 

# How tall is that pokemon?
print(data['height']) 
# 17

# How many versions of Pokemon games have been released? --> ASK ABOUT THIS ONE TOMORROW
url_versions = "https://pokeapi.co/api/v2/version/"
response = requests.get(url_versions, allow_redirects=True)
data = response.json()
total_versions = 0
for version in data['results']:
    total_versions = total_versions + 1
print("There are" , total_versions , "versions of the Pokemon games") 

# Print out the name of every electric-type pokemon
url_type = "https://pokeapi.co/api/v2/type/electric"
response = requests.get(url_type, allow_redirects=True)
data = response.json()
for pokemon_type in data['pokemon']:
    print("--------------------")
    print(pokemon_type['pokemon']['name'])

# What are electric-type Pokemon called in the Korean version of the game?
# print(data.keys())
# print(data['name']) --> type name
# print(data['pokemon']) --> pokemon names
# print(data['names']) --> language names
for name in data['names']:
    # print(name['language'])
    if name['language']['name'] == 'ko':
        print(name['name'])

# Who has a higher speed stat, Eevee or Pikachu?
# url_stats = "https://pokeapi.co/api/v2/pokeathlon-stat/"
# print(data['results'])
# for stat in data['results']:
#     print(stat['name'])
url1 = "https://pokeapi.co/api/v2/pokemon/eevee"
url2 = "https://pokeapi.co/api/v2/pokemon/pikachu"

 response = requests.get(url1, allow_redirects=True)
data = response.json()
# print(data.keys())

for stat in data['stats']:
    speed1 = stat['stat']
    if speed1['name'] == 'speed':
       eevee_speed = stat['base_stat'] # --> 55

response = requests.get(url2, allow_redirects=True)
data = response.json()

for stat in data['stats']:
    speed2 = stat['stat']
    if speed2['name'] == 'speed':
        pikachu_speed = stat['base_stat']  # --> 90

if eevee_speed > pikachu_speed:
    print("Eevee has a higher speed stat")
else:
    print("Pikachu has a higher speed stat")



 

