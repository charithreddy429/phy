import pygame

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Load transparent circle image
circle = pygame.Surface((40,40),pygame.SRCALPHA)
pygame.draw.circle(circle,(255,255,255),(20,20),20)
circle.convert_alpha()

# Initial alpha value
alpha = 128  # Semi-transparent (adjust as needed)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Increase or decrease alpha value with arrow keys
            if event.key == pygame.K_UP:
                alpha = min(alpha + 10, 255)  # Increase alpha (up arrow)
            elif event.key == pygame.K_DOWN:
                alpha = max(alpha - 10, 0)    # Decrease alpha (down arrow)

    # Clear the screen
    screen.fill((0, 0, 180))

    # Set alpha transparency for the circle image
    circle.set_alpha(alpha)
    print(type(circle))

    # Draw the transparent circle image onto the screen
    screen.blit(circle, (width // 2 - circle.get_width() // 2, height // 2 - circle.get_height() // 2))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
