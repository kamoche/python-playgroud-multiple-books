import sys

import pygame

from settings import Settings


def run_game():
    """Initialize game and create a screen object"""
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_hieght))
    pygame.display.set_caption("Alien Invasion")

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse event
        for event in pygame.event.get():

            # Watch for keyboard and mouse event
            if event.type == pygame.QUIT:
                sys.exit()
            # Redraw the screen during each pass through the loop
            screen.fill(ai_setting.bg_color)
            # Make the most drawn screen visible.
            pygame.display.flip()


run_game()
