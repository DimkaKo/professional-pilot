import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self, screen, width, position):
        super().__init__()

        self.screen = screen
        self.position = position
        self.rect = pygame.Rect(0, 0, width, 100)
        if position == 'left':
            self.rect.left = screen.get_rect().left
        elif position == 'right':
            self.rect.right = screen.get_rect().right

        self.rect.bottom = 0

        self.y = float(self.rect.y)
        self.speed_factor = 1.5
        self.color = (0, 0, 255)

    def update(self):
        self.y += self.speed_factor
        self.rect.y = self.y

    def is_left_block(self):
        return self.position == 'left'

    def is_right_bloc(self):
        return self.position == 'right'

    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
