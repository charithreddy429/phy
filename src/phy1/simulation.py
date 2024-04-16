import pylab as p
import softbody
import walls
import math
from ball import *
from walls import *
import utils


class Simulation:
    def __init__(self, app, boundary: list[int, int], *func):
        self.app = app
        self.objects: List[BallSet | WallSet | softbody.SoftBody] = []
        self.boundary = boundary
        self.ball = Ball(self.app.surf, *np.float64([640.0, 320.0]), np.float64([0, 200]),
                         20, color=(255, 255, 255))
        self.objects.append(BallSet([self.ball], self.boundary))
        self.circle = p.Surface((40, 40), p.SRCALPHA)
        p.draw.circle(self.circle, (255, 255, 255), (20, 20), 20)
        self.circle.convert_alpha()
        print(self.circle)

        def f(x, y, vec, n):
            self.objects.append(
                BallSet(
                    [Ball(self.app.surf, x, y, utils.vector_with_magnitude(100 * (random.random() + 1), vec),
                          color=(255, 223, 224), radius=3) for _ in range(n)], boundary))
            func[0].play()

        # self.addrandomballs()
        self.setupboundary()

    def addconcir(self, f):
        colors = [
            (255, 255, 0),  # Yellow
            (255, 192, 203),  # Pink
            (0, 0, 255),  # Blue
            (0, 255, 0),  # Green
            (255, 0, 0),  # Red
            (173, 216, 230),  # Light Blue
            (255, 255, 255)  # White
        ]
        self.objects.append(WallSet([walls.CircularWall(self.app.surf, np.array([640, 360]), 50, f, color=colors[0]),
                                     walls.CircularWall(self.app.surf, np.array([640, 360]), 100, f, color=colors[1]),
                                     walls.CircularWall(self.app.surf, np.array([640, 360]), 150, f, color=colors[2]),
                                     walls.CircularWall(self.app.surf, np.array([640, 360]), 200, f, color=colors[3]),
                                     walls.CircularWall(self.app.surf, np.array([640, 360]), 250, f, color=colors[4]),
                                     walls.CircularWall(self.app.surf, np.array([640, 360]), 300, f, color=colors[5]),
                                     walls.CircularWall(self.app.surf, np.array([640, 360]), 350, f, color=colors[6])]))

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
             for i in range(41) for j in range(28)], self.boundary))

    def update(self, dt, frame):
        for i in self.ball.path:
            self.app.surf.blit(self.circle, (int(i[0]), int(i[1])))
        dt = 1 / 60
        x: List[Ball] = []
        for i in self.objects:
            if isinstance(i, BallSet):
                x.extend(i.balls)

        for i in x:
            i.force += np.float64([1000, 0])

        # for i in range(l:=len(x)):
        #     for j in range(l):
        #         if i>j:
        #             Ball.collide(x[i],x[j])
        # Ball.gravity(x)
        # self.objects[0].balls[0].velocity += np.array([-600, 0]) * dt

        for i in self.objects:
            if i.update(dt) == -1:
                self.objects.remove(i)
        for i in range(len(self.objects)):
            for j in range(len(self.objects)):
                if i != j:
                    self.objects[i].interact(self.objects[j], frame)

    def draw(self):
        n = self.objects[0].balls[0].path
        for ind, i in enumerate(n):
            # self.setalp(int(255 * (1 - ind / len(n)))*0)
            self.circle.set_alpha(int(255 * (ind / len(n))))
            self.app.surf.blit(self.circle, (int(i[0] - 20), int(i[1] - 20)))
        for i in self.objects:
            i.draw()
