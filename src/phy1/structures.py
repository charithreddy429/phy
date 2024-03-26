import numpy as np
import pygame


class Circle:
    def __init__(self, position: np.ndarray, radius: float = 50):
        self.radius = radius
        self.position = position

    def normal(self, point: np.ndarray):
        n = (self.position - point)
        return n / np.linalg.norm(n)

    def draw(self, surf: pygame.Surface):
        pygame.draw.circle(surf, (255, 255, 255), self.position.astype(np.int64), self.radius, 1)
