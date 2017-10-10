import sys

import pygame


def game_character():
    pygame.init()

    # Init window size and background color
    screen = pygame.display.set_mode((800, 600))
    bg_color = (40, 40, 40)
    pygame.display.set_caption("Game Character")

    # Load megaman image and center
    megaman = pygame.image.load('megaman.png')
    screen_rect = screen.get_rect()
    megaman_rect = megaman.get_rect()
    megaman_rect.center = screen_rect.center

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        screen.blit(megaman, megaman_rect)

        pygame.display.flip()


game_character()
