# Make a game that begins with a rocket in the center of the screen.
# Allow the player to move the rocket up, down, left, or right using the
# four arrow keys. Make sure the rocket never moves beyond any edge of
# the screen.

import sys

import pygame


def rocket():
    """Init Pygame and run game functions and main loop"""
    pygame.init()

    # Set up Window, background, and title bar caption
    screen = pygame.display.set_mode((800, 600))
    bg_color = (40, 40, 40)
    pygame.display.set_caption("Rocket")

    while True:
        # Start event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Draw background
        screen.fill(bg_color)

        # Refresh screen
        pygame.display.flip()


rocket()
