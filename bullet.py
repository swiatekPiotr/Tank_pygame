import pygame
from utils import blit_rotate_center


class Shoot():

    def __init__(self, screen):
        self.screen = screen

        self.bullet_img = pygame.image.load('bullet.png')

        self.velocity = 8

    def tick(self, x, y, angle):
        self.bullet_x = x
        self.bullet_y = y
        self.angle = angle
        if self.bullet_y >= 0:
            self.bullet_y -= self.velocity

    def draw(self):
        blit_rotate_center(self.screen, self.bullet_img, (self.bullet_x, self.bullet_y), self.angle)
