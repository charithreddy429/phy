import numpy as np
import softbody
from rec import Rec, RecSet
import walls
import math
from ball import *
from walls import *
import utils
from spring import SpringSet, Spring

colors = [

    (255, 255, 0),  # Yellow

    (255, 192, 203),  # Pink

    (0, 0, 255),  # Blue

    (0, 255, 0),  # Green

    (255, 0, 0),  # Red

    (173, 216, 230),  # Light Blue

    (255, 255, 255)  # White

]

from functools import lru_cache

@lru_cache(maxsize=None)
def arrv(n):
    return  [    np.array([math.cos(math.pi/4+math.pi * 2 / n * i), math.sin(math.pi/4+math.pi * 2 / n * i)]) for i in range(n)]


class Simulation:
    substeps = 8
    def __init__(self, app, boundary: list[int, int], number,func):
        self.app = app
        self.number = number
        self.objects: List[BallSet | WallSet | SpringSet | softbody.SoftBody | RecSet] = []
        self.boundary = np.array(boundary)
        self.addrandomballs()
        self.setupboundary()
        def colporc(x, y, vec, n):
            # self.objects.append(
            #     BallSet(
            #         [Ball(self.app.surf, x, y, utils.vector_with_magnitude(100 * (random.random() + 1), vec),
            #               color=(255, 223, 224), radius=3) for _ in range(n)], boundary))
            func[0].play()

    def addconcir(self, f):
        self.objects.append(
            WallSet([walls.CircularWall(self.app.surf, np.array([640, 360]), 50 * i, f, elasticity=1.05,
                                        color=colors[i - 1])
                     for i in range(1, 8)]))

    def addconrec(self, n):
        self.objects.append(RecSet(
            [Rec(self.app.surf, self.boundary / 2 + np.float64([10 * (n - i) - 20 * n, 11.25 * (n - i) - 22.5 * n]),
                 velocity=np.float64([15 * (n - i) / 480, 15 * (n - i) / 480]),
                 wh=(40 * i, 45 * i)) for i in range(1, n)]
        ))

    def cirargbal(self, radius, velocity, n, radiusp=10):
        # self.objects.append(BallSet([*self.cirargbal(200,-200,40),*self.cirargbal(100,100,20),*self.cirargbal(40,-40,8)]))

        return [Ball(self.app.surf, self.boundary[0] / 2 + 40 + radius * math.sin(i / n * math.pi * 2),
                     self.boundary[1] / 2 + radius * math.cos(i / n * math.pi * 2),
                     np.float64([velocity * math.cos(i / n * math.pi * 2), -velocity * math.sin(i / n * math.pi * 2)]),
                     radiusp,
                     (255, 0, 0)) for i in range(n)
                ]

    def soft(self):
        self.objects.append(softbody.Circle2(self.app.surf, np.float64(self.boundary) / 2 + np.float64([-100, 0]) * 4.5,

                                             np.float64([-100, 0]), 100, 12))

    def setupboundary(self, lc=np.float64([0, 0]), bound=None):
        if bound is None:
            bound = self.boundary
        else:
            bound = bound + lc

        self.objects.append(WallSet([
            Wall(self.app.surf, 0, 0, bound[0], 0, 5),
            Wall(self.app.surf, bound[0], 0, *bound, 5),
            Wall(self.app.surf, *bound, 0, bound[1], 5),
            Wall(self.app.surf, 0, bound[1], 0, 0, 5)
        ]))

    def addrandomballs(self):
        self.objects.append(BallSet(
            [Ball(self.app.surf, 300 + 31 * i, 300 + 25 * j, utils.vector_with_magnitude(1))
             for i in range(4 ) for j in range(4)], self.boundary))

    def update(self, dt, frame):
        for _ in range(self.substeps):
            for i in self.objects:
                if i.update(dt, frame) == -1:
                    self.objects.remove(i)
            for i in range(len(self.objects)):
                for j in range(len(self.objects)):
                    if i != j:
                        self.objects[i].interact(self.objects[j], frame)

    def draw(self):

        for i in self.objects:
            i.draw()
