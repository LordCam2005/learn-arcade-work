import arcade

arcade.open_window(800, 800, "yeet")
arcade.set_background_color(arcade.color.SKY_BLUE)
arcade.start_render()
# ground
arcade.draw_circle_filled(0, -100, 200, arcade.color.APPLE_GREEN)
arcade.draw_circle_outline(0, -100, 200, arcade.color.GREEN_YELLOW)
arcade.draw_line(0, 25, 800, 25, arcade.color.GREEN_YELLOW)
arcade.draw_rectangle_filled(400, 0, 800, 50, arcade.color.APPLE_GREEN)

# truck
arcade.draw_circle_filled(400, 35, 10, arcade.color.BLACK)
arcade.draw_circle_filled(450, 35, 10, arcade.color.BLACK)
arcade.draw_circle_filled(400, 35, 5, arcade.color.WHITE)
arcade.draw_circle_filled(450, 35, 5, arcade.color.WHITE)
arcade.draw_rectangle_filled(425, 45, 75, 15, arcade.color.BLACK)
arcade.draw_triangle_filled(387, 50, 400, 50, 400, 70, arcade.color.BLACK)
arcade.draw_rectangle_filled(430, 65, 65, 30, arcade.color.BLUE)

# sun
arcade.draw_circle_filled(10, 790, 50, arcade.color.SUNGLOW)

# cloud 1
arcade.draw_circle_filled(300, 600, 25, arcade.color.GRAY)
arcade.draw_circle_filled(330, 630, 40, arcade.color.GRAY)
arcade.draw_circle_filled(270, 620, 30, arcade.color.GRAY)
arcade.draw_circle_filled(370, 610, 40, arcade.color.GRAY)

# cloud 2
arcade.draw_circle_filled(600, 700, 30, arcade.color.GRAY)
arcade.draw_circle_filled(630, 730, 44, arcade.color.GRAY)
arcade.draw_circle_filled(570, 720, 25, arcade.color.GRAY)
arcade.draw_circle_filled(670, 710, 20, arcade.color.GRAY)

arcade.finish_render()
arcade.run()
