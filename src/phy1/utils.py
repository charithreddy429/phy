import numpy as np
import random
import pygame as p

p.init()
h = width, height = 1380, 746
font = p.font.Font(None, 70)


def debug(info, x=10, y=10, surf=None):
    debug_surf = font.render(str(info), True, "red")
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    if surf is None:
        p.display.get_surface().blit(debug_surf, debug_rect)
    else:
        surf.blit(debug_surf, debug_rect)


def find_shortest_vector(coord1: np.ndarray, coord2: np.ndarray, boundary: np.ndarray) -> np.ndarray:
    # Calculate the vector components for each periodic repetition of coord2
    coord2_mod = coord2 % boundary

    periodic_coords = [(x + i * boundary[0], y + j * boundary[1])
                       for i in range(-1, 2)
                       for j in range(-1, 2)
                       for x, y in [coord2_mod]]

    # Calculate the vectors from coord1 to each periodic repetition of coord2
    vectors = np.array(periodic_coords) - coord1

    # Calculate the lengths of the vectors
    lengths = np.linalg.norm(vectors, axis=1)

    # Find the index of the shortest vector
    shortest_index = np.argmin(lengths)

    # Return the shortest vector
    return vectors[shortest_index]


def draw_circle(cord1, boundary, radius):
    """
    Draw a circle considering boundary conditions.

    Parameters:
        screen: Pygame screen surface object.
        cord1 (np.ndarray): Coordinates of the circle.
        boundary (np.ndarray): Coordinates of the boundary.
        radius (np.float64): Radius of the circle.
    """
    # Check if the circle is touching any wall and going out of the boundary
    direction = walls_circle_is_out_of(cord1, boundary, radius)
    if direction != (0, 0):
        # Adjust the coordinates based on the direction
        cord1_adj = cord1 - np.array(direction) * boundary
        return cord1_adj
    return False


def clange(a: int | float, b: int | float, c: int | float) -> int | float:
    if b <= a <= c:

        return a

    elif a < b:

        return b

    else:

        return c


def walls_circle_is_out_of(cord1: np.ndarray, boundary: np.ndarray, radius: np.float64) -> tuple[int, int]:
    """
    Identify which walls a circle with given coordinates and radius is out of.

    Parameters:
        cord1 (np.ndarray): Coordinates of the circle.
        boundary (np.ndarray): Coordinates of the boundary. Assuming the other coordinate of the boundary is (0,0).
        radius (np.float64): Radius of the circle.

    Returns:
        Tuple[int, int]: Tuple indicating the direction of the wall. First value is for vertical direction (1 for right, -1 for left),
        second value is for horizontal direction (1 for top, -1 for bottom).
        If the circle doesn't touch any wall, returns (0, 0).

    # # Example usage:
    # cord1 = np.array([3.0, 4.0], dtype=np.float64)
    # boundary = np.array([5.0, 5.0], dtype=np.float64)
    # radius = np.float64(2.0)
    #
    # print(walls_circle_is_out_of(cord1, boundary, radius))  # Output: (-1, 0) (indicating it touches the left wall)
    #
    """
    direction = (0, 0)

    # Calculate the distances to the boundaries
    distance_to_top = boundary[1] - cord1[1]
    distance_to_bottom = cord1[1]
    distance_to_left = cord1[0]
    distance_to_right = boundary[0] - cord1[0]

    # Check if the circle touches any wall
    if distance_to_top <= radius:
        direction = (0, 1)
    elif distance_to_bottom <= radius:
        direction = (0, -1)
    elif distance_to_left <= radius:
        direction = (-1, 0)
    elif distance_to_right <= radius:
        direction = (1, 0)

    return direction


def draw_vector(screen, vector, position, color=(255, 255, 255), scale=20):
    # Scale the vector based on the scale parameter
    scaled_vector = vector * scale

    # Calculate the end point of the vector
    end_point = position + scaled_vector

    # Draw the vector
    p.draw.line(screen, color, position, end_point, 2)


def set_magnitude(v: np.ndarray, x: float) -> np.ndarray:
    """
    Set the magnitude of a vector to a specified value.

    Args:
    - v: Input vector
    - x: Desired magnitude

    Returns:
    - Vector with the specified magnitude
    # Example usage:
    v = np.array([1, 2, 3])
    desired_magnitude = 5
    result = set_magnitude(v, desired_magnitude)
    print("Original vector:", v)
    print("Vector with desired magnitude:", result)

    """
    # Normalize the vector
    normalized_v = v / np.linalg.norm(v)

    # Scale the normalized vector to the desired magnitude
    scaled_v = normalized_v * x

    return scaled_v


random.seed(random.random())


def rclr(t=random.random()):
    # Adjust the period and phase to change the speed and starting color
    period = 1.0  # Adjust this value to change the speed of color transition
    phase_shift = 0.0  # Adjust this value to change the starting color

    # Calculate color components using sine function
    r = int((math.sin(2 * math.pi * t / period + phase_shift) + 1) * 127.5)
    g = int((math.sin(2 * math.pi * (t / period + 1 / 3) + phase_shift) + 1) * 127.5)
    b = int((math.sin(2 * math.pi * (t / period + 2 / 3) + phase_shift) + 1) * 127.5)

    return (r, g, b)


# # Example usage:
# current_time = 10.0  # Replace this with the actual current time
# color = time_based_color(current_time)
# print("Color:", color)
#
# def rclr():
#     return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

import datetime


def generate_file_name(prefix='', suffix='', extension=''):
    """
    Generate a file name based on the current date and time.

    Parameters:
        prefix (str): Optional prefix for the file name.
        suffix (str): Optional suffix for the file name.
        extension (str): Optional file extension.

    Returns:
        str: The generated file name.
    """
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{prefix}{current_time}{suffix}.{extension}"
    return file_name


def vector_with_magnitude(mag: float, vec=np.array([0, 0]), dim: int = 2) -> np.ndarray:
    """
    Generates a random vector of specified magnitude `h` in `dim` dimensions.

    Parameters:
        mag (float): The magnitude of the vector.
        dim (int): The number of dimensions of the vector. Default is 3.

    Returns:
        np.ndarray: A NumPy array representing the vector.
    """
    # Generate random values for the components
    components = np.random.randn(dim)

    # Normalize the vector to have magnitude `mag`
    normalized_vector = components / np.linalg.norm(components)

    # Scale the normalized vector to have magnitude `mag`
    vector = normalized_vector * mag

    return vector if np.dot(vec, vector) > 0 else - vector


def append_to_file(file_path, content):
    """
    Append content to a file.

    Args:
        file_path (str): The path to the file.
        content (str): The content to be appended to the file.
    """
    # Open the file in append mode ('a')
    with open(file_path, "a") as f:
        # Write content to the file
        f.write(str(content) + "\n")


def draw_horizontal_line(surface, x1, x2, y, color):
    p.draw.line(surface, color, (x1, y), (x2, y))


def fill_triangle(surface, points, color):
    # # Sort the points by y-coordinate
    # points.sort(key=lambda p: p[1])
    #
    # # Extract sorted points
    # p1, p2, p3 = points
    #
    # # Check if it's a flat bottom or flat top triangle
    # if p2[1] == p3[1]:
    #     flat_base = True
    # else:
    #     flat_base = False
    #
    # # Initialize the edge slopes
    # if not flat_base:
    #     inv_slope1 = (p2[0] - p1[0]) / (p2[1] - p1[1])
    #     inv_slope2 = (p3[0] - p1[0]) / (p3[1] - p1[1])
    # else:
    #     inv_slope1 = (p3[0] - p1[0]) / (p3[1] - p1[1])
    #     inv_slope2 = (p3[0] - p2[0]) / (p3[1] - p2[1])
    #
    # # Initialize edge x-coordinates
    # x1 =(p1[0])
    # x2 = (p1[0])
    # #   if type(x1)!=int:
    # #         print(type(x1))
    # #         pass
    # #     print(x1,x1)
    #     draw_horizontal_line(surface, int(x1), int(x2), y, color)
    #
    #     if not flat_base:
    #         x1 += inv_slope1
    #         x2 += inv_slope2
    #     else:
    #         x1 += inv_slope1
    #         x2 += inv_slope2
    # # # Start filling scanlines
    # # for y in range(p1[1], p3[1] + 1):
    # #
    p.draw.polygon(surface, (255, 0, 0), points)


def polyc(surf, center, points, color):
    for i in range(len(points)):
        fill_triangle(surf, [center, points[i], points[(i + 1) % len(points)]], color)


def totu(a):
    return (int(a[0]), int(a[1]))


import math


def is_clockwise(objects, center):
    # Calculate angles with respect to provided center
    angles = []
    for obj in objects:
        angle = math.atan2(obj[1] - center[1], obj[0] - center[0])
        angles.append(angle)

    for i in range(len(angles)):
        if angles[i] < 0:
            angles[i] += 2 * math.pi
    # Sort angles
    # Find the index of the smallest angle
    min_index = angles.index(min(angles))

    # Rotate the angles list so that the smallest angle comes first
    angles = angles[min_index:] + angles[:min_index]
    sorted_angles = sorted(angles)

    # Check if sorted angles are in ascending order
    if angles == sorted_angles:
        return True, (angles)  # Clockwise order
    else:
        return False, (angles)  # Not clockwise order
