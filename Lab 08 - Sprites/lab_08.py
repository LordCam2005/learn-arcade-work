import random
import arcade

# constants
sprite_scaling_player = 0.5
sprite_scaling_coin = 0.2
coin_count = 50

screen_height = 600
screen_width = 800



class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, "sprite shenanigans")

        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.RUBY_RED)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("charecter.png", sprite_scaling_player)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()

        self.coin_list.draw()
        self.player_list.draw()

def main():
    window = MyGame()
    window.setup
    arcade.run()

if __name__ == "__main__":
    main()
    