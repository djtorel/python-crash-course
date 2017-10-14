# Stars: Find an image of a star. Make a grid of stars appear on the
# screen.

# Imports
import pygame

from settings import Settings
import game_functions as gf
from star import Star

# Main function


def main():
    """Main game function"""
    # Init pygame and settings
    pygame.init()
    g_settings = Settings()

    # Create game window
    screen = gf.new_window(g_settings.screen_width,
                           g_settings.screen_height,
                           g_settings.caption)

    # Create star object
    star = Star(g_settings, screen)

    # Game loop
    while True:
        # Check events
        gf.check_events()

        # Update screen
        gf.update_screen(g_settings, screen, star)


# Run game
main()
