from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import requests
import pprint

# import math
import random

pp = pprint.PrettyPrinter(indent=2, depth=2)


def randomizer():
    rand_num = random.randint(1, 400)
    return rand_num


def get_pokemon_urls(poke_type):
    endpoint = f"https://pokeapi.co/api/v2/type/{poke_type}"
    response = requests.get(endpoint)
    responseJSON = response.json()
    pokemon_list = responseJSON["pokemon"]
    # pp.pprint(responseJSON["pokemon"][0])
    pokemon_results = []
    for i in range(6):
        try:
            rand_pokemon = random.randint(0, len(pokemon_list) - 1)
            pokemon_results.append(pokemon_list[rand_pokemon]["pokemon"]["url"])
        except pokemon_list[rand_pokemon]["pokemon"]["url"] in pokemon_results:
            print(pokemon_results)
            rand_pokemon = random.randint(0, len(pokemon_list) - 1)
            pokemon_results.append(pokemon_list[rand_pokemon]["pokemon"]["url"])

    return pokemon_results


# def get_pokemon_url(poke_type):
#     endpoint = f"https://pokeapi.co/api/v2/type/{poke_type}"
#     response = requests.get(endpoint)
#     responseJSON = response.json()
#     pokemon_list = responseJSON["pokemon"]
#     rand_pokemon = random.randint(0, len(pokemon_list))
#     pokemon_url = pokemon_list[rand_pokemon]["pokemon"]["url"]

#     return pokemon_url


# def get_pokemon_sprite(pokemon_url):
#     response = requests.get(pokemon_url)
#     responseJSON = response.json()
#     official_artwork_url = responseJSON["sprites"]["other"]["official-artwork"][
#         "front_default"
#     ]

# def get_pokemon_sprites(pokemon_type):
#     for i in range(6):
#       try:
#         pokemon_url = get_pokemon_url(pokemon_type)
#         sprite = get_pokemon_sprite(pokemon_url)
#       except sprite == None:


def get_pokemon_sprites(poke_list):
    results = []
    for url in poke_list:
        endpoint = url
        response = requests.get(endpoint)
        responseJSON = response.json()
        official_artwork_url = responseJSON["sprites"]["other"]["official-artwork"][
            "front_default"
        ]
        if official_artwork_url == None:
            official_artwork_url = responseJSON["sprites"]["front_default"]
        results.append(official_artwork_url)
        # pp.pprint(responseJSON["sprites"]["other"]["official-artwork"]["front_default"])
    return results


def index(request):
    rand_num = request.GET.get("id")
    if rand_num == None:
        rand_num = randomizer()

    endpoint = f"https://pokeapi.co/api/v2/pokemon/{rand_num}"
    response = requests.get(endpoint)
    responseJSON = response.json()

    pokemon_type = responseJSON["types"][0]["type"]["name"]
    # get_pokemon_urls(pokemon_type)
    # pp.pprint(responseJSON["types"][0]["type"]["name"])
    poke_list = get_pokemon_urls(pokemon_type)
    poke_sprites = get_pokemon_sprites(poke_list)
    context = {"type": pokemon_type, "sprite_urls": poke_sprites}

    return render(request, "index.html", context)
