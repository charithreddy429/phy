import numpy as np
import softbody
import walls
from settings import *
import math
from ball import *
from walls import *
import utils


class Simulation:
    def __init__(self, app, boundary: list[int, int]):
        self.app = app
        self.objects = []
        self.boundary = boundary
        self.objects.append(softbody.Softbody.circle(self.app.surf,np.float64(boundary)/2+np.float64([-100,0])*4.5,np.float64([-100,0]),100,100)
                            )# self.objects.append(
        #     BallSet(
        #
        #         [Ball(app.surf, 640 + 40 * math.sin(i / 8 * math.pi * 2), 360 + 40 * math.cos(i / 8 * math.pi * 2),
        #               np.float64([80000 * math.cos(i / 8 * math.pi * 2), -80000 * math.sin(i / 8 * math.pi * 2)]), 10,
        #               (255, 0, 0)) for i in range(8)
        #          ]
        #
        #     )
        # )
        # self.objects.append(WallSet([walls.CircularWall(app.surf, np.array([640, 360]), 300)]))
        # self.addrandomballs()
        self.setupboundary()

    def setupboundary(self):
        self.objects.append(WallSet([
            Wall(self.app.surf, 0, 0, self.boundary[0], 0),
            Wall(self.app.surf, self.boundary[0], 0, *self.boundary),
            Wall(self.app.surf, *self.boundary, 0, self.boundary[1]),
            Wall(self.app.surf, 0, self.boundary[1], 0, 0)

        ]))

    def addrandomballs(self):
        self.objects.append(BallSet(
            [Ball(self.app.surf, 10 + 31 * i, 10 + 25 * j, utils.vector_with_magnitude(100))
             for i in range(41) for j in range(28)]))

    def update(self, dt, frame):
        dt = 1 / 60
        # x = self.objects[0].balls
        # for i in range(l:=len(x)):
        #     for j in range(l):
        #         if i>j:
        #             Ball.collide(x[i],x[j])
        # Ball.gravity(x)
        # self.objects[0].balls[0].velocity+=np.array([-600,0])*dt
        for i in self.objects:
            i.update(dt)
        for i in range(len(self.objects)):
            for j in range(len(self.objects)):
                if i != j:
                    self.objects[i].interact(self.objects[j], frame)

    def draw(self):
        for i in self.objects:
            i.draw()
