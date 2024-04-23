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


class Simulation:
    def __init__(self, app, boundary: list[int, int], *func):
        self.app = app
        self.objects: List[BallSet | WallSet | SpringSet | softbody.SoftBody | RecSet] = []
        self.boundary = np.array(boundary)

        # self.ball = Ball(self.app.surf, *np.float64([640.0, 600.0]), np.float64([2000, 0]),
        #                  10, color=(0,0,0))
        # self.objects.append(BallSet([self.ball], self.boundary))
        # self.objects[0].balls.pop()
        def f(x, y, vec, n):
            # self.objects.append(
            #     BallSet(
            #         [Ball(self.app.surf, x, y, utils.vector_with_magnitude(100 * (random.random() + 1), vec),
            #               color=(255, 223, 224), radius=3) for _ in range(n)], boundary))
            func[0].play()

        # self.setupboundary()

        # self.objects.append(WallSet([CircularWall(self.app.surf,(self.boundary/2).astype(int),int(min(self.boundary)*0.45),f,int(min(self.boundary)*0.025))]))
        # self.circle = p.Surface((40, 40), p.SRCALPHA)
        # p.draw.circle(self.circle, (255, 255, 255), (20, 20), 20)
        # self.circle.convert_alpha()
        # print(self.circle)
        # self.objects.append(WallSet([CircularWall(self.app.surf,self.boundary/2,min(boundary)/2,f)]))
        # self.addrandomballs()
        self.addconrec(16)
        # self.objects[-1].recs[0].velocity = np.float64([100,173])

        self.objects[-1].recs[-1].mass = 1
        self.objects[-1].recs[-1].lpos = self.objects[-1].recs[-1].position
        # self.objects[-1].recs[1].velocity = np.float64([-100,-173])
        self.setupboundary()

    def addconcir(self, f):
        self.objects.append(
            WallSet([walls.CircularWall(self.app.surf, np.array([640, 360]), 50 * i, f, elasticity=1.05,
                                        color=colors[i - 1])
                     for i in range(1, 8)]))

    def addconrec(self, n):
        self.objects.append(RecSet(
            [Rec(self.app.surf, self.boundary / 2 + np.float64([10 * (n - i) - 20 * n,11.25 * (n - i) - 22.5 * n]), velocity=np.float64([15 * (n-i)/480, 15 * (n-i)/480]),
                 wh=(40 * i, 45 * i)) for i in range(1, n)]
        ))

    def cirargbal(self, radius, velocity, n, radiusp=10):
        # self.objects.append(BallSet([*self.cirargbal(200,-200,40),*self.cirargbal(100,100,20),*self.cirargbal(40,-40,8)]))

        return [Ball(self.app.surf, 640 + radius * math.sin(i / n * math.pi * 2),
                     360 + radius * math.cos(i / n * math.pi * 2),
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
            [Ball(self.app.surf, 10 + 31 * i, 10 + 25 * j, utils.vector_with_magnitude(100))
             for i in range(41) for j in range(28)], self.boundary))

    def update(self, dt, frame):
        rad = 10
        dt = 1 / 128
        for ind,i in enumerate(self.objects[0].recs):
            i.color = utils.rclr((frame-ind*24)/60)
        x, y = p.mouse.get_pos()
        # self.objects[0].recs[0].position = self.boundary[0]*(y/720),self.boundary[1]*(1-x/405)-30
        # if frame<500:
        #     self.objects[0].balls.append(Ball(self.app.surf,360,360.0,utils.vector_with_magnitude(1000,np.float64([1,0])),rad,(0,0,0)))
        #     self.objects[0].balls.append(Ball(self.app.surf,1280-360.0,360,utils.vector_with_magnitude(1000,np.float64([-1,0])),rad,(255,255,255)))
        # elif frame<15000:

        # for i in self.ball.path:
        #     self.app.surf.blit(self.circle, (int(i[0]), int(i[1])))
        # x: List[Ball] = []
        # for i in self.objects:
        #     if isinstance(i, BallSet):
        #         x.extend(i.balls)
        #
        # gravity = np.float64([1000, 0])
        # for i in x:
        #     i.force += gravity

        # for i in range(l:=len(x)):
        #     for j in range(l):
        #         if i>j:
        #             Ball.collide(x[i],x[j])
        # Ball.gravity(x)
        # self.objects[0].balls[0].velocity += np.array([-600, 0]) * dt
        # if 1 < len(self.objects[1].walls):
        #     if self.objects[1].walls[0].radius > self.objects[1].walls[1].radius - 6:
        #         self.objects[1].walls.pop(0)
        #
        for i in self.objects:
            if i.update(dt) == -1:
                self.objects.remove(i)
        for i in range(len(self.objects)):
            for j in range(len(self.objects)):
                if i != j:
                    self.objects[i].interact(self.objects[j], frame)

    def draw(self):
        # n = self.objects[0].balls[0].path
        # for ind, i in enumerate(n):
        #     # self.setalp(int(255 * (1 - ind / len(n)))*0)
        #     self.circle.set_alpha(int(255 * (ind / len(n))))
        #     self.app.surf.blit(self.circle, (int(i[0] - 20), int(i[1] - 20)))
        # for j in self.objects[1].balls:
        #     if len(j.path) > 1:
        #         for i in range(len(j.path) - 1):
        #             p.draw.line(self.app.surf, (255, 255, 255), j.path[i], j.path[i + 1], 2)

        for i in self.objects:
            i.draw()
