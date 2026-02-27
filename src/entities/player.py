# classe do jogador

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, key_mapping):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft=pos) # cria caixa de colisão
        
        # controles
        self.keys = key_mapping 

        # atributos para movimentação e tals
        self.direction = pygame.math.Vector2(0, 0) # direção do movimento
        self.speed = 5

        # estados
        self.state = 'idle' # estado inicial do jogador
        self.on_ground = False # se o jogador está no chão

    def get_input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = 0
        self.direction.y = 0

        # movimenta para os 4 lados
        if keys[self.keys['up']]:
            self.direction.y = -1
        if keys[self.keys['down']]:
            self.direction.y = 1
        if keys[self.keys['left']]:
            self.direction.x = -1
        if keys[self.keys['right']]:
            self.direction.x = 1
        if keys[self.keys['jump']]:
            self.jump()

    def jump(self):
        print("pulo")

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)
