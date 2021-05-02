import arcade

WIDTH = 800
HEIGHT = 600
TITLE = "sprite"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.player_sprite = None

    def setup(self):
        self.player_sprite = arcade.Sprite("./player_action1.png", center_x = WIDTH/2, center_y = HEIGHT/2)

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()

window = Game()
window.setup() 
arcade.run()