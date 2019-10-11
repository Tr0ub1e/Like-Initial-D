from os import path

class Settings():

# display
    W_Height = 1920
    W_Length = 1080
    grnd_colour = (0,128,128)

    gpath = path.dirname(path.abspath(__file__))
# files
    music = path.join(gpath, "music\\LXST - ODIUM.mp3")
    tree = path.join(gpath, 'images\\tree.png')

# PLAYER'S CAR
    up_image = path.join(gpath, 'images\\car_up.png')
    right_image = path.join(gpath, 'images\\car_right.png')
    left_image = path.join(gpath, 'images\\car_left.png')

# ai_cars
    car1 = path.join(gpath, 'images\\ai_cars\\car1.png')
    car2 = path.join(gpath, 'images\\ai_cars\\car2.png')
    car3 = path.join(gpath, 'images\\ai_cars\\car3.png')
    car4 = path.join(gpath, 'images\\ai_cars\\car4.png')
