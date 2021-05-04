import arcade

WIDTH = 800
HEIGHT = 600
TITLE = "sprite"
MOVEMENT_SPEED = 3

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.player_sprite = None
        self.set_mouse_visible(False)

    def setup(self):
        self.player_sprite = arcade.Sprite("./player_action1.png", center_x = WIDTH/2, center_y = HEIGHT/2)

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()

    def update(self, delta_time):
        self.player_sprite.update()
    
    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0

window = Game()
window.setup() 
arcade.run()