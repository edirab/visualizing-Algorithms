import pygame, sys
from settings import Settings
import functions as f


def run_game():

    app_settings= Settings()

    pygame.init()
    screen = pygame.display.set_mode(
        (app_settings.screen_width, app_settings.screen_height))
    pygame.display.set_caption("Visualization")

    data = f.init_data(app_settings.num_of_objects, app_settings.screen_width, app_settings.screen_height)
    f.bubbleSort(data)

    while True:
        screen.fill(app_settings.bg_color)
        f.draw(screen, data, app_settings.screen_width, app_settings.screen_height)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

run_game()