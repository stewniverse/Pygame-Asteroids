from circleshape import *
from asteroid import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        # on each frame should if should self.velocity to its position from the parent class CircleShape
        self.position += (self.velocity * dt)