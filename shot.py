# shot.py
import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    SHOT_RADIUS = 5
    
    def __init__(self, x, y):
        super().__init__(x, y, self.SHOT_RADIUS)  # automatically added to containers
        self.velocity = pygame.Vector2(0, 0)  # initialize velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt
