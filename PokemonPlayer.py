from Pokemon import *
from Skill import *

class PokemonPlayer(Pokemon):
    # Construtor
    def __init__(self,name, health, fullHealth, x, y):
        super().__init__(health, fullHealth, x, y)
        # Nome
        self.name = name
        # Saltar
        self.jump = False
        # Abilidades
        self.skill1s = []
        self.skill2s = []
        self.cool_down_count1 = 0
        self.cool_down_count2 = 0
        # Hitbox
        self.hitbox = (self.x, self.y, 40, 40)
        # Vidas
        self.lives = 1
        self.alive = True
        self.invulnerable = False

        
    # Andar para os lados
    def move(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= 800 - 35:
            self.x += self.velx
            self.face_right = True
            self.face_left = False
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0

    # Saltar
    def jump_motion(self, userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vely*4
            self.vely -= 1
        if self.vely < -6:
            self.jump = False
            self.vely = 6

    # Saber o lado que o jodagor está a olhar
    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    # Desenhar o jogador, a vida, criar hitbox
    def draw(self, win):
        self.hitbox = (self.x, self.y, 40, 40)
        pygame.draw.rect(win, (255, 0, 0), (self.x + 15, self.y, 30, 10))
        if self.health >= 0:
            pygame.draw.rect(win, (0, 255, 0), (self.x + 15, self.y, self.health, 10))
        if self.stepIndex >= 21:
            self.stepIndex = 0
        if self.face_left:
            win.blit(Left_001[self.stepIndex // 3], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(Right_001[self.stepIndex // 3], (self.x, self.y))
            self.stepIndex += 1

    # Cooldown da 1ª abilidade
    def cooldown1(self):
        if self.cool_down_count1 >= 10:
            self.cool_down_count1 = 0
        elif self.cool_down_count1 > 0:
            self.cool_down_count1 += 1

    # Cooldown da 2ª abilidade
    def cooldown2(self):
        if self.cool_down_count2 >= 100:
            self.cool_down_count2 = 0
        elif self.cool_down_count2 > 0:
            self.cool_down_count2 += 1

    # 1ª abilidade
    def skillUse1(self,userInput,wave,wave2,enemy,enemy2):
        self.hit1(wave,wave2,enemy,enemy2)
        self.cooldown1()
        if userInput[pygame.K_f] and self.cool_down_count1 == 0:
            skl001 = Skill(self.x, self.y - 15, self.direction(), BulletSeed, 30, 30)
            self.skill1s.append(skl001)
            self.cool_down_count1 = 1
        for skl001 in self.skill1s:
            skl001.move()
            if skl001.x > 810 or skl001.x < 20:
                self.skill1s.remove(skl001)

    # 2ª abilidade
    def skillUse2(self,userInput,wave,wave2,enemy,enemy2):
        self.hit2(wave,wave2,enemy,enemy2)
        self.cooldown2()
        if userInput[pygame.K_d] and self.cool_down_count2 == 0:
            if self.direction() == 1:
                skl002 = Skill(self.x, self.y - 15, self.direction(), HyperBeam, 30, 120)
                self.skill2s.append(skl002)
                self.cool_down_count2 = 1
            elif self.direction() == -1:
                skl002 = Skill(self.x - 140, self.y - 15, self.direction(), HyperBeam_L, 30, 120)
                self.skill2s.append(skl002)
                self.cool_down_count2 = 1

        for skl002 in self.skill2s:
            if self.cool_down_count2 == 30:
                self.skill2s.remove(skl002)

    # Dano da 1ª abilidade
    def hit1(self,wave,wave2,enemy,enemy2):
        for enemy in wave:
            for skl001 in self.skill1s:
                if enemy.hitbox[0] < skl001.x < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < skl001.y < enemy.hitbox[1] + enemy.hitbox[3]:
                    enemy.health -= 5
                    self.skill1s.remove(skl001)

        for enemy2 in wave2:
            for skl001 in self.skill1s:
                if enemy2.hitbox[0] < skl001.x < enemy2.hitbox[0] + enemy2.hitbox[2] and enemy2.hitbox[1] < skl001.y < enemy2.hitbox[1] + enemy2.hitbox[3]:
                    enemy2.health -= 5
                    self.skill1s.remove(skl001)

    # Dano da 2ª abilidade
    def hit2(self,wave,wave2,enemy,enemy2):
    
        for enemy2 in wave2:
            for skl002 in self.skill2s:
                if enemy2.hitbox[0] < skl002.x + 120 < enemy2.hitbox[0] + enemy2.hitbox[2] and enemy2.hitbox[1] < skl002.y + 32 <enemy2.hitbox[1] + enemy2.hitbox[3] or enemy2.hitbox[0] < skl002.x + 30 < enemy2.hitbox[0] + enemy2.hitbox[2] and enemy2.hitbox[1] < skl002.y + 32 <enemy2.hitbox[1] + enemy2.hitbox[3] or enemy2.hitbox[0] < skl002.x + 75 < enemy2.hitbox[0] + enemy2.hitbox[2] and enemy2.hitbox[1] < skl002.y + 32 <enemy2.hitbox[1] + enemy2.hitbox[3]:
                    enemy2.health -= 3

        for enemy in wave:
            for skl002 in self.skill2s:
                if enemy.hitbox[0] < skl002.x + 120 < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < skl002.y + 32 <enemy.hitbox[1] + enemy.hitbox[3] or enemy.hitbox[0] < skl002.x + 30 < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < skl002.y + 32 <enemy.hitbox[1] + enemy.hitbox[3] or enemy.hitbox[0] < skl002.x + 75 < enemy.hitbox[0] + enemy.hitbox[2] and enemy.hitbox[1] < skl002.y + 32 <enemy.hitbox[1] + enemy.hitbox[3]:
                    enemy.health -= 2
                    