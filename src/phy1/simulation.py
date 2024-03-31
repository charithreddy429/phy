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
        self.objects.append(
            BallSet(

                [Ball(
                    app.surf,640,360,utils.vector_with_magnitude(1000),10,(255,0,0))
                 ]

                 )
                      )
        self.objects.append(WallSet([walls.CircularWall(app.surf,np.array([640,360]),300)]))

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

    def update(self, dt,frame):
        dt = 1 / 60
        self.objects[0].balls[0].velocity+=np.array([-600,0])*dt
        for i in self.objects:
            i.update(dt)
        for i in range(len(self.objects)):
            for j in range(len(self.objects)):
                if i != j:
                    self.objects[i].interact(self.objects[j],frame)

    def draw(self):
        for i in self.objects:
            i.draw()
