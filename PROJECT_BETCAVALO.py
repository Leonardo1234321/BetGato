import pygame
from sys import exit
from random import randint
pygame.init()
screen = pygame.display.set_mode((1280, 660))
tempo_inicial = 60000




class gato:
    def __init__(self):
        self.sprites = []
        self.index_int = 0
        self.index_float = float(0)
        self.speed = 0
        self.valor_apostado = 0
        self.keys = pygame.K_0
    def spritecheetos(self, x, y, a , b):
        for i in range(0, x):
            self.sprites.append(pygame.image.load(f"gato{y}_correndo/tile00{i}.png"))
        for i in range(0, x):
            self.sprites[i] = pygame.transform.scale(self.sprites[i], (a, b))
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
        if self.sprite_rect.right < (screen.get_width() / 3):
            self.speed -= 0.1
        elif (screen.get_width() / 3) <= self.sprite_rect.right <= ((2*screen.get_width()) / 3):
            self.speed -= 0.2
        elif ((2*screen.get_width()) / 3) <= self.sprite_rect.right:
            self.speed -= 0.3
        if self.speed >= 0:
            self.gato_animacao(0.5 + (self.speed/10), 2)
        else:
            self.gato_animacao(0.5, 2)
        self.gato_movimento(5, -5)
  
fundo1 = [pygame.transform.scale(pygame.image.load("fundos/fundo01.png"), (1280, 660)), 
          pygame.transform.scale(pygame.image.load("fundos/fundo02.png"), (1280, 660))]
fundo_rect = [fundo1[0].get_rect(topleft=(0,0)),fundo1[1].get_rect(topleft=(1280,0))]

def fundo_dinamico(x):
    fundo_rect[0].centerx -= x
    fundo_rect[1].centerx -= x
    if fundo_rect[0].right <= 0:
        fundo_rect[0].left = screen.get_width()
    if fundo_rect[1].right <= 0:
        fundo_rect[1].left = screen.get_width()
        

gato01 = gato()
gato01.spritecheetos(8, 1, 200, 200)
gato01.Gatorect(100, 550)
gato01.keys = pygame.K_w

gato02 = gato()
gato02.spritecheetos(8, 2, 200, 200)
gato02.Gatorect(100, 500)
gato02.keys = pygame.K_d

gato03 = gato()
gato03.spritecheetos(8, 3, 200, 200)
gato03.Gatorect(100, 600)
gato03.keys = pygame.K_a

clock = pygame.time.Clock()

text_Font = pygame.font.Font("minecraft_font.ttf", 40)

fases = [False, False]
menu_musik = True
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    fases[0] = True
                    tempo_inicial = pygame.time.get_ticks() + 6500
                    pygame.mixer.music.load("musicas/musica_corrida.mpeg")
                    pygame.mixer.music.play()
    if menu_musik:
        pygame.mixer.music.load("musicas/musica_menu.mpeg")
        pygame.mixer.music.play(123123)
        menu_musik = False
    while fases[0]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        tempo = (tempo_inicial - pygame.time.get_ticks()) / 1000
        if tempo <= 0:
            fases[1] = True
            tempo_inicial = pygame.time.get_ticks() + 60000
            fases[0] = False
            break

        if tempo > 2:
            texto1 = text_Font.render(f"{tempo:.2f}", False, "white")
        elif 0.5< tempo <= 2:
            texto1 = text_Font.render("Preparados?", False, "white")
        elif tempo <= 0.5:
            texto1 = text_Font.render("FOI!!!", False, "white")
        texto1_rect = texto1.get_rect(center=(640, 50))

        screen.blit(fundo1[0], fundo_rect[0])
        screen.blit(fundo1[1], fundo_rect[1])
        screen.blit(texto1, texto1_rect)
        screen.blit(gato01.sprites[gato01.index_int], gato01.sprite_rect)
        screen.blit(gato02.sprites[gato02.index_int], gato02.sprite_rect)
        screen.blit(gato03.sprites[gato03.index_int], gato03.sprite_rect)

        pygame.time.wait(3)
        pygame.display.update()
        clock.tick(30)

    while fases[1]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == gato01.keys:
                    gato01.speed += 1
                if event.key == gato02.keys:
                    gato02.speed += 1
                if event.key == gato03.keys:
                    gato03.speed += 1
                if event.key == pygame.K_0:
                    tempo_inicial = pygame.time.get_ticks() + 60000
                    pygame.mixer.music.load("musicas/musica_corrida.mpeg")
                    pygame.mixer.music.play(123123)

        tempo = (tempo_inicial - pygame.time.get_ticks()) / 1000
        if tempo <= 0:
            fases[1] = False
            break
        
        texto1 = text_Font.render(f"{tempo:.2f}", False, "white")
        texto1_rect = texto1.get_rect(center=(640, 50))


        screen.blit(fundo1[0], fundo_rect[0])
        screen.blit(fundo1[1], fundo_rect[1])
        screen.blit(texto1, texto1_rect)
        fundo_dinamico(15)
        screen.blit(gato01.sprites[gato01.index_int], gato01.sprite_rect)
        screen.blit(gato02.sprites[gato02.index_int], gato02.sprite_rect)
        screen.blit(gato03.sprites[gato03.index_int], gato03.sprite_rect)

        gato01.corrida()
        gato02.corrida()
        gato03.corrida()
        pygame.time.wait(3)
        pygame.display.update()
        clock.tick(30)
    
    pygame.time.wait(3)
    pygame.display.update()
    clock.tick(30)
