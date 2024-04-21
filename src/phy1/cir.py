import pygame as p 
import math
import cvrec
import utils
out = cvrec.get_out(utils.generate_file_name(r"output\vid","","mp4"),30,(720,1280))
# Initialize p
p.init()

# Set up the screen
screen_width = 405+10
screen_height = 720+10
screen = p.display.set_mode((screen_width, screen_height))
win = p.Surface((1280,720))
p.display.set_caption("Circle with evenly spaced points")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255),  # Cyan
    (128, 0, 128),  # Purple
    (255, 165, 0),  # Orange
    (255, 192, 203),# Pink
    (0, 128, 0),    # Dark Green
    (0, 0, 128),    # Dark Blue
    (128, 128, 0)   # Olive
]

# Function to draw a circle with evenly spaced points
def draw_circle_with_points(screen, center, radius, num_points):
    p.draw.circle(screen, BLACK, center, radius, 20)
    angle_increment = 2 * math.pi / num_points
    for i in range(num_points):
        x = center[0] + int(radius * math.cos(i * angle_increment+45))
        y = center[1] + int(radius * math.sin(i * angle_increment+45))
        # # p.draw.circle(screen, RED, (x, y), 5)
        next_x = center[0] + int(radius * math.cos((i) * angle_increment*factor+45))
        next_y = center[1] + int(radius * math.sin((i ) * angle_increment*factor+45))
        p.draw.line(screen, BLACK, (x, y), (next_x, next_y),2)



maxcir = 180
ncir = 30
factor = -0.01
fps = 30
running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    win.fill(WHITE)
    if ncir<180:
        ncir+=2
    else:
        factor+=1/30
    draw_circle_with_points(win, (640,360), 320, ncir)
    # print(len(p.surfarray.array3d(win)))
    out.write(p.surfarray.array3d(win))
    screen.blit(p.transform.rotozoom(win,-90,405/720),(0,0))
    p.display.flip()
p.quit()
