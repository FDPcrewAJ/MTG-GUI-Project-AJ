"""
controller.py
by Aiden Jungels
This contains two functions - get_colors() sets up which colors needed to be added to the api call,
and make_call(), which makes the call to the scryfall API including the colors that need to be
searched for. If the user left all colors unselected, then it will just call for a random commander.
It then gets the name of the card from the returned API file.
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
    
    return search_colors

def make_call(search_colors) -> str:
    # Set up the API call URL
    base_url = "https://api.scryfall.com/cards/random?q=is%3Acommander"
    color_add = ""
    if search_colors != "":
        color_add = "+color%3D"
    full_url = base_url + color_add + search_colors
    
    # Make API call and get card name from it
    response = requests.get(full_url).json()
    card_name = response['name']
    print(response['color_identity'])
    return card_name
