import pygame


class Star():
    """Class to construct star objects"""

    def __init__(self, g_settings, screen):
        """Init variables needed"""
        # Init settings and screen
        self.g_settings = g_settings
        self.screen = screen

        # Set image and rects
        self.image = pygame.image.load('images\star.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Set initial position
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left

    def draw_star(self):
        """Function to draw star object"""
        self.screen.blit(self.image, self.rect)
