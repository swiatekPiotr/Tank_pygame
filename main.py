import pygame, sys
from tank import Tank
from bullet import Shoot


class Game(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 600))

        # Title, icon from flaticon
        pygame.display.set_caption("Tanks")
        icon = pygame.image.load('tank.png')
        pygame.display.set_icon(icon)

        clock = pygame.time.Clock()

        self.player = Tank(self, 2)
        self.bullet = Shoot(self.screen)

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            self.screen.fill((110, 120, 40))
            self.tick()
            self.draw()
            pygame.display.update()
            pygame.display.flip()  # podwójne buforowanie, rysujemy na ukrytej kartce, flip zamienia kartki

    def tick(self):
        self.player.tick()
        if self.player.bullet_status == "fire":
            self.bullet.tick(self.player.bullet_x, self.player.bullet_y, self.player.bullet_angle)

    def draw(self):
        pygame.draw.rect(self.screen, (180, 180, 100), pygame.Rect(120, 220, 60, 280))

        self.player.draw()
        if self.player.bullet_status == "fire":
            self.bullet.draw()


if __name__ == "__main__":
    Game()
