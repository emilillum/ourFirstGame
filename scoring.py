import arcade

class Score(arcade.Sprite):

    def __init__(self, filename, center_x, center_y):
        super().__init__(filename=filename, center_x=center_x, center_y=center_y)
