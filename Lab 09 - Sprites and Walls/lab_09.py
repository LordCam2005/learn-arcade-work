import arcade

SPRITE_SCALING = 0.5
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_TITLE = "srite with walls"
MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self, height, width, title):
        super().__init__(width, height, title)

        self.coin_list = None
        self.player_list = None
        self.wall_list = None

        self.player_sprite = None
        self.physics_engine = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("player_action1.png")
        

        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        for x in range(173,650,64):
            wall = arcade.Sprite("box.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)

        for y in range(273, 500, 64):
            wall = arcade.Sprite("box.png", SPRITE_SCALING)
            wall.center_y = y
            wall.center_x = 495
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED
        
    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0
    
    def on_update(self, delta_time):
        self.physics_engine.update()

def main():
    window = MyGame(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE)
    window.setup()
    arcade.run()

main()