import random
import pygame
import math

def init_data(n_objects, screen_width, screen_height):
    data = []
    for i in range(n_objects):
        data.append(random.randint(0, screen_height))
    return data


def draw(surface, data, screen_width, screen_height):
    rect_width = screen_width // len(data)
    x = 0

    for i in range(len(data)):
        green = math.floor(data[i] / screen_height * 255)
        blue = math.floor(data[i] / screen_height * 255)
        color = (0, green, blue)
        pygame.draw.rect(surface, color, (x, screen_height-data[i], rect_width, data[i]))
        x += rect_width


def bubbleSort(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] < data[j]:
                t = data[i]
                data[i] = data[j]
                data[j] = t
