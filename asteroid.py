import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        child1_velocity = self.velocity.copy()
        child2_velocity = self.velocity.copy()

        random_angle = random.uniform(20, 50)
        
        child1_velocity.rotate(random_angle)
        child2_velocity.rotate(-random_angle)

        child1_velocity *= 1.2
        child2_velocity *= 1.2

        child_radius = self.radius - ASTEROID_MIN_RADIUS

        child1 = Asteroid(self.position.x, self.position.y, child_radius)
        child2 = Asteroid(self.position.x, self.position.y, child_radius)

        child1.velocity = child1_velocity
        child2.velocity = child2_velocity
