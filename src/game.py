# classe do jogo, loop do jogo, gerenciamento de estados, etc.
import pygame
import settings

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.width, settings.height))
        pygame.display.set_caption(settings.game_title)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:

            # chamada cada função enquanto o jogo estiver rodando
            self.events()
            self.update()
            self.draw()

            self.clock.tick(settings.fps)
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(settings.colors['black'])
        pygame.display.flip()