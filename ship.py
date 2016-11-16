import pygame


class Ship:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.ship_image = pygame.image.load('image/download-img-big-3511.jpg')
        self.ship_image = pygame.transform.scale(self.ship_image, (100, 50))

        self.rect = self.ship_image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        elif self.move_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        elif self.move_up and self.rect.top >= self.screen_rect.top:
            self.rect.y -= self.settings.ship_speed_factor
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed_factor

        self.rect.centerx = self.center

    def blit(self):
        self.screen.blit(self.ship_image, self.rect)
