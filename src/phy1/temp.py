import pygame
import numpy as np
from scipy.interpolate import CubicSpline

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Soft Body Visualization")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define data points
points = np.array([[100, 200],
                   [200, 300],
                   [300, 250],
                   [400, 350],
                   [500, 200]])

# Compute the cubic spline interpolation
x = points[:, 0]
y = points[:, 1]
cs = CubicSpline(x, y)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw original data points
    for point in points:
        pygame.draw.circle(screen, BLACK, (int(point[0]), int(point[1])), 5)

    # Draw the interpolated curve
    t = np.linspace(0, len(points) - 1, 100)
    curve_points = np.column_stack((cs(t),)).astype(int)

    # Check if curve_points has more than one column
    print(curve_points)
    curve_points = [(point[0], point[1]) for point in curve_points[:,0]]  # Convert to list of (x, y) tuples
    pygame.draw.lines(screen, RED, False, curve_points, 10)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
