# circleshape.py
import pygame
from circleshape import CircleShape
from pygame import Vector2
from constants import *
from logger import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius): 
        super().__init__( x, y, radius)
        self.rotation = 0
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        # on each frame should if should self.velocity to its position from the parent class CircleShape
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        log_event("asteroid_split")
        ran_angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(ran_angle)
        vec2 = self.velocity.rotate(-ran_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_one.velocity = vec1 * 1.2
        new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_two.velocity = vec2