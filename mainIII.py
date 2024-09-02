#modify the code: the code below adjust the size and position of the shapes



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

    # Draw shapes with adjusted sizes and positions
    pygame.draw.rect(screen, BLUE, pygame.Rect(100, 150, 300, 150))  # Rectangle
    pygame.draw.circle(screen, RED, (600, 400), 100)  # Circle
    pygame.draw.line(screen, GREEN, (0, 0), (WIDTH // 2, HEIGHT), 10)  # Line

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

#Summary of Changes:
#Rectangle: Positioned more centrally on the left side,
#and it's larger than before.
#Circle: Moved towards the bottom right and larger.
#Line: Starts from the top-left corner and
# now reaches the middle of the screen horizontally and fully vertically,
#making it more visible.
