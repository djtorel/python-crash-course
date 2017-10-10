# Make a game that begins with a rocket in the center of the screen.
# Allow the player to move the rocket up, down, left, or right using the
# four arrow keys. Make sure the rocket never moves beyond any edge of
# the screen.

import sys

import pygame

from settings import Settings
import game_functions as gf


def rocket():
    """Init Pygame and run game functions and main loop"""
    pygame.init()
    r_settings = Settings()
    # Set up Window, background, and title bar caption
    screen = gf.window(r_settings.screen_width, r_settings.screen_height,
                       r_settings.caption)

    while True:
        gf.check_events()
        gf.update_screen(r_settings, screen)


rocket()
