"""
controller.py
by Aiden Jungels

"""
import requests

# Get the colors selected by the user.
def get_colors(selected_colors):
    c_w = ""
    c_u = ""
    c_b = ""
    c_r = ""
    c_g = ""
    for item in selected_colors:
        if item == "White":
            c_w = "+c%3Awhite"
        if item == "Blue":
            c_u = "+c%3Ablue"
        if item == "Black":
            c_b = "+c%3Ablack"
        if item == "Red":
            c_r = "+c%3Ared"
        if item == "Green":
            c_g = "+c%3Agreen"
    
    search_colors = c_w + c_u + c_b + c_r + c_g
    make_call(search_colors)

def make_call(search_colors):
    base_url = "https://api.scryfall.com/cards/random?q=is%3Acommander"
    full_url = base_url + search_colors
    response = requests.get(full_url)
    print(response.json())
    