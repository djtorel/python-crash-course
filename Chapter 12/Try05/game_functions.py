import sys

import pygame


def new_window(screen_width, screen_height, caption):
    """Create game window using inputted values, return screen"""
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(caption)

    return screen


def check_events():
    """Check for events and determine what to do"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen, g_settings, ship):
    """Functions to update screen and draw objects on them"""
    # Fill background
    screen.fill(g_settings.bg_color)

    # Draw ship
    ship.blitme()

    # Refresh screen
    pygame.display.flip()
