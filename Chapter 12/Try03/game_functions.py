import sys

import pygame


def check_events():
    """Functions for handling events"""
    # Start event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def window(width, height, caption):
    """Create window using width, height, and caption"""
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return screen


def update_screen(r_settings, screen):
    # Draw background
    screen.fill(r_settings.bg_color)

    # Refresh screen
    pygame.display.flip()
