# this allows us to use code from
# the open-source pygame library
# throughout this file
from player import Player
from asteroid import Asteroid  
from asteroidfield import AsteroidField
from shot import Shot
import pygame
from constants import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
shots = pygame.sprite.Group() 
asteroids = pygame.sprite.Group()

Shot.containers = (updatable, drawable, shots)


Player.containers = (updatable, drawable)

Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)



def main():
    pygame.init()

    print("Starting Asteroids!")  # exact text the test expects
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    # initialize delta time
    dt = 0


    player = Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField() 

    while True:
        # Check for quit events at the start of each iteration
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen black and refresh the display
        screen.fill((0, 0, 0))

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.kill()
                    shot.kill()
                

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Update delta time (seconds per frame)
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
