from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  
    
    def move(self, dt):
        # Create a forward vector and rotate it by current rotation
        forward = pygame.Vector2(0, -1).rotate(self.rotation) * (PLAYER_SPEED * dt)
        self.position += forward

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt, direction=1):
        """direction: 1 = right (clockwise), -1 = left (counter-clockwise)"""
        self.rotation += PLAYER_TURN_SPEED * dt * direction

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, -1)  # turn left
        if keys[pygame.K_d]:
            self.rotate(dt, 1)   # turn right
        if keys[pygame.K_w]:
            self.move(dt)        # move forward
        if keys[pygame.K_s]:
            self.move(-dt)       # move backward
