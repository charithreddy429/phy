import numpy as np
import pygame as p
import math
import cvrec
import utils
from math import sin, cos

out = cvrec.get_out(utils.generate_file_name(r"output\vid", "", "mp4"), 30, (720, 1280))
# Initialize p
p.init()

# Set up the screen
screen_width = 405 + 10
screen_height = 720 + 10
screen = p.display.set_mode((screen_width, screen_height))
win = p.Surface((1280, 720))
p.display.set_caption("Circle with evenly spaced points")
circle = p.Surface((80, 80), p.SRCALPHA)
p.draw.circle(circle, (20, 20+15, 20), (40, 40), 20*2)
p.draw.circle(circle, (20, 20+15, 20), (40, 40), 20*2)
p.draw.circle(circle, (25, 25+15, 25), (40, 40), 17*2)
p.draw.circle(circle, (30, 30+15, 30), (40, 40), 15*2)
p.draw.circle(circle, (40, 40+15, 40), (40, 40), 13*2)
circle.convert_alpha()
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
colors = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (128, 0, 128),  # Purple
    (255, 165, 0),  # Orange
    (255, 192, 203),  # Pink
    (0, 128, 0),  # Dark Green
    (0, 0, 128),  # Dark Blue
    (128, 128, 0)  # Olive
]


class circ:
    def __init__(self, radius, dist, center, angle, omega):
        self.radius = radius
        self.dist = dist
        self.center = center
        self.angle = angle
        self.omega = omega

    def update(self, dt):
        self.angle += self.omega * dt

    def draw(self, surf, color,hs):
        if hs:
            p.draw.circle(surf,(120,120,0),self.center,self.dist,5)
        p.draw.circle(surf, color, self.center + self.dist * np.float64([sin(self.angle), cos(self.angle)]),
                      self.radius)
        surf.blit(circle,self.center + self.dist * np.float64([sin(self.angle), cos(self.angle)]) - 40,special_flags=1)
circs = [circ(20, 50 * i, (640, 360), 0, math.pi * i) for i in range(1, 7)]
fps = 150
running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    win.fill((128, 128, 0))
    for ind,i  in enumerate(circs):
        i.update(1 / fps)
        i.draw(win,WHITE,1)
    p.draw.circle(screen, WHITE, (50, 50), 10)
    # print(len(p.surfarray.array3d(win)))
    out.write(p.surfarray.array3d(win))
    screen.blit(p.transform.rotozoom(win, -90, 405 / 720), (0, 0))
    p.display.update()
p.quit()
