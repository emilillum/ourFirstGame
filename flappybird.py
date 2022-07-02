import arcade

class Bird(arcade.Sprite):

    def __init__(self, image_source, center_x, center_y):
        super().__init__(filename=image_source, center_x=center_x, center_y=center_y)
    
        