import pygame


class Ship():
    """Class to store values and funcionality of Ship objects"""

    def __init__(self, screen, g_settings):
        """Initialize variables and settings for Ship object"""
        # Initialize variables
        self.screen = screen
        self.g_settings = g_settings

        # Set image for ship
        self.image = pygame.image.load('images\ship.png')

        # Set rects
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set initial position
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Set center variable
        self.center = float(self.rect.centery)

        # Set speed factor
        self.speed_factor = self.g_settings.ship_speed_factor

        # Set movement variables
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw ship to screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update ship position on screen"""
        if self.moving_up and self.rect.top > 0:
            self.center -= self.speed_factor

        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.center += self.speed_factor

        self.rect.centery = self.center
