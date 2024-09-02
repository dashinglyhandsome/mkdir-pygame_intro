#Add Interactivity: modifying the code to change the
#background color when the user clicks anywhere in the window
#this code will cycle through a list of colors each time
#the user clicks.

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
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# List of colors to cycle through
colors = [WHITE, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA]
current_color_index = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for mouse clicks
    if pygame.mouse.get_pressed()[0]:  # If left mouse button is clicked
        current_color_index = (current_color_index + 1) % len(colors)

    # Fill the background with the current color
    screen.fill(colors[current_color_index])

    # Draw shapes
    pygame.draw.rect(screen, RED, pygame.Rect(50, 50, 200, 100))
    pygame.draw.circle(screen, GREEN, (400, 300), 75)
    pygame.draw.line(screen, BLUE, (0, 0), (WIDTH, HEIGHT), 5)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

#I added a list of colors (colors) that the background
#will cycle through each time the user clicks.
#The code checks for mouse clicks using pygame.mouse.get_pressed().
#If the left mouse button is clicked (pygame.mouse.get_pressed()[0]),
#the background color changes. The current_color_index is updated
#with each click, cycling through the list of colors.
#Now, every time I click anywhere in the window,
#the background color will change to the next color in the list.
