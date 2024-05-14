"""
controller.py
by Aiden Jungels

"""
import requests

# Get the colors selected by the user.
def get_colors(selected_colors):
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
    make_call()

def make_call():
    base_url = "https://api.scryfall.com/cards/random?q=is%3Acommander"
    query = {'name'}
    response = requests.get(base_url)
    print(response.json())
    