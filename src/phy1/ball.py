import utils
import numpy as np
import random
import pygame as p
from typing import List
from math import floor


class Ball:
    elasticity = 1

    def __init__(self, surf: p.Surface, x: float, y: float, velocity,
                 radius=10,color = None,mass=1):
        self.position = np.float64([x, y])
        self.velocity = velocity  # type: ignore
        self.radius = radius
        self.force = np.float64([0.0, 0.0])  # type: ignore
        self.mass = mass
        self.path = []
        self.surf = surf
        if color is not None:
            self.color =   color
        else:
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    def update(self, dt):

        # self.path.append(self.position.astype(np.int64))  # type: ignore
        if len(self.path) > 500:
            self.path.pop(0)

        self.velocity = self.velocity + self.force * dt / self.mass
        self.force = 0
        self.position += self.velocity * dt

    def draw(self):
        p.draw.circle(self.surf, self.color, self.position, self.radius)

    @staticmethod
    def collide(a, b: 'Ball') -> None:
        distance = np.linalg.norm(a.position - b.position)
        if distance <= a.radius + b.radius:
            # Calculate collision normal
            collision_normal = (b.position - a.position) / distance

            # Calculate relative velocity
            relative_velocity = a.velocity - b.velocity

            # Calculate relative velocity along the collision normal
            relative_velocity_normal = np.dot(relative_velocity, collision_normal)

            # If relative velocity along normal is positive, balls are moving apart
            if relative_velocity_normal < 0:
                return

            # Calculate impulse (change in velocity) with elasticity
            impulse = (-(1 + Ball.elasticity) * relative_velocity_normal) / (a.mass + b.mass) * collision_normal

            # Update velocities
            print(impulse)
            a.velocity += impulse / a.mass
            b.velocity -= impulse / b.mass
            a.position -= collision_normal * (a.radius + b.radius - distance) / 2
            b.position += collision_normal * (a.radius + b.radius - distance) / 2

    @staticmethod
    def gravity(balls: List['Ball'], k=1e5):
        for i in range(len(balls)):
            for j in range(len(balls)):
                if i > j:

                    r = balls[i].position - balls[j].position  # type: ignore
                    # force = r*( k/((np.dot(r, r)-500) ** (3 / 2)) -k/ (np.dot(r, r) ** (3 / 2)))
                    force = r*k/(np.dot(r, r)**(3/2))
                    l= 1e4
                    f = np.dot(force, force)
                    if f > l:
                        force = -force / f
                    balls[j].force += force
                    balls[i].force -= force

    def collide_wall(self, normal: np.ndarray, df=1) -> None:
        self.velocity -= (2 * np.dot(self.velocity, normal) * normal)
        self.velocity *= df


class BallSet:
    def __init__(self, balls: list[Ball],boundary):
        self.balls = balls
        self.ke = 0
        self.gridSize = balls[0].radius
        self.gridDim = (-(-boundary[0]//self.gridSize), -(-boundary[1]//self.gridSize))

    def update(self, dt):
        self.ke = 0

        grid: list[list[int]] = [[] for i in range(self.gridDim[0] * self.gridDim[1])]

        for ind, i in enumerate(self.balls):
            i.update(dt)

            self.ke += np.dot(i.velocity, i.velocity)
            n = floor(max(min(i.position[0] // self.gridSize, self.gridDim[0]), 0) +
                             max(min(i.position[1] // self.gridSize, self.gridDim[1]), 0) * self.gridDim[0])
            grid[n].append(ind)

        for i in range(self.gridDim[0] * self.gridDim[1]):
            if not (grid[i]):
               continue
            for j in [0, 1, -1, self.gridDim[0], -self.gridDim[0], 1 + self.gridDim[0], -1 + self.gridDim[0],


                      1 - self.gridDim[0], -1 - self.gridDim[0]]:
                if 0 <= i + j < self.gridDim[0]*self.gridDim[1]:
                    self.cocell(grid[i], grid[i + j])

    def cocell(self, s, b):
        for i in s:
            for j in b:
                if i != j:
                    Ball.collide(self.balls[i], self.balls[j])

    def draw(self):
        for i in self.balls:
            i.draw()
        utils.debug(self.ke)

    def interact(self, p,f):
        pass
