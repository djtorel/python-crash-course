import sys

import pygame


def check_events():
    """Functions for handling events"""
    # Start event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(r_settings, screen):
    # Draw background
    screen.fill(r_settings.bg_color)

    # Refresh screen
    pygame.display.flip()
