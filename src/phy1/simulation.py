import numpy as np
import softbody
import walls
from settings import *
import math
from ball import *
from walls import *
import utils


class Simulation:
    def __init__(self, app, boundary: list[int, int],*func):
        self.app = app
        self.objects = []
        self.boundary = boundary
        self.objects.append(BallSet([Ball(self.app.surf, *np.float64([640.0, 360.0]), np.float64([0, 100]), 20,color=(255,255,255))],self.boundary))
        self.objects.append(WallSet([walls.CircularWall(app.surf, np.array([640, 360]), 300,func[0])]))
        # self.addrandomballs()
        self.setupboundary()

    def cirargbal(self, radius, velocity, n, radiusp=10):
        # self.objects.append(BallSet([*self.cirargbal(200,-200,40),*self.cirargbal(100,100,20),*self.cirargbal(40,-40,8)]))

        return [Ball(self.app.surf, 640 + radius * math.sin(i / n * math.pi * 2),
                     360 + radius * math.cos(i / n * math.pi * 2),
                     np.float64([velocity * math.cos(i / n * math.pi * 2), -velocity * math.sin(i / n * math.pi * 2)]),
                     radiusp,
                     (255, 0, 0)) for i in range(n)
                ]

    def soft(self):
        self.objects.append(softbody.Circle2(self.app.surf, np.float64(boundary) / 2 + np.float64([-100, 0]) * 4.5,

                                             np.float64([-100, 0]), 100, 12))

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
             for i in range(41) for j in range(28)],self.boundary))

    def update(self, dt, frame):
        dt = 1 / 60
        x: List[Ball] = self.objects[0].balls
        for i in x:
            i.force += np.float64([-1000, 0])
        # for i in range(l:=len(x)):
        #     for j in range(l):
        #         if i>j:
        #             Ball.collide(x[i],x[j])
        # Ball.gravity(x)
        # self.objects[0].balls[0].velocity += np.array([-600, 0]) * dt
        for i in self.objects:
            i.update(dt)
        for i in range(len(self.objects)):
            for j in range(len(self.objects)):
                if i != j:
                    self.objects[i].interact(self.objects[j], frame)

    def draw(self):
        for i in self.objects:
            i.draw()
