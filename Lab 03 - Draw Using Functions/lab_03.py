import arcade
import math

width = 1000
height = 800


def on_draw(dt):
    arcade.start_render()
    if on_draw.x >= 975 or on_draw.x <= 25:
        on_draw.change_x *= -1
    if on_draw.y >= 775 or on_draw.y < 25:
        on_draw.change_y *= -1
    arcade.draw_circle_filled(on_draw.x, on_draw.y, 25, arcade.color.RED)
    on_draw.x += on_draw.change_x
    on_draw.y += on_draw.change_y

on_draw.x = 100
on_draw.y = 100

on_draw.change_x = 1
on_draw.change_y = 1



arcade.open_window(width, height, "yeet")
arcade.schedule(on_draw, 1/60)
arcade.run()