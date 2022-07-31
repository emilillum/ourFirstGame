import arcade

image_source = "pipe-green.png"


class Pipes(arcade.Sprite):

    def __init__(self, center_x, center_y, flipped=False):
        super().__init__(filename=image_source, center_x=center_x, center_y=center_y, flipped_vertically=flipped)

        
        

