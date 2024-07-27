import pygame as pg
import random

pg.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

border_alert_rectangle = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
border_alert_rectangle_width = 18

# border normal state
border_normal_state = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
border_normal_state_width = 5

# enemy stuff
# x = 70
# y = 70
# radius = 70
# speed = 2

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def enemy_circle(x=10, y=10, color="blue", radius=10, width=0, speed=2):
    circle = pg.draw.circle(screen, color, (x, y), radius=radius, width=0)


