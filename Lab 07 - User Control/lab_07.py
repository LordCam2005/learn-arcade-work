import arcade
import pathlib
import os

screen_width = 800
screen_height = 600


class Ball:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(
            self.position_x, self.position_y, self.radius, self.color
        )


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.HOT_PINK)
        self.ball = Ball(50, 50, 15, arcade.color.ASH_GREY)
        self.sound = arcade.Sound(
            pathlib.Path(
                os.path.join(
                    pathlib.Path(__file__).parent.absolute(), pathlib.Path("cannon.wav")
                )
            )
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            arcade.play_sound(self.sound)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball.position_x = x
        self.ball.position_y = y


def main():
    window = MyGame(800, 600, "yeet")
    arcade.run()


main()
