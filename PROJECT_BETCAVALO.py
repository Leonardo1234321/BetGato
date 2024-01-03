import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1280, 660))
tempo_inicial = 50000

class gato:
    def __init__(self, name):
        self.sprites = []
        self.index_int = 0
        self.index_float = float(0)
        self.speed = 0
        self.valor_apostado = 0
        self.keys = pygame.K_0
        self.name = name
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
  
fundo1 = [pygame.transform.scale(pygame.image.load("fundos/fundo_running_track01.png"), (1280, 660)), 
          pygame.transform.scale(pygame.image.load("fundos/fundo_running_track02.png"), (1280, 660)),
          pygame.transform.scale(pygame.image.load("fundos/linha_de_chegada.png"), (1280, 660))]
fundo_rect = [fundo1[0].get_rect(topleft=(0,0)),fundo1[1].get_rect(topleft=(1280,0)), fundo1[2].get_rect(topleft=(1280, 0))]


fim = False
mover = False
def fundo_dinamico(x):
    global fim
    global mover
    fundo_rect[0].centerx -= x
    fundo_rect[1].centerx -= x
    if fundo_rect[0].right <= 0:
        fundo_rect[0].left = screen.get_width()
        if fim:
            mover = True 
    elif fundo_rect[1].right <= 0:
        fundo_rect[1].left = screen.get_width()
        if fim:
            mover = True 
    if mover:
        fundo_rect[2].centerx -= x
        if fundo_rect[2].right <= 0:
            fim = False
            mover = False

teclas = [pygame.K_a, pygame.K_g, pygame.K_l]

gato01 = gato("Lindo")
gato01.spritecheetos(8, 1, 200, 200)
gato01.Gatorect(100, 300)#300 # 360 #420
gato01.keys = teclas[0]

gato02 = gato("Gostoso")
gato02.spritecheetos(8, 2, 200, 200)
gato02.Gatorect(100, 360)
gato02.keys = teclas[1]

gato03 = gato("Charmoso")
gato03.spritecheetos(8, 3, 200, 200)
gato03.Gatorect(100, 420)
gato03.keys = teclas[2]
gatos = [gato01, gato02, gato03]

botao_iniciar = pygame.transform.scale(pygame.image.load("elementos_imagens/botao_iniciar.png"), (175, 75))
botao_rect = botao_iniciar.get_rect(center=(640, 430))
logo = pygame.transform.scale(pygame.image.load("elementos_imagens/catbetlogofinal.png"), (960, 495))
logo_rect = logo.get_rect(center=(640, 230))

clock = pygame.time.Clock()

text_Font = pygame.font.Font("minecraft_font.ttf", 40)

creditos_font = pygame.font.Font("minecraft_font.ttf", 20)
creditos = creditos_font.render("Creditos dos criadores ©", False, "white")
creditos_rect = creditos.get_rect(topleft=(950, 610))

botao_seguir = pygame.image.load("elementos_imagens/seta_seguir.png")
botao_voltar = pygame.image.load("elementos_imagens/seta_voltar.png")
botao_s_rect = botao_seguir.get_rect(center=(100, 100))
botao_v_rect = botao_voltar.get_rect(center=(100, 590))
crias = pygame.transform.scale(pygame.image.load("elementos_imagens/crias.jpeg"), (1280, 660))

imagem_a = pygame.image.load("elementos_imagens/a.png")
imagem_g = pygame.image.load("elementos_imagens/g.png")
imagem_l = pygame.image.load("elementos_imagens/l.png")
imagem_a_rect = imagem_a.get_rect(center=(30, 300))
imagem_g_rect = imagem_a.get_rect(center=(30, 360))
imagem_l_rect = imagem_a.get_rect(center=(30, 420))


fases = [False, False, False]
menu_musik = True
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(event.pos):
                    fundo_rect[0].left = 0
                    fundo_rect[1].left = 1280
                    fundo_rect[2].left = 1280
                    for i in gatos:
                        i.sprite_rect.left = 100
                        i.speed = 0
                        i.index_int = 0
                        i.index_float = 0
                        i.keys = teclas[gatos.index(i)]
                    imagem_a_rect.centery = 300
                    imagem_g_rect.centery = 360
                    imagem_l_rect.centery = 420
                    fases[0] = True
                    tempo_inicial = pygame.time.get_ticks() + 6500
                    pygame.mixer.music.load("musicas/musica_corrida.mpeg")
                    pygame.mixer.music.play()
                if creditos_rect.collidepoint(event.pos):
                    fases[2] = True
    if menu_musik:
        pygame.mixer.music.load("musicas/musica_menu.mpeg")
        pygame.mixer.music.play(123123)
        menu_musik = False
    screen.blit(fundo1[0], fundo_rect[0])
    screen.blit(fundo1[1], fundo_rect[1])
    screen.blit(gato01.sprites[gato01.index_int], gato01.sprite_rect)
    screen.blit(gato02.sprites[gato02.index_int], gato02.sprite_rect)
    screen.blit(gato03.sprites[gato03.index_int], gato03.sprite_rect)
    screen.blit(logo, logo_rect)
    screen.blit(botao_iniciar, botao_rect)
    screen.blit(creditos, creditos_rect)
    fundo_dinamico(15)
    
    for i in gatos:
        i.speed = -0.1
        i.gato_animacao(0.5, 2)

    while fases[0]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        tempo = (tempo_inicial - pygame.time.get_ticks()) / 1000
        if tempo <= 0:
            fases[1] = True
            tempo_inicial = pygame.time.get_ticks() + 50000
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

        
        chegada = pygame.rect.Rect((fundo_rect[2].left + 1065), 221, 32, 311)
        tempo = (tempo_inicial - pygame.time.get_ticks()) / 1000
        screen.blit(fundo1[0], fundo_rect[0])
        screen.blit(fundo1[1], fundo_rect[1])
        screen.blit(fundo1[2], fundo_rect[2])
        fundo_dinamico(15)
        if 34.9 <= tempo < 35:
            gato01.keys = teclas[2]
            gato02.keys = teclas[0]
            gato03.keys = teclas[1]
            imagem_a_rect.centery = 360
            imagem_g_rect.centery = 420
            imagem_l_rect.centery = 300
        elif 19.9 <= tempo < 20:
            gato01.keys = teclas[1]
            gato02.keys = teclas[2]
            gato03.keys = teclas[0]
            imagem_a_rect.centery = 420
            imagem_g_rect.centery = 300
            imagem_l_rect.centery = 360
        elif tempo <= 0:
            fim = True
            for i in gatos:
                if chegada.collidepoint(i.sprite_rect.centerx, i.sprite_rect.centery):
                    print(f"{i.name} GANHOU")
                    fases[1] = False
                    break
        if tempo > 0:
            texto1 = text_Font.render(f"{tempo:.2f}", False, "white")
            texto1_rect = texto1.get_rect(center=(640, 50))
            screen.blit(texto1, texto1_rect)
        else:
            texto1 = text_Font.render("A linha de chegada esta proxima..", False, "white")
            texto1_rect = texto1.get_rect(center=(640, 50))
            screen.blit(texto1, texto1_rect)

        
        screen.blit(gato01.sprites[gato01.index_int], gato01.sprite_rect)
        screen.blit(gato02.sprites[gato02.index_int], gato02.sprite_rect)
        screen.blit(gato03.sprites[gato03.index_int], gato03.sprite_rect)

        screen.blit(imagem_a, imagem_a_rect)
        screen.blit(imagem_g, imagem_g_rect)
        screen.blit(imagem_l, imagem_l_rect)

        gato01.corrida()
        gato02.corrida()
        gato03.corrida()
        pygame.time.wait(3)
        pygame.display.update()
        clock.tick(30)
    
    while fases[2]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_v_rect.collidepoint(event.pos):
                    fases[2] = False
                    break

        screen.blit(crias, (0,0))
        screen.blit(botao_voltar, botao_v_rect)
        

        pygame.time.wait(3)    
        pygame.display.update()
        clock.tick(30)
    pygame.time.wait(3)    
    pygame.display.update()
    clock.tick(30)
