import arcade
import flappybird
import base
import pipe
from random import randint

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

        self.collisions = [self.scene["Tubes"], self.scene["Base"]]

        # The bird is defined in flappybird.py, imported at the top of the file and called here
        self.player_sprite = flappybird.Bird()

        # Base set up
        self.base = base.Base(base_x, base_y)

        self.bottom_pipe1, self.top_pipe1 = self.place_pipes(0)
        self.bottom_pipe2, self.top_pipe2 = self.place_pipes(200)
        self.bottom_pipe3, self.top_pipe3 = self.place_pipes(400)
        self.bottom_pipe4, self.top_pipe4 = self.place_pipes(600)
        self.bottom_pipe5, self.top_pipe5 = self.place_pipes(800)
        self.bottom_pipe6, self.top_pipe6 = self.place_pipes(1000)


        self.scene.add_sprite("Player", self.player_sprite)
        self.scene.add_sprite("Base", self.base)
        self.scene.add_sprite("Tubes", self.top_pipe1)
        self.scene.add_sprite("Tubes", self.bottom_pipe1)
        self.scene.add_sprite("Tubes", self.top_pipe2)
        self.scene.add_sprite("Tubes", self.bottom_pipe2)
        self.scene.add_sprite("Tubes", self.top_pipe3)
        self.scene.add_sprite("Tubes", self.bottom_pipe3)
        self.scene.add_sprite("Tubes", self.top_pipe4)
        self.scene.add_sprite("Tubes", self.bottom_pipe4)
        self.scene.add_sprite("Tubes", self.top_pipe5)
        self.scene.add_sprite("Tubes", self.bottom_pipe5)
        self.scene.add_sprite("Tubes", self.top_pipe6)
        self.scene.add_sprite("Tubes", self.bottom_pipe6)


        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.collisions
        )
    
    def place_pipes(self, x_offset):
        y_offset = randint(0, 240)
        bottom_pipe = pipe.Pipes(200 + x_offset, -5 + y_offset)
        top_pipe = pipe.Pipes(200 + x_offset, 420 + y_offset, flipped=True)
        return bottom_pipe, top_pipe

    

        

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
    
    
    def near_edge(self):
        if self.player_sprite.top > SCREEN_HEIGHT:
            self.player_sprite.top = SCREEN_HEIGHT


    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        self.near_edge()
        
        #self.death()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
