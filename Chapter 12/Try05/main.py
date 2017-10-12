# Sideways Shooter: Write a game that places a ship on the left side of
# the screen and allows the player to move the ship up and down. Make
# the ship fire a bullet that travels right across the screen when the
# player presses the spacebar. Make sure bullets are deleted once they
# disappear off the screen.

# Imports
import pygame

from settings import Settings
import game_functions as gf


def main():
    # Init pygame and settings
    pygame.init()
    g_settings = Settings()

    # Set up screen
    screen = gf.new_window(g_settings.screen_width,
                           g_settings.screen_height,
                           g_settings.caption)

    # Set up variables for ship and bullets

    # Main loop
    while True:

        # Check for events
        gf.check_events()

        # Update ship

        # Update bullets

        # Refresh screen
        gf.update_screen(screen, g_settings)


main()
