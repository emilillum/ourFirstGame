import arcade
import flappybird
import base

# Constants
SCREEN_WIDTH = 280
SCREEN_HEIGHT = 510
SCREEN_TITLE = "My Flappy Bird"

CHARACTER_SCALING = 1
TILE_SCALING = 0.5
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0.7
PLAYER_JUMP_SPEED = 12
base_x = SCREEN_WIDTH//2
base_y = 40


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, center_window = True)

        self.scene = None

        self.player_sprite = None

        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)


    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        self.background = arcade.load_texture("background-day.png")

        self.scene = arcade.Scene()
        # Sprite lists are created
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Tubes")
        self.scene.add_sprite_list("Base")

        # The location of the bird is setup
        image_source = "yellowbird-midflap.png"
        center_x = 50
        center_y = 350
        self.player_sprite = flappybird.Bird(image_source, center_x, center_y)

        # Base set up
        self.base = base.Base(base_x, base_y)


        self.scene.add_sprite("Player", self.player_sprite)
        self.scene.add_sprite("Base", self.base)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Tubes", "Base"]
        )
    
    def draw_background(self):
        """
        Draws the background.
        """
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.background.width, self.background.height,
                                      self.background, 0)


    def on_draw(self):
        """Render the screen."""

        self.clear()
        # Code to draw the screen goes here
        self.draw_background()
        self.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.SPACE:
            self.player_sprite.change_y = PLAYER_JUMP_SPEED

'''
        if dead == False:
            if key == arcade.key.SPACE:
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
    
    def death(self):
        dead = False
        if self.player_sprite.bottom < self.base.height:
            self.player_sprite.bottom = self.base.height
            dead = True
        return dead
'''
    
    
    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        if self.player_sprite.top > SCREEN_HEIGHT:
            self.player_sprite.top = SCREEN_HEIGHT
        
        #self.death()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
