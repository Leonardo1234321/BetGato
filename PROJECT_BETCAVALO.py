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
        self.ganhou = False
        self.clicks = 0
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

gato01 = gato("LARANJA")
gato01.spritecheetos(8, 1, 200, 200)
gato01.Gatorect(100, 300)#300 # 360 #420
gato01.keys = teclas[0]

gato02 = gato("PRETO")
gato02.spritecheetos(8, 2, 200, 200)
gato02.Gatorect(100, 360)
gato02.keys = teclas[1]

gato03 = gato("CINZA")
gato03.spritecheetos(8, 3, 200, 200)
gato03.Gatorect(100, 420)
gato03.keys = teclas[2]
gatos = [gato01, gato02, gato03]
selecionado = [False, False, False]

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
botao_s_rect = botao_seguir.get_rect(center=(1180, 590))
botao_v_rect = botao_voltar.get_rect(center=(100, 590))
crias = pygame.transform.scale(pygame.image.load("elementos_imagens/crias.jpeg"), (1280, 660))

imagem_a = pygame.image.load("elementos_imagens/a.png")
imagem_g = pygame.image.load("elementos_imagens/g.png")
imagem_l = pygame.image.load("elementos_imagens/l.png")
imagem_a_rect = imagem_a.get_rect(center=(30, 300))
imagem_g_rect = imagem_a.get_rect(center=(30, 360))
imagem_l_rect = imagem_a.get_rect(center=(30, 420))

tabela = pygame.Surface((700, 700))
tabela_rect = tabela.get_rect(center=(640, 330))
tabela.set_alpha(220)
tabela.fill((0,0,0))
tabela_texto3 = []

Valor_botao_add = [pygame.transform.scale(pygame.image.load("elementos_imagens/botao_100.png"), (150, 75)), 
pygame.transform.scale(pygame.image.load("elementos_imagens/botao_500.png"), (150, 75)),
pygame.transform.scale(pygame.image.load("elementos_imagens/botao_1000.png"), (150, 75))]
valores = [100, 500, 1000]
botao_add_rect = []
botao_sub_rect = []
botao_x = 750
for i in Valor_botao_add:
    botao_add_rect.append(i.get_rect(topleft=(botao_x,300)))
    botao_sub_rect.append(i.get_rect(topleft=(botao_x,450)))
    botao_x += 175
Valor_botao_sub = Valor_botao_add.copy()

comojogar = pygame.image.load("fundos/como_jogar.png")

indice_textoAlerta = 0

total = 0

fases = [False, False, False, False, False, False]

podendo = True
menu_musik = True
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(event.pos):
                    podendo = True
                    fases[5] = True
                if creditos_rect.collidepoint(event.pos):
                    fases[3] = True
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
    fundo_dinamico(16)
    
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
            tempo_inicial = pygame.time.get_ticks() + 56000
            indice_textoAlerta = 0
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
                    gato01.clicks += 1
                if event.key == gato02.keys:
                    gato02.speed += 1
                    gato02.clicks += 1
                if event.key == gato03.keys:
                    gato03.speed += 1
                    gato03.clicks += 1

        
        chegada = pygame.rect.Rect((fundo_rect[2].left + 1065), 221, 32, 311)
        tempo = (tempo_inicial - pygame.time.get_ticks()) / 1000
        screen.blit(fundo1[0], fundo_rect[0])
        screen.blit(fundo1[1], fundo_rect[1])
        screen.blit(fundo1[2], fundo_rect[2])
        fundo_dinamico(16)

        if tempo > 0:
            texto1 = text_Font.render(f"{tempo:.2f}", False, "white")
            texto1_rect = texto1.get_rect(center=(640, 50))
            texto_alerta = [text_Font.render(f"Mudando as teclas em {tempo - 35:.2f}", False, "white"), 
                            text_Font.render(f"Mudando as teclas em {tempo - 15:.2f}", False, "white"),
                            text_Font.render(f"", False, "white")]
            texto_alerta_rect = texto_alerta[indice_textoAlerta].get_rect(center=(640, 88))
            screen.blit(texto1, texto1_rect)
            screen.blit(texto_alerta[indice_textoAlerta], texto_alerta_rect)
        else:
            texto1 = text_Font.render("A linha de chegada esta proxima..", False, "white")
            texto1_rect = texto1.get_rect(center=(640, 50))
            screen.blit(texto1, texto1_rect)

        if 34.9 <= tempo < 35:
            gato01.keys = teclas[2]
            gato02.keys = teclas[0]
            gato03.keys = teclas[1]
            imagem_a_rect.centery = 360
            imagem_g_rect.centery = 420
            imagem_l_rect.centery = 300
            indice_textoAlerta = 1
        elif 14.9 <= tempo < 15:
            gato01.keys = teclas[1]
            gato02.keys = teclas[2]
            gato03.keys = teclas[0]
            imagem_a_rect.centery = 420
            imagem_g_rect.centery = 300
            imagem_l_rect.centery = 360
            indice_textoAlerta = 2
        elif tempo <= 0:
            fim = True
            for i in gatos:
                if chegada.collidepoint(i.sprite_rect.centerx, i.sprite_rect.centery):
                    tempo_inicial = pygame.time.get_ticks() + 20000
                    i.ganhou = True
                    fases[2] = True
                    fases[1] = False
                    break
        
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
        tempo = (tempo_inicial - pygame.time.get_ticks())/1000
        screen.blit(fundo1[0], fundo_rect[0])
        screen.blit(fundo1[1], fundo_rect[1])
        screen.blit(fundo1[2], fundo_rect[2])
        fundo_dinamico(16)
        
        screen.blit(gato01.sprites[gato01.index_int], gato01.sprite_rect)
        screen.blit(gato02.sprites[gato02.index_int], gato02.sprite_rect)
        screen.blit(gato03.sprites[gato03.index_int], gato03.sprite_rect)

        for i in gatos:
            if i.ganhou == True:
                y = 300
                texto1 = text_Font.render(f"VITORIA DO GATO {i.name}", False, "black")
                texto2 =  text_Font.render(f"VITORIA DO GATO {i.name}", False, "white")
                texto3 = creditos_font.render(f"Valor final do Ganhador: R${total:.2f}", False, "white")
                
                texto1_rect = texto1.get_rect(center=(640, 150))
                texto2_rect = texto2.get_rect(center=(637, 150))
                texto3_rect = texto3.get_rect(topleft=(400, 500))
                for i in gatos:
                    tabela_texto3.append([creditos_font.render(f"{i.name} clicks: {i.clicks}", False, "white"),  
                    creditos_font.render(f"{i.name} clicks: {i.clicks}",  False, "white").get_rect(topleft=(400, y))])
                    y += 50
                i.ganhou = False
        screen.blit(tabela, tabela_rect)    
        for i in tabela_texto3:
            screen.blit(i[0], i[1])
        screen.blit(texto1, texto1_rect)
        screen.blit(texto2, texto2_rect)
        screen.blit(texto3, texto3_rect)
        if tempo <= 0:
            for i in gatos:
                i.valor_apostado = 0
            total = 0
            fases[2] = False
            menu_musik = True
            break
        gato01.corrida()
        gato02.corrida()
        gato03.corrida()
        pygame.time.wait(3)
        pygame.display.update()
        clock.tick(30)

    while fases[3]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_v_rect.collidepoint(event.pos):
                    fases[3] = False
                    break

        screen.blit(crias, (0,0))
        screen.blit(botao_voltar, botao_v_rect)
        

        pygame.time.wait(3)    
        pygame.display.update()
        clock.tick(30)
    
    while fases[4]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_v_rect.collidepoint(event.pos):
                    fundo_rect[0].left = 0
                    fundo_rect[1].left = 1280
                    fundo_rect[2].left = 1280
                    for i in gatos:
                        i.sprite_rect.left = 100
                        i.speed = 0
                        i.index_int = 0
                        i.index_float = 0
                        i.keys = teclas[gatos.index(i)]
                    gato01.sprite_rect.center=(100, 300)
                    gato02.sprite_rect.center=(100, 360)
                    gato03.sprite_rect.center=(100, 420)
                    fases[4] = False
                    fases[5] = True
                    podendo = False
                    break
                if botao_s_rect.collidepoint(event.pos):
                    fundo_rect[0].left = 0
                    fundo_rect[1].left = 1280
                    fundo_rect[2].left = 1280
                    for i in gatos:
                        i.sprite_rect.left = 100
                        i.speed = 0
                        i.index_int = 0
                        i.index_float = 0
                        i.keys = teclas[gatos.index(i)]
                    gato01.sprite_rect.center=(100, 300)
                    gato02.sprite_rect.center=(100, 360)
                    gato03.sprite_rect.center=(100, 420)
                    imagem_a_rect.centery = 300
                    imagem_g_rect.centery = 360
                    imagem_l_rect.centery = 420
                    tempo_inicial = pygame.time.get_ticks() + 6500
                    pygame.mixer.music.load("musicas/musica_corrida.mpeg")
                    pygame.mixer.music.play()
                    podendo = False
                    fases[0] = True
                    fases[4] = False
                    break
                for i in gatos:
                    if i.sprite_rect.collidepoint(event.pos):
                        selecionado[0] = False
                        selecionado[1] = False
                        selecionado[2] = False
                        selecionado[gatos.index(i)] = True
                for b in botao_add_rect:
                    x = botao_add_rect.index(b)
                    if b.collidepoint(event.pos):
                        for g in gatos:
                            if selecionado[gatos.index(g)]:
                                g.valor_apostado += valores[x]
                for s in botao_sub_rect:
                    x = botao_sub_rect.index(s)
                    if s.collidepoint(event.pos):
                        for g in gatos:
                            if selecionado[gatos.index(g)] and g.valor_apostado >= 0:
                                g.valor_apostado -= valores[x]
                                if g.valor_apostado < 0:
                                    g.valor_apostado = 0
                                    
        pygame.draw.rect(screen, (226, 99, 16), (0, 0, 1280, 660))
        screen.blit(botao_voltar, botao_v_rect)
        screen.blit(botao_seguir, botao_s_rect)
        gato_frame = 150
        if podendo:
            for i in gatos:
                x = gatos.index(i)
                i.index_int = 1
                texto4 = creditos_font.render(f"{i.name}", False, "White")
                texto5 = creditos_font.render(f"valor: R${i.valor_apostado}", False, "White")
                texto4_rect = texto4.get_rect(center=(gato_frame, 275))
                texto5_rect = texto5.get_rect(center=(gato_frame, 325))
                surface = pygame.Surface((200, 200))
                surface.set_alpha(200)
                if i.sprite_rect.collidepoint(pygame.mouse.get_pos()):
                    surface.set_alpha(50)
                if selecionado[x]:
                    surface.set_alpha(50)
                surface.fill((210, 73, 0))
                i.sprite_rect.centery = 150
                i.sprite_rect.centerx = gato_frame
                screen.blit(surface, i.sprite_rect)
                screen.blit(i.sprites[i.index_int], i.sprite_rect)
                screen.blit(texto4, texto4_rect)
                screen.blit(texto5, texto5_rect)
                gato_frame += 225
        logo2 = pygame.transform.scale(pygame.image.load("elementos_imagens/catbetlogofinal.png"), (640, 330))
        screen.blit(logo2, (750, 50))

        total = gato01.valor_apostado + gato02.valor_apostado + gato03.valor_apostado
        texto7 = creditos_font.render(f"Total apostado/premio final: R${total:.2f}", False, "white")
        lucro_medio = ((3 * total) - gato01.valor_apostado - gato02.valor_apostado - gato03.valor_apostado) / 3
        texto8 = creditos_font.render(f"Lucro medio geral: R${lucro_medio:.2f}", False, "white")
        texto9 = creditos_font.render(f"ADICIONAR AO MONTANTE", False, "white")
        texto10 = creditos_font.render(f"DIMINUIR O MONTANTE", False, "white")
        screen.blit(texto7, (50, 420))
        screen.blit(texto8, (50, 470))
        screen.blit(texto9, (750, 270))
        screen.blit(texto10, (750, 420))

        for i in range(0, 3):
            screen.blit(Valor_botao_add[i], botao_add_rect[i])
            screen.blit(Valor_botao_sub[i], botao_sub_rect[i])
        pygame.time.wait(3)
        pygame.display.update()
        clock.tick(30)

    while fases[5]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_v_rect.collidepoint(event.pos):
                    fases[5] = False
                    break
                if botao_s_rect.collidepoint(event.pos):
                    podendo = True
                    fases[4] = True
                    fases[5] = False
                    break

        screen.blit(comojogar, (0,0))
        screen.blit(botao_voltar, botao_v_rect)
        screen.blit(botao_seguir, botao_s_rect)

        pygame.time.wait(3)
        pygame.display.update()
        clock.tick(30)
    pygame.time.wait(3)
    pygame.display.update()
    clock.tick(30)
