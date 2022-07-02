import arcade

image_source = "yellowbird-midflap.png"
center_x = 50
center_y = 350

class Bird(arcade.Sprite):

    def __init__(self):
        super().__init__(filename=image_source, center_x=center_x, center_y=center_y)
