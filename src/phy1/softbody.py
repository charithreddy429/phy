import pygame as p
import math
import utils
import spring
import ball


class SoftBody:
    def __init__(self, balls: list[ball.Ball], springs: list[spring.Spring], surf: p.Surface):
        self.balls = balls
        self.springs = springs
        self.surf = surf

    def update(self, dt):
        for i in self.balls:
            i.update(dt)
        for j in self.springs:
            j.update()

    def draw(self):
        for i in self.balls:
            i.draw()

        for i in self.springs:
            i.draw(self.surf)

    def interact(self, *_):
        pass


class CircleS(SoftBody):

    def __init__(self, surf, center, velocity, radius, nodes):
        x = [ball.Ball(surf, center[0], center[1], velocity, 10, (0, 0, 0))]
        x[0].mass = 1e2
        s = []
        for i in range(nodes * 4):
            x.append(ball.Ball(surf, center[0] + radius * math.sin(math.pi * i / (2 * nodes)),
                               center[1] + radius * math.cos(math.pi * i / (2 * nodes)), velocity, 1, (0, 0, 0)))
        for i in range(1, nodes * 4 + 1):
            s.append(spring.Spring(x[0], x[i], 100))

        for i in range(1, nodes * 4 + 1):
            if i == 4 * nodes:
                s.append(spring.Spring(x[i], x[1], 2000, 1))
                continue
            s.append(spring.Spring(x[i], x[(i + 1)], 2000, 1))
        super().__init__(x, s, surf)

    def draw(self):
        super().draw()
        utils.polyc(self.surf, utils.totu(self.balls[0].position), [utils.totu(i.position) for i in self.balls[1::]],
                    (100, 100, 255))
        (l, a) = utils.is_clockwise([utils.totu(i.position) for i in self.balls[1::]][::-1],
                                    utils.totu(self.balls[0].position))

        utils.debug(
            str(l),
            10, 10, self.surf)

        del l
        # for i in self.balls:
        #     i.draw()
        # for i in self.springs:
        #     i.draw(self.surf)


class Circle2(SoftBody):
    def __init__(self, surf, center, velocity, radius, nodes, ):

        x = [ball.Ball(surf, center[0], center[1], velocity, 10, (0, 0, 0))]
        x[0].mass = 10
        s = []
        for i in range(nodes * 4):

            x.append(ball.Ball(surf, center[0] + radius / 2 * math.sin(math.pi  / (4 * nodes)+math.pi * i / (2 * nodes)),
                               center[1] + radius / 2 * math.cos(math.pi  / (4 * nodes)+math.pi * i / (2 * nodes)), velocity, 1, (0, 0, 0),1))
        for i in range(1, nodes * 4 + 1):
            s.append(spring.Spring(x[0], x[i], 10000))
        for i in range(nodes * 4):
            x.append(ball.Ball(surf, center[0] + radius * math.sin(math.pi * i / (2 * nodes)),
                               center[1] + radius * math.cos(math.pi * i / (2 * nodes)), velocity, 1, (0, 0, 0),100))

        for i in range(1, nodes * 8 + 1):
            if i == 4 * nodes:
                s.append(spring.Spring(x[i], x[1], 20000, 1))
                continue
            if i == 8 * nodes:
                s.append(spring.Spring(x[i], x[1 + 4 * nodes], 20000, 1))
                continue
            if i <=4*nodes:
                s.append(spring.Spring(x[i], x[(i + 1)], 10000, 1))
            else:
                s.append(spring.Spring(x[i], x[(i + 1)], 20000, 1))
        for i in range(1, nodes * 4 + 1):
            s.append(spring.Spring(x[i], x[(i + 4 * nodes)], 10000, 1))
            if i == 4 * nodes:
                s.append(spring.Spring(x[i], x[(i + 1)], 10000, 1))
                continue
            s.append(spring.Spring(x[i], x[(i + 4 * nodes + 1)], 10000, 1))
        super().__init__(x, s, surf)

    def draw(self):
        super().draw()
        # utils.polyc(self.surf, utils.totu(self.balls[0].position), [utils.totu(i.position) for i in self.balls[1::]],
        #             (100, 100, 255))
        # (l, a) = utils.is_clockwise([utils.totu(i.position) for i in self.balls[1::]][::-1],
        #                             utils.totu(self.balls[0].position))
