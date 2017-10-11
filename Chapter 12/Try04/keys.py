# Make a Pygame file that creates an empty screen. In the event loop,
# print the event.key attribute whenever a pygame.KEYDOWN event is
# detected. Run the program and press various keys to see how Pygame
# responds.

import sys

import pygame


def keys():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Keys")
    bg_color = (40, 40, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

        screen.fill(bg_color)
        pygame.display.flip()


keys()
