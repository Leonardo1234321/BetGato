import pygame
from sys import exit
from random import randint
pygame.init()
screen = pygame.display.set_mode((1280, 660))

class gato:
    def __init__(self):
        self.sprites = []
        self.index_int = 0
        self.index_float = float(0)
        self.speed = 0
        self.valor_apostado = 0
        self.keys = pygame.K_d
    def spritecheetos(self, x, y):
        for i in range(0, x):
            self.sprites.append(pygame.image.load(f"gato{y}_correndo/tile00{i}.png"))
        for i in range(0, x):
            self.sprites[i] = pygame.transform.scale(self.sprites[i], (200, 200))
    def Gatorect(self, x, y):
        self.sprite_rect = self.sprites[self.index_int].get_rect(center=(x, y))
    def gato_animacao(self, v, s):
        if self.speed != 0:
            self.index_float += min(v, s)
            self.index_int = int(self.index_float)
        if 0 > self.index_int or self.index_int >= (len(self.sprites) - 1):
            self.index_float = 0
            self.index_int = 0
    def gato_movimento(self, max, min):
        self.sprite_rect.centerx += self.speed
        if self.speed >= max:
            self.speed = max
        elif self.speed <= min:
            self.speed = min
        if self.sprite_rect.right >= screen.get_width(): 
            self.sprite_rect.right= screen.get_width()
        elif self.sprite_rect.left <= 0: 
            self.sprite_rect.left = 0
    def corrida(self):
        self.speed -= 0.1
        if self.speed >= 0:
            self.gato_animacao(0.5 + (self.speed/10), 2)
        else:
            self.gato_animacao(0.5, 2)
        self.gato_movimento(5, -3)
  
fundo1 = [pygame.transform.scale(pygame.image.load("fundo01.jpeg"), (1280, 660)), 
          pygame.transform.scale(pygame.image.load("fundo01.jpeg"), (1280, 660))]
    
fundo_rect = [fundo1[0].get_rect(topleft=(0,0)),fundo1[1].get_rect(topleft=(1280,0))]

def fundo_dinamico(x):
    fundo_rect[0].centerx -= x
    fundo_rect[1].centerx -= x
    if fundo_rect[0].right <= 0:
        fundo_rect[0].left = screen.get_width()
    if fundo_rect[1].right <= 0:
        fundo_rect[1].left = screen.get_width()
        

gato01 = gato()
gato01.spritecheetos(8, 1)
gato01.Gatorect(100, 500)

gato02 = gato()
gato02.spritecheetos(8, 2)
gato02.Gatorect(100, 550)

gato03 = gato()
gato03.spritecheetos(8, 3)
gato03.Gatorect(100, 600)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == gato01.keys:
                gato01.speed += 0.6
            if event.key == pygame.K_a:
                gato02.speed += 0.6
            if event.key == pygame.K_0:
                gato03.speed += 0.6

    screen.blit(fundo1[0], fundo_rect[0])
    screen.blit(fundo1[1], fundo_rect[1])
    fundo_dinamico(10)

    screen.blit(gato01.sprites[gato01.index_int], gato01.sprite_rect)
    screen.blit(gato02.sprites[gato02.index_int], gato02.sprite_rect)
    screen.blit(gato03.sprites[gato03.index_int], gato03.sprite_rect)

    gato01.corrida()
    gato02.corrida()
    gato03.corrida()

    pygame.display.update()
    clock.tick(30)