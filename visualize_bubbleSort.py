import pygame, sys
from settings import Settings
import functions as f


def run_game():

    app_settings= Settings()

    pygame.init()
    screen = pygame.display.set_mode(
        (app_settings.screen_width, app_settings.screen_height))
    pygame.display.set_caption("Visualization")
    # pygame.event.set_blocked(None)

    data = f.init_data(app_settings.num_of_objects, app_settings.screen_width, app_settings.screen_height)

    for i in range(len(data)):
        for j in range(len(data)):
            # Чтобы игра не зависла
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            if data[i] < data[j]:
                t = data[i]
                data[i] = data[j]
                data[j] = t

                screen.fill(app_settings.bg_color)
                f.draw(screen, data, app_settings.screen_width, app_settings.screen_height)
                pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

run_game()