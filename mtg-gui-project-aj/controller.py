"""
controller.py
by Aiden Jungels

"""
import requests
import random

# Get the colors selected by the user.
def get_colors(selected_colors):
    c_w = ""
    c_u = ""
    c_b = ""
    c_r = ""
    c_g = ""
    for item in selected_colors:
        if item == "White":
            c_w = "w"
        
        if item == "Blue":
            c_u = "u"
        
        if item == "Black":
            c_b = "b"
        
        if item == "Red":
            c_r = "r"
        
        if item == "Green":
            c_g = "g"
    
    search_colors = c_w + c_u + c_b + c_r + c_g
    if search_colors == "":
        possible_colors = ["w", "u", "b", "r", "g"]
        search_colors = random.choices(possible_colors)
        print(search_colors)
    
    return search_colors

def make_call(search_colors) -> str:
    base_url = "https://api.scryfall.com/cards/random?q=is%3Acommander+color%3D"
    full_url = base_url + search_colors
    response = requests.get(full_url).json()
    card_name = response['name']
    return card_name
