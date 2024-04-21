from typing import List

import pygame as p

import utils
from ball import Ball
import numpy as np


class Spring:
    def __init__(self, b1: Ball, b2: Ball,surf, k=100, k2=1, l=None):
        self.ball1 = b1
        self.ball2 = b2
        self.surf = surf
        if l is None:
            self.length = np.linalg.norm(self.ball2.position - self.ball1.position)
        else:
            self.length = l
        self.k = k
        self.k2 = k2
        self.damping = 0.8

    def draw(self):
        p.draw.line(self.surf, (0, 0, 0), utils.totu(self.ball1.position), utils.totu(self.ball2.position), 1)

    def update(self,dt):
        dist = np.linalg.norm(r := (self.ball2.position - self.ball1.position))
        force = (self.k * (dist - self.length) * (
                self.ball1.position - self.ball2.position) / dist +
                 self.k2 * r * np.dot(r, self.ball1.velocity - self.ball2.velocity) / dist ** 2)
        self.ball2.force += force
        self.ball1.force -= force

    # def draw(self):
    #     p.draw.line(self.surf,(255,255,255),self.ball1.position.astype(int),
    #                 self.ball2.position.astype(int),20)


class SpringSet:
    def __init__(self, springs: List[Spring]):
        self.springs = springs

    def update(self,dt):
        for i in self.springs:
            i.update(dt)

    def draw(self):
        for i in self.springs:
            i.draw()
    def interact(self,a,b):
        pass