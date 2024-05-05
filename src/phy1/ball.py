import utils
import numpy as np
import random
import pygame as p
from typing import List
from math import floor

import time


# while True:
#     x.fill((23,23,54))
#     p.draw.circle(x,(23,23,23),(50,550),12)
#     x.blit(circle,(20,20))
#     # time.sleep(0.01)
#     for event in p.event.get():
#         if event.type == p.QUIT or (event.type == p.KEYDOWN and event.key == p.K_ESCAPE):
#             p.quit()
#     p.display.update()

class Ball:
    elasticity = 1
    r = 30
    circle = p.Surface((2 * r, 2 * r), p.SRCALPHA)
    p.draw.circle(circle, (20 + 10, 20 + 10, 20 * 3), (r, r), int(r * 20 / 20))
    p.draw.circle(circle, (25 + 10, 25 + 10, 25 * 3), (r, r), int(r * 17 / 20))
    p.draw.circle(circle, (30 + 10, 30 + 10, 30 * 3), (r, r), int(r * 15 / 20))
    p.draw.circle(circle, (40 + 10, 40 + 10, 40 * 3), (r, r), int(r * 13 / 20))
    circle.convert_alpha()
    x = p.display.get_surface()

    def __init__(self, surf: p.Surface, x: float, y: float, velocity,
                 radius=10, color=None, mass=1):
        self.position = np.float64([x, y])
        self.lposition = np.float64([x, y]) - velocity
        self.radius = radius
        self.force = np.float64([0.0, 0.0])  # type: ignore
        self.mass = mass
        self.path = []
        self.surf = surf

        if color is not None:
            self.color = color
        else:
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def getvel(self):
        return (self.position - self.lposition)

    def setvel(self, v):
        self.lposition = self.position - v

    def addvel(self, v):
        self.lposition -= v

    def update(self, dt):

        # if len(self.path) > 5000:
        #     self.path.pop(0)
        # self.path.append(self.position.copy())
        self.force = 0

        self.position, self.lposition = (2 * self.position - self.lposition), self.position

    def draw(self):
        # circle.set_alpha(255)

        p.draw.circle(self.surf, self.color, self.position, self.radius)
        # self.surf.blit(self.circle, (int(self.position[0] - self.r), int(self.position[1] -self.r)),special_flags=1)

    @staticmethod
    def collide(a, b: 'Ball') -> None:
        distance = np.linalg.norm(a.position - b.position)
        if distance <= a.radius + b.radius:

            collision_normal = (b.position - a.position) / distance
            relative_velocity = a.getvel() - b.getvel()
            relative_velocity_normal = np.dot(relative_velocity, collision_normal)

            if relative_velocity_normal < 0:
                return

            # impulse = (-(1 + Ball.elasticity) * relative_velocity_normal) / (a.mass + b.mass) * collision_normal

            # a.addvel(+impulse / a.mass)
            # b.addvel(-impulse / b.mass)
            a.position -= collision_normal*(3/4) * (a.radius + b.radius - distance) / 2
            b.position += collision_normal*(3/4) * (a.radius + b.radius - distance) / 2

    def collide_wall(self, normal: np.ndarray, df=1) -> None:
        self.velocity -= (2 * np.dot(self.velocity, normal) * normal)
        self.velocity *= df


class BallSet:
    def __init__(self, balls: list[Ball], boundary, coll=True):
        self.balls = balls
        self.ke = 0
        self.nd = set()
        self.gridSize = balls[0].radius
        self.boundary = boundary
        self.gridDim = (-(-boundary[0] // self.gridSize), -(-boundary[1] // self.gridSize))
        self.collision = coll

    def update(self, dt, frame, *k):
        if len(self.balls) == 0:
            return -1
        self.ke = 0

        grid: list[list[int]] = [[] for i in range(self.gridDim[0] * self.gridDim[1])]

        for ind, i in enumerate(self.balls):
            i.update(dt)
        if self.collision:
            for ind, i in enumerate(self.balls):
                self.ke += np.dot(i.getvel(), i.getvel())
                # i.position[0] = utils.clange(i.position[0], 10, self.boundary[0] - 10)
                # i.position[1] = utils.clange(i.position[1], 10, self.boundary[1] - 10)
                n = floor(max(min(i.position[0] // self.gridSize, self.gridDim[0]), 0) +
                          max(min(i.position[1] // self.gridSize, self.gridDim[1]), 0) * self.gridDim[0])
                grid[n].append(ind)

            for i in range(self.gridDim[0] * self.gridDim[1]):
                if not (grid[i]):
                    continue
                for j in [0, 1, -1, self.gridDim[0], -self.gridDim[0], 1 + self.gridDim[0], -1 + self.gridDim[0],

                          1 - self.gridDim[0], -1 - self.gridDim[0]]:
                    if 0 <= i + j < self.gridDim[0] * self.gridDim[1]:
                        self.cocell(grid[i], grid[i + j])

    def cocell(self, s, b):
        for i in s:
            for j in b:
                if i != j:
                    Ball.collide(self.balls[i], self.balls[j])

    def draw(self):
        for i in self.balls:
            i.draw()
        utils.debug(self.ke,100,10,self.balls[0].surf)

    def interact(self, p, f):
        pass
