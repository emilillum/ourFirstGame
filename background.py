import arcade
image_source = 'background-day.png'

class Background(arcade.Sprite):

    def __init__(self, base_x, base_y):
        super().__init__(filename=image_source, center_x=base_x, center_y=base_y)
