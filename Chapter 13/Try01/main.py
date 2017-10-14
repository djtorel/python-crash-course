# Stars: Find an image of a star. Make a grid of stars appear on the
# screen.

# Imports
import pygame

from settings import Settings
import game_functions as gf


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

    # Game loop
    while True:
        # Check events
        gf.check_events()

        # Update screen
        gf.update_screen(g_settings, screen)


# Run game
main()
