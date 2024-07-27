# dsfgn

import pygame as pg

pg.init()


class IDK_ill_rename_later(object):

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # screen corners
    top_left = (0, 0)
    bottom_left = (0, SCREEN_HEIGHT)
    top_right = (SCREEN_WIDTH, 0)
    bottom_right = (SCREEN_WIDTH, SCREEN_HEIGHT)

    border_alert_rectangle = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    border_alert_rectangle_width = 18


    # border normal state
    border_normal_state = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    border_normal_state_width = 5

    x = 40
    y = 40
    radius = 40
    speed = 4


    def __init__(self): #what am i suposed to do here?? -k 7_26_24
        self.screen
        self.radius
        self.x
        self.y

    circle = pg.draw.circle(screen, "green", (x, y), radius=radius, width=0)

    def enemy(self, radius_p=10, x_p=10, y_p=10, color_p="white", width_p=0 ):
        self.radius = radius_p
        self.x = x_p
        self.y = y_p




