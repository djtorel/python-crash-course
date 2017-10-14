import sys

import pygame


def new_window(screen_width, screen_height, caption):
    """Create new game window"""
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(caption)
    return screen


def check_events():
    """Check for events, then determine what to do"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(g_settings, screen):
    """Functions to run when refreshing screen"""
    # Set background color
    screen.fill(g_settings.bg_color)

    # Draw fram
    pygame.display.flip()
