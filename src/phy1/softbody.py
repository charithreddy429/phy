import pygame as p
import numpy as np
import math

import pygame.draw
import utils
import spring
import ball


class Softbody:
    def __init__(self, nodes, springs, surf):
        self.balls = nodes
        self.springs = springs
        self.surf = surf

    def update(self, dt):
        for i in self.balls:
            i.update(dt)
        for j in self.springs:
            j.update()

    def interact(self, *_):
        pass

    def draw(self):
        utils.polyc(self.surf, utils.totu(self.balls[0].position), [utils.totu(i.position) for i in self.balls[1::]],
                    (100, 100, 255))
        (l,a) = utils.is_clockwise([utils.totu(i.position) for i in self.balls[1::]][::-1],
                                      utils.totu(self.balls[0].position))

        utils.debug(
            str(l),
            10, 10, self.surf)

        del l
        # for i in self.balls:
        #     i.draw()
        # for i in self.springs:
        #     i.draw(self.surf)

    @classmethod
    def circle(cls, surf, center, velocity, radius, nodes, ):
        x = [ball.Ball(surf, center[0], center[1], velocity, 10, (0, 0, 0))]
        x[0].mass = 1e2
        s = []
        for i in range(nodes * 4):
            x.append(ball.Ball(surf, center[0] + radius * math.sin(math.pi * i / (2 * nodes)),
                               center[1] + radius * math.cos(math.pi * i / (2 * nodes)), velocity, 1, (0, 0, 0)))
        for i in range(1, nodes * 4 + 1):
            s.append(spring.Spring(x[0], x[i], 100))
        print(len(s))

        for i in range(1, nodes * 4 + 1):
            if i == 4 * nodes:
                s.append(spring.Spring(x[i], x[1], 2000,1))
                continue
            s.append(spring.Spring(x[i], x[(i + 1)], 2000,1))

        return cls(x, s, surf)
