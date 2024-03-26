import numpy as np
import random
import pygame as p
import ball


class Wall:
    elasticity = 1

    def __init__(self, surf: p.Surface, x1: float, y1: float, x2, y2,
                 thickness=5,
                 color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))):
        self.stPosition = np.float64([x1, y1, 0])
        self.edPosition = np.float64([x2, y2, 0])
        self.color = color
        self.thickness = thickness
        self.surf = surf

    def draw(self):
        p.draw.line(self.surf, self.color, self.stPosition[0:2], self.edPosition[0:2], self.thickness)

    def update(self,dt):
        pass

    def interact(self, b: ball.Ball):

        # Calculate the vector representing the wall
        wall_vector = self.edPosition - self.stPosition

        # Calculate the normalized normal vector of the wall
        wall_normal = np.array([-wall_vector[1], wall_vector[0]])

        # Normalize the wall_normal vector
        wall_normal /= np.linalg.norm(wall_normal)

        # Calculate the vector from the start of the wall to the ball
        wall_to_ball = b.position - self.stPosition

        # Calculate the perpendicular distance between the wall and the ball
        perpendicular_distance = np.dot(wall_to_ball[0:2], wall_normal)

        # If the perpendicular distance is less than the radius of the ball,
        # then there is a collision
        if abs(perpendicular_distance) <= b.radius:
            # Calculate the relative velocity between the ball and the wall
            relative_velocity = np.dot(b.velocity[0:2], wall_normal[0:2])
            penetration_depth = b.radius - abs(perpendicular_distance)

            # Move the ball out of the wall along the normal vector
            b.position[0:2] += penetration_depth * wall_normal
            # If the relative velocity is positive, the ball is moving away from the wall
            # and no collision response is needed
            if relative_velocity > 0:
                return

            # Calculate the impulse magnitude
            impulse_magnitude = -(1 + self.elasticity) * relative_velocity

            # Calculate the impulse
            impulse = impulse_magnitude * wall_normal

            # Apply the impulse to the ball
            b.velocity[0:2]+= impulse
            b.position

class WallSet:
    def __init__(self, walls: list[Wall]):
        self.walls = walls

    def update(self,dt):
        for i in self.walls:
            i.update(dt)

    def draw(self):
        for i in self.walls:
            i.draw()

    def interact(self, b: ball.BallSet):
        for i in self.walls:
            for j in b.balls:
                i.interact(j)
