import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Store information and functions for bullets"""

    def __init__(self, screen, g_settings, ship):
        """Init super class and bullet variables"""
        super().__init__()
        # Init screen
        self.screen = screen

        # Set max distance
        self.max_distance = g_settings.screen_width

        # Width and height and color
        self.width = g_settings.bullet_width
        self.height = g_settings.bullet_height
        self.color = g_settings.bullet_color

        # Speed factor
        self.speed = g_settings.bullet_speed_factor

        # Create bullet at (0,0) then move it to front of ship
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right

    def update(self):
        """Update bullet position"""
        self.rect.centerx += self.speed

    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
