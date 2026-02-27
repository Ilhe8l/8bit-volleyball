# classe do jogo, loop do jogo, gerenciamento de estados, etc.
import pygame
import settings
from src.entities.player import Player

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((settings.width, settings.height))
        pygame.display.set_caption(settings.game_title)
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group() # todos os sprites do jogo, fica mais fácil pra depois conseguir carregar tudo
        # criar jogador
        self.player1 = Player((100, 100), settings.player1_keys)
        self.player2 = Player((1050, 750), settings.player2_keys)

        self.all_sprites.add(self.player1, self.player2) #adiciona sprite do jogador

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
        self.all_sprites.update() # atualiza todos os sprites do jogo

    def draw(self):
        self.screen.fill(settings.colors['black'])

        self.all_sprites.draw(self.screen) # desenha todos os sprites do jogo na tela

        pygame.display.flip()