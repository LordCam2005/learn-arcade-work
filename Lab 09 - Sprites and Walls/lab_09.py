import arcade

SPRITE_SCALING = 0.5
SCREEEN_HEIGHT = 800
SCREEN_WIDTH = 1000
SCREEN_TITLE = "srite with walls"
MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self, height, width, title):
        super().__init__(self, width, height, title)

        self.coin_list = None
        self.player_list = None
        self.wall_list = None

        self.player_sprite = None
        self.physics_engine = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()