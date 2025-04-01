import pygame
import random

pygame.init () #inicia o pygame

#tamanho da janela do jogo
x = 1280 
y = 720 

#abrir a janela
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('My first game in Python')

#carrega e define o tamanho da imagem de fundo
bg = pygame.image.load('img/tela.jpg')
bg = pygame.transform.scale(bg, (x,y))

#imagem do inimigo
inimigo = pygame.image.load('img/inimigo.png').convert_alpha()
inimigo = pygame.transform.scale(inimigo, (55,55))

#imagem do player
playerImg = pygame.image.load('img/player.png').convert_alpha()
playerImg = pygame.transform.scale(playerImg, (65,65)) 
playerImg = pygame.transform.rotate(playerImg, -90)

#imagem do golpe
golpe = pygame.image.load('img/golpe.png').convert_alpha()
golpe = pygame.transform.scale(golpe, (30, 30))
golpe = pygame.transform.rotate(golpe, 0)

#posicoes
pos_inimigo_x = 500
pos_inimigo_y = 360

pos_player_x = 200
pos_player_y = 300

vel_x_golpe = 0
pos_x_golpe = 200
pos_y_golpe = 300

#pontuacao
pontos = 3

triggered = False
rodando=True 

font = pygame.font.SysFont('font/PixelGameFont.ttf', 50)

#objeto da imagem
player_rect = playerImg.get_rect()
inimigo_rect = inimigo.get_rect()
golpe_rect = golpe.get_rect()


#funcoes
def respawn ():
    x = 1350
    y = random.randint (1,640)
    return [x,y]

def respawn_golpe():
    triggered = False
    respawn_golpe_x = pos_player_x
    respawn_golpe_y = pos_player_y
    vel_x_golpe = 0
    return[respawn_golpe_x, respawn_golpe_y, triggered, vel_x_golpe]

def colisions():
    global pontos
    if player_rect.colliderect(inimigo_rect) or inimigo_rect.x == 60:
        pontos -=1
        return True
    elif golpe_rect.colliderect(inimigo_rect):
        pontos +=1
        return True
    else:
        return False 


#deixa a janela aberta

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    #faz a imagem aparecer
    screen.blit(bg, (0,0))

    #carrossel
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))
    
    #teclas
    tecla = pygame.key.get_pressed()
    if tecla [pygame.K_UP] and pos_player_y > 1:
        pos_player_y -=1
        if not triggered:
            pos_y_golpe -=1

    if tecla [pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y +=1

        if not triggered:
            pos_y_golpe +=1


    if tecla [pygame.K_SPACE]:
        triggered = True 
        vel_x_golpe = 1.5

    if pontos == -1:
        rodando = False

    #respawn
    if pos_inimigo_x == 50:
        pos_inimigo_x = respawn()[0]
        pos_inimigo_y = respawn()[1]

    if pos_x_golpe >= 1300:
        pos_x_golpe, pos_y_golpe, triggered,  vel_x_golpe = respawn_golpe()

    if pos_inimigo_x == 50 or colisions():
        pos_inimigo_x = respawn()[0]
        pos_inimigo_y = respawn()[1]
        

    #posicao do rect
    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    golpe_rect.y = pos_y_golpe
    golpe_rect.x = pos_x_golpe

    inimigo_rect.y = pos_inimigo_y
    inimigo_rect.x = pos_inimigo_x

    #movimento
    x-=0.3
    pos_inimigo_x -=1

    pos_x_golpe += vel_x_golpe

    # pygame.draw.rect(screen,(255,0, 0), player_rect, 4)
    # pygame.draw.rect(screen,(255,0, 0), golpe_rect, 4) 
    # pygame.draw.rect(screen,(255,0, 0), inimigo_rect, 4)

    score =font.render(f'Pontos {int(pontos)}', True, (255, 255, 255))
    screen.blit(score, (50,50))

    #criar imagens
    screen.blit(inimigo, (pos_inimigo_x, pos_inimigo_y))  # Corrigido
    screen.blit(golpe, (pos_x_golpe, pos_y_golpe))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    print(pontos)

    pygame.display.update()