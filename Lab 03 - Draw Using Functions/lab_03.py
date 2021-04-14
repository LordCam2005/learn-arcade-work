import arcade
from random import randint, choice

width = 2000
height = 1000
balls = []


class Ball:
    def __init__(self, x, y, vx, vy, size, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = size
        self.color = color

    def update(self):

        if self.x >= width or self.x <= 0:
            self.vx *= -1
        if self.y >= height or self.y < 0:
            self.vy *= -1
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)


def on_draw(dt):
    arcade.start_render()

    for b in balls:
        b.update()
        b.draw()


for i in range(1000):
    b = Ball(
        randint(0, width),
        randint(0, height),
        randint(1, 100),
        randint(0, 10),
        randint(0, 10),
        arcade.color.RED,
    )
    balls.append(b)


arcade.open_window(width, height, "yeet")
arcade.schedule(on_draw, 1 / 60)
arcade.run()
