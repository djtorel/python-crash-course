# Make a Pygame window with a blue background.

import sys

import pygame


def blue_sky():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    bg_color = (0, 0, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Fill screen with blue and draw it
        screen.fill(bg_color)
        pygame.display.flip()


blue_sky()
