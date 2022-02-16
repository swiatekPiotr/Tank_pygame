import pygame
import math
from utils import blit_rotate_center



class Tank(object):
    def __init__(self, game, screen, max_vel):
        self.game= game
        self.size = self.game.screen.get_size()
        self.screen = screen

        self.playerImg = pygame.image.load('tank.png')

        self.max_vel = max_vel
        self.velocity = 0
        self.rotation_vel = 1.5
        self.angle = 0
        self.x, self.y = self.size[0] / 2, self.size[1] * (8 / 10)
        self.acceleration = 0.025


    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        moved = False

        if pressed[pygame.K_a]:
            self.rotate(left=True)
        if pressed[pygame.K_d]:
            self.rotate(right=True)
        if pressed[pygame.K_w]:
            moved = True
            self.move_forward()

        if not moved:
            self.reduce_speed()

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def move_forward(self):
        self.velocity = min(self.velocity + self.acceleration, self.max_vel)
        self.move()

    def reduce_speed(self):
        self.velocity = max(self.velocity - self.acceleration * 4, 0)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.velocity
        horizontal = math.sin(radians) * self.velocity

        self.y -= vertical
        self.x -= horizontal


    def draw(self):
        blit_rotate_center(self.screen, self.playerImg, (self.x, self.y), self.angle)

        # Adding Boundaries
        if self.x <= 0:
            self.x = 0
        if self.x >= self.size[0] - 32:
            self.x = self.size[0] - 32
        if self.y <= 0:
            self.y = 0
        if self.y >= self.size[1] - 32:
            self.y = self.size[1] - 32