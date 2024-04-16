# import numpy as np
# import random
# import pygame as p
from ball import *
import time
import cv2
from structures import Circle
from cvrec import get_out

p.init()
h = width, height = 1380, 746
font = p.font.Font(None, 30)

def debug(info, x=10, y=10,surf = None):
    debug_surf = font.render(str(info), True, "red")
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    if surf is None:
        p.display.get_surface().blit(debug_surf, debug_rect)
    else:
        surf.blit(debug_surf, debug_rect)
import math
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

# Example usage:
prefix = "data_"
suffix = "_backup"
extension = "txt"
file_name = generate_file_name(prefix, suffix, extension)
print("Generated file name:", file_name)

def vector_with_magnitude(mag: float,vec = np.array([0,0]) ,dim: int = 2) -> np.ndarray:
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

    return vector if np.dot(vec,vector)>0 else - vector

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
def polyc(surf , center,points,color):
    for  i in range(len(points)):
        fill_triangle(surf,[center,points[i],points[(i+1)%len(points)]],color)

def totu(a):
    return (int(a[0]),int(a[1]))


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
        return True ,(angles) # Clockwise order
    else:
        return False  ,(angles)# Not clockwise order