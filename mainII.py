#modify the code: the code below changed the color of the
#rectangle to blue and the circle color changed to red.



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

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill(WHITE)

    # Draw shapes
    pygame.draw.rect(screen, BLUE, pygame.Rect(50, 50, 200, 100))
    pygame.draw.circle(screen, RED, (400, 300), 75)
    pygame.draw.line(screen, GREEN, (0, 0), (WIDTH, HEIGHT), 5)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

#In this code the rectangle is now blue('BLUE =(0,0,255)')
#the circle is now red ('RED = (255,0,0)')
#the line color remains green
