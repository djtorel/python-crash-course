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

        # Set center variable
        self.center = float(self.rect.centery)

        # Set initial position
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Set speed factor
        self.speed_factor = self.g_settings.ship_speed_factor

    def blitme(self):
        """Draw ship to screen"""
        self.screen.blit(self.image, self.rect)
