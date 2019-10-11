import pygame
from settings import Settings
import game_func as gf
from car import Car
from trees import Tree
from ai_cars import Ai_cars


def main():

    gset = Settings()

    pygame.init()
    pygame.display.set_caption("Initial D")

    car1 = pygame.image.load(gset.car1)
    car2 = pygame.image.load(gset.car2)
    car3 = pygame.image.load(gset.car3)
    car4 = pygame.image.load(gset.car4)

    score = 0
    cars_images = [car1, car2, car3, car4]

    game_sound = pygame.mixer.music
    game_sound.load(gset.music)
    game_sound.play(-1)

    screen = pygame.display.set_mode((gset.W_Height, gset.W_Length), pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE)
    screen.fill(gset.grnd_colour)

    my_car = Car(screen)
    clock = pygame.time.Clock()

    woods = pygame.sprite.Group()
    woods2 = pygame.sprite.Group()
    cars = pygame.sprite.Group()

    debug = False

    while True:
        clock.tick(60)
        score += 1
        screen.fill(gset.grnd_colour)

        gf.check_event(score)

        keys = pygame.key.get_pressed()
        direction = gf.check_dir(keys)

        my_car.update(direction, debug)
        my_car.blitme()

        gf.check_trees_left(woods, screen)
        gf.check_trees_right(woods2, screen)
        gf.update_trees(woods, woods2, screen, gset.W_Height)

        gf.check_cars(cars, screen, cars_images)
        gf.update_cars(cars, screen, my_car, gset.W_Height)

# x and y chord
        screen.blit(gf.game_score(score), (538, 916))
        screen.blit(gf.speed(), (1138, 916))

        pygame.display.update()


if __name__ == '__main__':
    main()
