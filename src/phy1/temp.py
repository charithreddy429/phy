# import pygame
# import math
#
# def interpolate(from_value, to_value, percent):
#     difference = to_value - from_value
#     return from_value + (difference * percent)
#
# def bezier_curve(control_points, num_segments=100):
#     curve_points = []
#     for i in range(num_segments):
#         t = i / num_segments
#         xa = interpolate(control_points[0][0], control_points[1][0], t)
#         ya = interpolate(control_points[0][1], control_points[1][1], t)
#         xb = interpolate(control_points[1][0], control_points[2][0], t)
#         yb = interpolate(control_points[1][1], control_points[2][1], t)
#         x = interpolate(xa, xb, t)
#         y = interpolate(ya, yb, t)
#         curve_points.append((int(x), int(y)))
#     return curve_points
#
# # Example usage:
# control_points = [(100, 100), (200, 300), (400, 100)]  # Control points for the Bézier curve
#
# # Initialize Pygame
# pygame.init()
#
# # Set up the display
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
#
# # Define colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
#
# # Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Clear the screen
#     screen.fill(WHITE)
#
#     # Draw control points
#     for point in control_points:
#         pygame.draw.circle(screen, BLACK, point, 5)
#
#     # Draw Bézier curve
#     curve_points = bezier_curve(control_points)
#     pygame.draw.lines(screen, RED, False, curve_points, 2)
#
#     # Update the display
#     pygame.display.flip()
#
# # Quit Pygame
# pygame.quit()

