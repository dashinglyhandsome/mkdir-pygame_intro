#Below is the modified code that includes drawing
#different shapes such as ellipses and polygons


import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Graphics Lab")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(WHITE)

    # Draw a rectangle
    pygame.draw.rect(screen, RED, pygame.Rect(50, 50, 200, 100))

    # Draw a circle
    pygame.draw.circle(screen, GREEN, (400, 300), 75)

    # Draw a line
    pygame.draw.line(screen, BLUE, (0, 0), (WIDTH, HEIGHT), 5)

    # Draw an ellipse
    pygame.draw.ellipse(screen, YELLOW, pygame.Rect(300, 400, 200, 100))

    # Draw a polygon (e.g., a triangle)
    pygame.draw.polygon(screen, PURPLE, [(500, 100), (600, 200), (400, 200)])

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

#The ellipse is yellow.
#The ellipse is drawn inside the rectangle
#The polygon is purple.
#This polygon is a triangle formed by the points (500, 100), (600, 200),
#and (400, 200).
