"""
controller.py
by Aiden Jungels

"""
# Get the colors selected by the user.
def get_colors(selected_colors):
    for item in selected_colors:
        if item == "White":
            c_w = True
        if item == "Blue":
            c_u = True
        if item == "Black":
            c_b = True
        if item == "Red":
            c_r = True
        if item == "Green":
            c_g = True
        if item == "Colorless":
            c_co = True