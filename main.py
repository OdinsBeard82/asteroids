# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()

    print("Starting Asteroids!")  # exact text the test expects
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    # initialize delta time
    dt = 0

    while True:
        # Check for quit events at the start of each iteration
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen black and refresh the display
        screen.fill((0, 0, 0))
        pygame.display.flip()

        # Update delta time (seconds per frame)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
