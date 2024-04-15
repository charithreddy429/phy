import pygame as p

import utils
from ball import Ball
import numpy as np


class Spring:
    def __init__(self, b1: Ball, b2: Ball,k=None,k2=None, l=None):
        self.ball1 = b1
        self.ball2 = b2
        if l is None:
            self.length = np.linalg.norm(self.ball2.position - self.ball1.position)
        else:
            self.length = l
        if k is None:
            self.k = 100
        else:
            self.k = k
        if k2 is None:
            self.k2 = 1
        else:
            self.k2 = k2
        self.damping = 0.8
    def draw(self,surf):
        p.draw.line(surf,(0,0,0),utils.totu(self.ball1.position),utils.totu(self.ball2.position),1)

    def update(self):
        dist = np.linalg.norm(r := (self.ball2.position - self.ball1.position))
        force = (self.k * (dist - self.length) * (
                    self.ball1.position - self.ball2.position) / dist +
                 self.k2 * r * np.dot(r,self.ball1.velocity - self.ball2.velocity) / dist ** 2)
        self.ball2.force += force
        self.ball1.force -= force
