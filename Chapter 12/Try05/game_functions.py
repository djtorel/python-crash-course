import sys

import pygame

from bullet import Bullet


def new_window(screen_width, screen_height, caption):
    """Create game window using inputted values, return screen"""
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(caption)

    return screen


def check_keydown_events(event, screen, g_settings, ship, bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, g_settings, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(screen, g_settings, ship, bullets):
    """Check for events and determine what to do"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, g_settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def draw_bullets(bullets):
    """Function to update bullets on screen"""
    for bullet in bullets.sprites():
        bullet.draw_bullet()


def update_bullets(bullets):
    """Update bullet position and remove if off screen"""
    bullets.update()
    # Remove if off screen
    for bullet in bullets.copy():
        if bullet.rect.left >= bullet.max_distance:
            bullets.remove(bullet)


def update_screen(screen, g_settings, ship, bullets):
    """Functions to update screen and draw objects on them"""
    # Fill background
    screen.fill(g_settings.bg_color)

    # Draw bullets
    draw_bullets(bullets)

    # Draw ship
    ship.blitme()

    # Refresh screen
    pygame.display.flip()
