import arcade
import random

SPRITE_SCALING = 0.5
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_TITLE = "sprite with walls"
MOVEMENT_SPEED = 5
VIEWPOINT_MARGIN = 300
class MyGame(arcade.Window):
    def __init__(self, height, width, title):
        super().__init__(width, height, title)

        self.coin_list = None
        self.player_list = None
        self.wall_list = None

        self.player_sprite = None
        self.physics_engine = None

        self.view_left = 0
        self.view_bottom = 0

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("pieceRED_border04.png")
        

        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        for x in range(200, 1650, 210):
            for y in range(0, 1000, 64):
                if random.randrange(5) > 0:
                    wall = arcade.Sprite("box.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
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

        changed = False

        left_boundary = self.view_left + VIEWPOINT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPOINT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        bottom_boundary = self.view_bottom + VIEWPOINT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPOINT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        if changed:
            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left, self.view_bottom, SCREEN_HEIGHT + self.view_bottom)

def main():
    window = MyGame(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE)
    window.setup()
    arcade.run()

main()