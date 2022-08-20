import arcade

image_source = "yellowbird-midflap.png"
image_source2 = "yellowbird-downflap.png"
image_source3 = "yellowbird-upflap.png"
center_x = 50
center_y = 350

class Bird(arcade.Sprite):

    def __init__(self):
        super().__init__(filename=image_source, center_x=center_x, center_y=center_y)

        self.up = False
        self.down = False
        self.mid = False

        self.mid_texture = arcade.load_texture(image_source)
        self.down_texture = arcade.load_texture(image_source2)
        self.up_texture = arcade.load_texture(image_source3)
