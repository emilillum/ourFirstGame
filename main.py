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
PLAYER_JUMP_SPEED = 9
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

        self.time = 0
        self.handle_time = 0

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)


    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        self.background = arcade.load_texture("background-day.png")
        self.background_2 = arcade.load_texture("background-day.png")

        self.scene = arcade.Scene()
        # Sprite lists are created
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Tubes")
        self.scene.add_sprite_list("Base")
        self.scene.add_sprite_list("background")

        self.collisions = [self.scene["Tubes"], self.scene["Base"]]

        # The bird is defined in flappybird.py, imported at the top of the file and called here
        self.player_sprite = flappybird.Bird()

        # the base is definded in base.py, imported at the top of the file and called here
        self.base = base.Base(base_x, base_y)
        self.base_2 = base.Base(base_x + 335, base_y)
        self.base_3 = base.Base(base_x - 335, base_y)

        # 6 sets of tubes are defined in pipe.py, imported at the top of the file and called here
        self.bottom_pipe1, self.top_pipe1 = self.place_pipes(0)
        self.bottom_pipe2, self.top_pipe2 = self.place_pipes(200)
        self.bottom_pipe3, self.top_pipe3 = self.place_pipes(400)
        self.bottom_pipe4, self.top_pipe4 = self.place_pipes(600)
        self.bottom_pipe5, self.top_pipe5 = self.place_pipes(800)
        self.bottom_pipe6, self.top_pipe6 = self.place_pipes(1000)

        # Sprites are added to the initial scene
        self.scene.add_sprite("Player", self.player_sprite)
        self.scene.add_sprite("Base", self.base)
        self.scene.add_sprite("Base", self.base_2)
        self.scene.add_sprite("Base", self.base_3)

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
        """Places pipes with equal spacing"""
        y_offset = randint(0, 240)
        bottom_pipe = pipe.Pipes(280 + x_offset, -15 + y_offset)
        top_pipe = pipe.Pipes(280 + x_offset, 410 + y_offset, flipped=True)
        return bottom_pipe, top_pipe


    def draw_background(self):
        """
        Draws the background.
        """
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.background.width, self.background.height,
                                      self.background, 0)


    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
        self.clear()
        # Code to draw the screen goes here
        self.draw_background()
        self.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.SPACE:
            self.player_sprite.change_y = PLAYER_JUMP_SPEED
            self.player_sprite.texture = self.player_sprite.down_texture
            self.handle_time = self.time

    def handle_prite_animation(self):
        if self.time > self.handle_time + 0.125:
            self.player_sprite.texture = self.player_sprite.mid_texture
        if self.time > self.handle_time +  0.25:
            self.player_sprite.texture = self.player_sprite.up_texture


    def death(self):
        """Whenever the bird hits a tube or the base, it dies"""
        if self.player_sprite.collides_with_list(self.scene["Tubes"]):
            dead = True
        elif self.player_sprite.collides_with_list(self.scene["Base"]):
            dead = True
        else:
            dead = False
        return dead

    def check_base_for_relocating(self, position_x):
        if position_x < -335:
            position_x = base_x + 335
        return position_x

    def move_base(self):
        self.base.center_x = self.base.center_x - 2
        self.base_2.center_x = self.base_2.center_x - 2
        self.base_3.center_x = self.base_3.center_x - 2
        self.base.center_x = self.check_base_for_relocating(self.base.center_x)
        self.base_2.center_x = self.check_base_for_relocating(self.base_2.center_x)
        self.base_3.center_x = self.check_base_for_relocating(self.base_3.center_x)


    def move_kill_and_make_pipes(self):
        self.top_pipe1.center_x, self.bottom_pipe1.center_x = self.top_pipe1.center_x - 2, self.bottom_pipe1.center_x - 2
        self.top_pipe2.center_x, self.bottom_pipe2.center_x = self.top_pipe2.center_x - 2, self.bottom_pipe2.center_x - 2
        self.top_pipe3.center_x, self.bottom_pipe3.center_x = self.top_pipe3.center_x - 2, self.bottom_pipe3.center_x - 2
        self.top_pipe4.center_x, self.bottom_pipe4.center_x = self.top_pipe4.center_x - 2, self.bottom_pipe4.center_x - 2
        self.top_pipe5.center_x, self.bottom_pipe5.center_x = self.top_pipe5.center_x - 2, self.bottom_pipe5.center_x - 2
        self.top_pipe6.center_x, self.bottom_pipe6.center_x = self.top_pipe6.center_x - 2, self.bottom_pipe6.center_x - 2

        if self.top_pipe1.center_x < -20:
            self.bottom_pipe1.kill(); self.top_pipe1.kill()
            self.bottom_pipe1, self.top_pipe1 = self.place_pipes(900)
            self.scene.add_sprite("Tubes", self.top_pipe1)
            self.scene.add_sprite("Tubes", self.bottom_pipe1)

        if self.top_pipe2.center_x < -20:
            self.bottom_pipe2.kill(); self.top_pipe2.kill()
            self.bottom_pipe2, self.top_pipe2 = self.place_pipes(900)
            self.scene.add_sprite("Tubes", self.top_pipe2)
            self.scene.add_sprite("Tubes", self.bottom_pipe2)

        if self.top_pipe3.center_x < -20:
            self.bottom_pipe3.kill(); self.top_pipe3.kill()
            self.bottom_pipe3, self.top_pipe3 = self.place_pipes(900)
            self.scene.add_sprite("Tubes", self.top_pipe3)
            self.scene.add_sprite("Tubes", self.bottom_pipe3)

        if self.top_pipe4.center_x < -20:
            self.bottom_pipe4.kill(); self.top_pipe4.kill()
            self.bottom_pipe4, self.top_pipe4 = self.place_pipes(900)
            self.scene.add_sprite("Tubes", self.top_pipe4)
            self.scene.add_sprite("Tubes", self.bottom_pipe4)

        if self.top_pipe5.center_x < -20:
            self.bottom_pipe5.kill(); self.top_pipe5.kill()
            self.bottom_pipe5, self.top_pipe5 = self.place_pipes(900)
            self.scene.add_sprite("Tubes", self.top_pipe5)
            self.scene.add_sprite("Tubes", self.bottom_pipe5)

        if self.top_pipe6.center_x < -20:
            self.bottom_pipe6.kill(); self.top_pipe6.kill()
            self.bottom_pipe6, self.top_pipe6 = self.place_pipes(900)
            self.scene.add_sprite("Tubes", self.top_pipe6)
            self.scene.add_sprite("Tubes", self.bottom_pipe6)

    def near_edge(self):
        if self.player_sprite.top > SCREEN_HEIGHT:
            self.player_sprite.top = SCREEN_HEIGHT


    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        self.near_edge()
        self.move_base()
        self.move_kill_and_make_pipes()

        self.time = self.time + delta_time
        self.handle_prite_animation()

        dead = self.death()
        if dead == True:
            self.player_sprite.kill()
            arcade.exit()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
