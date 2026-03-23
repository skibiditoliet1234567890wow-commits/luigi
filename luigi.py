import time
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Luigi')

# Load the Luigi image
luigi_image = pygame.image.load('luigi.png')  # Make sure you have a luigi.png in the same directory

# Main loop
time_start = time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear the screen
    screen.fill((255, 255, 255))  # Fill with white

    # Display the Luigi image
    screen.blit(luigi_image, (0, 0))
    font = pygame.font.Font(None, 74)
    text = font.render('luigi', True, (0, 0, 0))  # Black text
    screen.blit(text, (350, 250))

    # Update the display
    pygame.display.flip()

    # Check elapsed time
    if time.time() - time_start > 200:
        break

pygame.quit()