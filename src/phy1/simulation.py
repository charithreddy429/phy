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
        self.objects.append(WallSet([
            Wall(self.app.surf, 0, 0, self.boundary[0], 0),
            Wall(self.app.surf, self.boundary[0], 0, *self.boundary),
            Wall(self.app.surf, *self.boundary, 0, self.boundary[1]),
            Wall(self.app.surf, 0, self.boundary[1], 0, 0)

        ]))
        self.objects.append(BallSet(
            [Ball(self.app.surf, 20 + 30 * i, 20 + 30 * j, utils.vector_with_magnitude(100))
             for i in range(20) for j in range(20)]))

    def update(self, dt):
        dt = 1 / 60
        for i in self.objects:
            i.update(dt)
        for i in range(len(self.objects)):
            for j in range(len(self.objects)):
                if i != j:
                    self.objects[i].interact(self.objects[j])

    def draw(self):
        for i in self.objects:
            i.draw()
