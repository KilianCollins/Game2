import random

import pygame as pg

pg.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
# screen corners
top_left = (0, 0)
bottom_left = (0, SCREEN_HEIGHT)
top_right = (SCREEN_WIDTH, 0)
bottom_right = (SCREEN_WIDTH, SCREEN_HEIGHT)

# border alert vars
border_alert_rectangle = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
border_alert_rectangle_width = 18

# border normal state
border_normal_state = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
border_normal_state_width = 5


x = 40
y = 40
radius = 40
speed = 4

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

circle = pg.draw.circle(screen,"green", (x, y), radius=radius, width=0)


# def enemy_circle(screen2=screen,x2=10, y2=10, color2="blue", radius2=10, width2=0, speed2=2):
#     screen2
#     circle_2 = pg.draw.circle(screen, color2, (x2, y2), radius=radius, width=0)

random_location_x = random.randint(0, SCREEN_WIDTH - 1)  # this is a start
random_location_y = random.randint(0, SCREEN_HEIGHT - 1)

circle_enemy = pg.draw.circle(screen, "green", (random_location_x, random_location_y), radius=radius, width=0)

run = True

while run:
    keys = pg.key.get_pressed()
    screen.fill("black")
    pg.draw.rect(screen, "green2", border_normal_state, border_normal_state_width)
    circle = pg.draw.circle(screen, "green", (x, y), radius=radius, width=0)




    for event in pg.event.get():
        if event.type == pg.QUIT: # whats the diffrence etween pg.QUIT() & pg.QUIT??
            run = False

    # if

    if keys[pg.K_w]:
        y -= speed
    if keys[pg.K_s]:
        y += speed
    if keys[pg.K_a]:
        x -= speed
    if keys[pg.K_d]:
        x += speed
    if keys[pg.K_ESCAPE]:
        run = False
    # if keys[pg.K_j]:
        # pg.draw.rect(screen, "blue1", pg.Rect(0, 0, 60, 60), 7)

    if x < radius:
        x = radius
        pg.draw.rect(screen, "blue1", border_alert_rectangle, border_alert_rectangle_width)
    if x > SCREEN_WIDTH - radius:
        x = SCREEN_WIDTH - radius
        pg.draw.rect(screen, "blue1", border_alert_rectangle, border_alert_rectangle_width)
    if y < radius:
        y = radius
        pg.draw.rect(screen, "blue1", border_alert_rectangle, border_alert_rectangle_width)
    if y > SCREEN_HEIGHT - radius:
        y = SCREEN_HEIGHT - radius
        pg.draw.rect(screen, "blue1", border_alert_rectangle, border_alert_rectangle_width)





    pg.display.flip()

pg.quit()
