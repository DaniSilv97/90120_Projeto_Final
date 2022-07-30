import pygame
import os
from Pokemon import *
from PokemonEnemy import *
from PokemonPlayer import *
from LoadImages import *
from Skill import *

# Criar Janela de jogo (win)
pygame.init()
win_height = 400
win_width = 800
win = pygame.display.set_mode((win_width,win_height))

# Imagem de fundo
background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "desert_BG.png")), (win_width, win_height))

# Desenhar o Jogo
def draw_game():
    global kills,tower_health
    # Preencher a tela
    win.fill((0, 0, 0))
    win.blit(background, (0,0))

    # Desenhar o Jogador
    jogador.draw(win)

    # Desenhar Enimigos
    for poke007 in wave1:
        poke007.draw(win)

    for chumbo in wave2:
        chumbo.draw(win)

    # Desenhar abilidades
    for skl001 in jogador.skill1s:
        skl001.drawSkill(win)

    for skl002 in jogador.skill2s:
        skl002.drawSkill(win)
    
    # Draw Tower
    win.blit(tower, (-50,55))
    
    # Vidas do jogador e pontos
    if jogador.alive == False:
        win.fill((0,0,0))
        font = pygame.font.Font ('freesansbold.ttf',32)
        text = font.render('You Died ! Press R to restart', True, (255,255,255))
        textRect = text.get_rect()
        textRect.center = (win_width//2, win_height//2)
        win.blit(text,textRect)
        if userInput[pygame.K_r]:
            jogador.alive = True
            jogador.lives = 1
            jogador.health = 30
            jogador.x = 150
            jogador.y = 310
            tower_health = 5
            kills = 0
            wave1.remove(poke007)
            if len(wave2) != 0:
                wave2.remove(chumbo)
    font = pygame.font.Font ('freesansbold.ttf',32)
    text = font.render('Lives: '+str(jogador.lives) + '| Tower Health: '+ str(tower_health) + '| Kill count: ' + str(kills), True, (0,0,0))
    win.blit(text, (150,20))



    # Delay de tacha de atualização
    pygame.time.delay(30)
    # Updade gráfico
    pygame.display.update()


#----------------------------------------------------------------------------------
# Instance jogador
jogador = PokemonPlayer('Bulbasaur', 30, 30, 150, 310)

# Instance de Inimigos
poke007 = PokemonEnemy('Squirtle', 30, 30, 750, 310, 2, 30, 45)
chumbo = PokemonEnemy('Chumbo', 90, 90, 750, 110, 2, 300, 300)

# Waves
wave1 = []
wave2 = []

# Pontos
kills = 0

# Torre
tower_health = 5

#----------------------------------------------------------------------------------
# Mainloop
run = True
while run:
    # Desligar o jogo no [X] da janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Ler Inputs do jogador
    userInput = pygame.key.get_pressed()

    # Movimento do Jogador
    jogador.move(userInput)
    jogador.jump_motion(userInput)
    # Utilização de Skills
    jogador.skillUse1(userInput,wave1,wave2,poke007,chumbo)
    jogador.skillUse2(userInput,wave1,wave2,poke007,chumbo) 

    # Enemy
    if len(wave1) == 0:
        poke007 = PokemonEnemy('Squirtle', 30, 30, 750, 310, 2, 30, 45)
        wave1.append(poke007)

    if len(wave2) == 0 and kills == 10:
            chumbo = PokemonEnemy('Chumbo', 180, 180, 750, 110, 2, 300, 300)
            wave2.append(chumbo)

    if len(wave2) == 0 and kills == 25:
            chumbo = PokemonEnemy('Chumbo', 300, 300, 750, 110, 2, 300, 300)
            wave2.append(chumbo)

    # Torre
    if tower_health == 0:
        jogador.alive = False

    for poke007 in wave1:
        poke007.move()
        poke007.hit(jogador)
        if poke007.x < 20:
            wave1.remove(poke007)
            tower_health -= 1
        if poke007.health <= 0:
            wave1.remove(poke007)
            kills += 1

    for chumbo in wave2:
        chumbo.move()
        chumbo.hit(jogador)
        if chumbo.x < 20:
            wave2.remove(chumbo)
            tower_health -= 3
        if chumbo.health <= 0:
            wave2.remove(chumbo)
            kills += 1
            
    draw_game()