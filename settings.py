# configurações de variáveis globais, constantes, etc.
import pygame

game_title = "8-bit Volleyball"
height = 900
width = 1200
fps = 60

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0)
}

player_size = (50, 50)
player_speed = 5

ball_size = (30, 30)
ball_speed = 3

player1_keys = {
    'up': pygame.K_w,
    'down': pygame.K_s,
    'left': pygame.K_a,
    'right': pygame.K_d,
    'jump': pygame.K_SPACE
}

player2_keys = {
    'up': pygame.K_UP,
    'down': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'jump': pygame.K_RETURN
}