import random
import time
import pygame as pg

pg.init()
# inventory screen
SCREEN_WIDTH_i = 640
SCREEN_HEIGHT_i = 360
# inventory_screen = pg.display.set_mode((SCREEN_WIDTH_i, SCREEN_HEIGHT_i))
# i will figure hoe to draw another screen on top later
inventor_screen = pg.Rect(320,180, SCREEN_WIDTH_i, SCREEN_HEIGHT_i)


# main screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen corners
# top_left = (0, 0)
# bottom_left = (0, SCREEN_HEIGHT)
# top_right = (SCREEN_WIDTH, 0)
# bottom_right = (SCREEN_WIDTH, SCREEN_HEIGHT)
dt = 0
clock = pg.time.Clock()

# border alert vars
border_alert_rectangle = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
border_alert_rectangle_width = 18

# border normal state
border_normal_state = pg.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
border_normal_state_width = 5

# player
x = 40
y = 40
radius = 40
speed = 500

# enemy set up
viable_points_list = [(40, 40), (45, 45), (53, 60), (134, 680), (590, 49), (89, 389), (1000,600),
                      (985, 201), (81, 407),]
# make an algorithim to automate pairs of viable random coordinates
random_location = random.choice(viable_points_list)
# enemy
circle_enemy = pg.draw.circle(screen, "red2", random_location, radius=radius, width=0)

# def enemy_circle(screen2=screen,x2=10, y2=10, color2="blue", radius2=10, width2=0, speed2=2):
#     screen2
#     circle_2 = pg.draw.circle(screen, color2, (x2, y2), radius=radius, width=0)

# random_location_x = random.randint(0, SCREEN_WIDTH - 1)  # this is a start
screen_AREA = SCREEN_WIDTH * SCREEN_HEIGHT

# Screen_Perimiter = 2 * (SCREEN_WIDTH + SCREEN_HEIGHT)

# random_location = random.choice(0, screen_AREA)


run = True

while run:
    keys = pg.key.get_pressed()
    screen.fill("black")
    pg.draw.rect(screen, "green2", border_normal_state, border_normal_state_width)
    circle = pg.draw.circle(screen, "green", (x, y), radius=radius, width=0)

    # if random_location >= SCREEN_WIDTH:
    #     x_m = random_location - (SCREEN_WIDTH/2)
    #     circle_enemy = pg.draw.circle(screen, "red2", (x_m, x_m), radius=radius, width=0)
    # if random_location >= SCREEN_HEIGHT:
    #     y_m = random_location - (SCREEN_HEIGHT/2)
    # if not circle_enemy in screen_AREA:
    circle_enemy = pg.draw.circle(screen, "red2", random_location, radius=radius, width=0)

    for event in pg.event.get():
        if event.type == pg.QUIT:  # What's the diffirence between pg.QUIT()[object of QUIT] & pg.QUIT[newstyle class]??
            run = False

    # if

    if keys[pg.K_w]:
        y -= speed * dt
    if keys[pg.K_s]:
        y += speed * dt
    if keys[pg.K_a]:
        x -= speed * dt
    if keys[pg.K_d]:
        x += speed * dt
    if keys[pg.K_ESCAPE]:
        run = False
    if keys[pg.K_LSHIFT]:
        if keys[pg.K_a]:
            x -= speed * dt * 4
        if keys[pg.K_d]:
            x += speed * dt * 4
        if keys[pg.K_w]:
            y -= speed * dt * 4
        if keys[pg.K_s]:
            y += speed * dt * 4
    if keys[pg.K_e]:
        pg.draw.rect(surface=screen, color="lightsalmon", rect=inventor_screen, width=0)
        # pg.Surface.blit(source=inventory_screen, dest=screen)
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
    dt = clock.tick(300) / 1000

pg.quit()
