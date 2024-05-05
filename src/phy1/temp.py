# import pygame
# import time
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Initialize Pygame
# pygame.init()
#
# # Set the tempo and beats per measure for each rhythm
# tempo = 120
# beats_per_measure_1 = 4  # Change this to adjust the first rhythm
# beats_per_measure_2 = 3  # Change this to adjust the second rhythm
#
# # Calculate the time duration for each beat
# beat_duration = 60.0 / tempo
#
# # Set up the Pygame mixer
# pygame.mixer.init()
#
# # Define the frequencies for each rhythm (you can adjust these to change the tones)
# frequency_1 = 440  # Adjust this to change the first rhythm tone
# frequency_2 = 660  # Adjust this to change the second rhythm tone
# time.sleep(10)
# # Function to generate the waveform for the first rhythm
# def generate_waveform_1():
#     samples = []
#     for t in range(int(44100 * beat_duration)):  # Generate samples for one beat
#         sample = np.sin(2 * np.pi * frequency_1 * t / 44100)
#         samples.append(sample)
#     return samples
#
# # Function to generate the waveform for the second rhythm
# def generate_waveform_2():
#     samples = []
#     for t in range(int(44100 * beat_duration)):  # Generate samples for one beat
#         sample = np.sin(2 * np.pi * frequency_2 * t / 44100)
#         samples.append(sample)
#     return samples
#
# # Generate waveforms
# waveform_1 = generate_waveform_1()
# waveform_2 = generate_waveform_2()
# waveform_1.play()
# # Plot waveforms
# plt.figure(figsize=(10, 6))
#
# plt.subplot(2, 1, 1)
# plt.plot(waveform_1)
# plt.title('First Rhythm Waveform')
# plt.xlabel('Sample')
# plt.ylabel('Amplitude')
#
# plt.subplot(2, 1, 2)
# plt.plot(waveform_2)
# plt.title('Second Rhythm Waveform')
# plt.xlabel('Sample')
# plt.ylabel('Amplitude')
#
# plt.tight_layout()
# plt.show()
#
# # Quit Pygame
# pygame.quit()
import numpy as np


class Circle:
    def __init__(self, center, velocity, radius):
        self.center = np.array(center, dtype=np.float64)
        self.velocity = np.array(velocity, dtype=np.float64)
        self.radius = radius


def generate_circle_array(num_circles, boundary):
    center = np.array(boundary) / 2
    big_radius = 360
    circles = []

    for i in range(1, num_circles):
        position = center + np.float64(
            [10 * (num_circles - i) - 20 * num_circles, 11.25 * (num_circles - i) - 22.5 * num_circles])
        velocity = np.float64([15 * (num_circles - i) / 480, 15 * (num_circles - i) / 480])
        radius = 40 * i
        circles.append(Circle(position, velocity, radius))

    return circles


# Example usage:
num_circles = 6
boundary = (800, 600)
circle_array = generate_circle_array(num_circles, boundary)

for circle in circle_array:
    print("Center:", circle.center, "Velocity:", circle.velocity, "Radius:", circle.radius)
