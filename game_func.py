import pygame
from random import choice, randint
from car import Car
from trees import Tree
from ai_cars import Ai_cars

def check_dir(keys):

    # checking pressed keys and choosing direction

    if keys[pygame.K_LEFT]:
        direction = "left"

    elif keys[pygame.K_RIGHT]:
        direction = "right"

    elif keys[pygame.K_UP]:
        direction = "up"

    elif keys[pygame.K_DOWN]:
        direction = "down"

    else:
        direction = None

    return direction

def check_event(score):

    #checking events

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("\n\nYour score is:" +str(score))
                pygame.quit()
                exit()

def check_trees_left(woods, screen):

    #spawning trees on left side

    if len(woods) < 10:
        new_tree = Tree(screen, "left")
        if pygame.time.get_ticks() % 10 == 0:
            woods.add(new_tree)

def check_trees_right(woods, screen):

    #spawning trees in right side

    if len(woods) < 10:
        new_tree = Tree(screen, "right")
        if pygame.time.get_ticks() % 10 == 0:
            woods.add(new_tree)

def update_trees(woods, woods2, screen, screen_height):

    # drawing trees on left and right side

    woods.draw(screen)
    woods2.draw(screen)

    # running trees down and del them

    for tree in woods.copy():
        tree.rect.y += 15

        if tree.rect.y > screen_height - 175:
            woods.remove(tree)

    for tree in woods2.copy():
        tree.rect.y += 15

        if tree.rect.y > screen_height - 175:
            woods2.remove(tree)


def check_cars(cars, screen, cars_images):

    #random image car and spawning every second
    image = choice(cars_images)

    if len(cars) < 15:
        new_car = Ai_cars(screen, image)
        if pygame.time.get_ticks() % 10 == 0:
            cars.add(new_car)

def update_cars(cars, screen, my_car, screen_height):

    #drawing cars and checking for collision

    cars.draw(screen)

    for car in cars.copy():
        car.rect.y += 15

        if car.rect.colliderect(my_car):
            pygame.quit()
            exit()

        if car.rect.y > screen_height - 175:
            cars.remove(car)


def game_score(score):

    # just dinamic game score

    score_f = pygame.font.SysFont("arial", 48)
    textsurf = score_f.render("Score: " + str(score), False, (0,0,0))

    return textsurf

def speed():

    # just static speed (only text)

    spd_f = pygame.font.SysFont("arial", 48)
    textsurf = spd_f.render("Speed: 190 km/h", False, (0,0,0))

    return textsurf
