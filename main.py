import pygame
import sys
import random
import time
from setting import Settings
from ship import Ship
from block import Block
from pygame.sprite import Group


def main():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(screen, settings)
    blocks = Group()

    current_milliseconds = lambda: int(round(time.time() * 1000))
    delay_time = 0

    pygame.display.set_caption('Alien game')
    bg_image = pygame.image.load('image/bg.jpg')

    while True:

        ############

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.move_right = True
                elif event.key == pygame.K_LEFT:
                    ship.move_left = True
                elif event.key == pygame.K_UP:
                    ship.move_up = True
                elif event.key == pygame.K_DOWN:
                    ship.move_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.move_right = False
                elif event.key == pygame.K_LEFT:
                    ship.move_left = False
                elif event.key == pygame.K_UP:
                    ship.move_up = False
                elif event.key == pygame.K_DOWN:
                    ship.move_down = False

        ############


        if current_milliseconds() > delay_time:
            property = generate_random_width(settings, ship)
            blocks.add(Block(screen, property[0], 'left'), Block(screen, property[1], 'right'))
            delay_time = current_milliseconds() + 3000

        ############

        ship.update()
        screen.blit(bg_image, (0, 0))
        ship.blit()

        ############

        blocks.update()

        for block in blocks.copy():
            crash_test(ship, block)
            if block.rect.top == screen.get_rect().bottom:
                blocks.remove(block)

        for block in blocks.sprites():
            block.blitme()

        ############

        pygame.display.flip()


def generate_random_width(settings, ship):
    expansivity = 90
    max_width = settings.screen_width - (ship.rect.width + expansivity)
    while True:
        number = random.randint(1, settings.screen_width)
        if number <= max_width:
            return number, max_width - number


def crash_test(ship, block):
    if ship.rect.top <= block.rect.bottom and ship.rect.bottom >= block.rect.top:
        if block.is_left_block():
            if ship.rect.left <= block.rect.right:
                print('задел левый блок')
        elif block.is_right_bloc():
            if ship.rect.right >= block.rect.left:
                print('задел правый блок')


if __name__ == '__main__':
    main()
