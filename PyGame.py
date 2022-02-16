import pygame, sys
from Tank import Tank



class Game(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024,600))

        # Title, icon from flaticon
        pygame.display.set_caption("Tanks")
        icon = pygame.image.load('tank.png')
        pygame.display.set_icon(icon)

        clock = pygame.time.Clock()

        self.player = Tank(self, self.screen, 2)

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: sys.exit(0)

            self.tick()
            self.screen.fill((110,120,40))
            self.draw()
            pygame.display.update()
            pygame.display.flip()   #podwójne buforowanie, rysujemy na ukrytej kartce, flip zamienia kartki


    def tick(self):
        self.player.tick()

    def draw(self):
        self.player.draw()
        pygame.draw.rect(self.screen, (180, 180, 100), pygame.Rect(120, 220, 60, 280))


if __name__ == "__main__":
    Game()