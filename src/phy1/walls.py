import numpy as np
import random
import pygame as p
import ball
import utils


class Wall:
    elasticity = 1

    def __init__(self, surf: p.Surface, x1: float, y1: float, x2, y2,
                 thickness=5,
                 color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))):
        self.stPosition = np.float64([x1, y1])
        self.edPosition = np.float64([x2, y2])
        self.color = color
        self.thickness = thickness
        self.surf = surf

    def draw(self):
        p.draw.line(self.surf, self.color, self.stPosition, self.edPosition, self.thickness)

    def update(self, dt):
        pass

    def interact(self, b: ball.Ball, frame):

        # Calculate the vector representing the wall
        wall_vector = self.edPosition - self.stPosition

        # Calculate the normalized normal vector of the wall
        wall_normal = np.array([-wall_vector[1], wall_vector[0]])

        # Normalize the wall_normal vector
        wall_normal /= np.linalg.norm(wall_normal)

        # Calculate the vector from the start of the wall to the ball
        wall_to_ball = b.position - self.stPosition

        # Calculate the perpendicular distance between the wall and the ball
        perpendicular_distance = np.dot(wall_to_ball, wall_normal)

        # If the perpendicular distance is less than the radius of the ball,
        # then there is a collision
        if abs(perpendicular_distance) <= b.radius:
            # Calculate the relative velocity between the ball and the wall
            relative_velocity = np.dot(b.velocity, wall_normal)
            penetration_depth = b.radius - abs(perpendicular_distance)

            # Move the ball out of the wall along the normal vector
            b.position += penetration_depth * wall_normal
            # If the relative velocity is positive, the ball is moving away from the wall
            # and no collision response is needed
            if relative_velocity > 0:
                return

            # Calculate the impulse magnitude
            impulse_magnitude = -(1 + self.elasticity) * relative_velocity

            # Calculate the impulse
            impulse = impulse_magnitude * wall_normal

            # Apply the impulse to the ball
            b.velocity += impulse


class CircularWall:
    elasticity = 1.1

    def __init__(self, surf: p.Surface, center: np.ndarray, radius: float, func,
                 thickness=10,
                 color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))):
        self.center = np.float64(center)
        self.radius = radius
        self.color = color
        self.thickness = thickness
        self.surf = surf
        self.func = func

    def draw(self):
        p.draw.circle(self.surf, self.color, self.center.astype(int), self.radius + self.thickness / 2, self.thickness)

    def update(self, dt):
        pass

    def interact(self, b: ball.Ball, frame):
        # Calculate the vector from the center of the circle to the ball
        center_to_ball = b.position - self.center

        # Calculate the distance between the center of the circle and the ball
        distance_to_center = np.linalg.norm(center_to_ball[0:2])

        # print("Distance to center:", distance_to_center)
        # print("Sum of radii:", self.radius + b.radius)

        # If the distance is less than or equal to the radius of the circle,
        # then there is a collision
        if distance_to_center >= self.radius - b.radius:
            # Calculate the normalized normal vector pointing from the circle center to the ball
            normal_vector = center_to_ball / distance_to_center

            # Calculate the relative velocity between the ball and the circle
            relative_velocity = np.dot(b.velocity[0:2], normal_vector)

            # If the relative velocity is positive, the ball is moving away from the circle
            # and no collision response is needed
            if relative_velocity < 0:
                return

            # time.sleep(0.1)
            # Calculate the impulse magnitude
            impulse_magnitude = -(1 + self.elasticity) * relative_velocity

            # Calculate the impulse
            # assert isinstance(normal_vector, np.float64)
            impulse = impulse_magnitude * normal_vector

            b.position -= normal_vector * (distance_to_center + b.radius - self.radius)
            if b.color == (255, 223, 224):
                return -1
            else:
                print(frame)
                utils.append_to_file('g1.txt', str(frame))
                self.func(b.position[0], b.position[1], -normal_vector, 10)
            # Apply the impulse to the ball
            b.velocity += impulse
            self.radius += 5
            # b.radius += 2
            # utils.append_to_file('g.txt',str(frame))


class WallSet:
    def __init__(self, walls: list[Wall | CircularWall]):
        self.walls = walls

    def update(self, dt):
        for i in self.walls:
            i.update(dt)

    def draw(self):
        for i in self.walls:
            i.draw()

    def interact(self, b: ball.BallSet, frame):
        for i in self.walls:
            if isinstance(i, ball.BallSet):
                for j in b.balls:
                    if i.interact(j, frame) == -1:
                        b.balls.remove(j)
