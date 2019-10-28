import math

class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # self.num_of_objects = 255
        self.num_of_objects = math.floor(self.screen_width / 6)
