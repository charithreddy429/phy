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

def debug(info, x=10, y=10):
    debug_surf = font.render(str(info), True, "red")
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    p.display.get_surface().blit(debug_surf, debug_rect)

import math
def vector_with_magnitude(mag: float, dim: int = 2) -> np.ndarray:
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

    return vector

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
        f.write(content + "\n")
