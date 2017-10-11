import pygame


class Rocket():
    """Stores and manipulates data for Rocket"""

    def __init__(self, r_settings, screen):
        """Initialize values for settings and screen"""
        self.r_settings = r_settings
        self.screen = screen
        # Setting up rocket
        self.image = pygame.image.load('rocket.png')
        # Getting rects to get coordinates to center rocket
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
