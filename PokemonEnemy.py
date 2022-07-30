from Pokemon import *

class PokemonEnemy(Pokemon):
    # Construtor
    def __init__(self, name, health, fullHealth, x, y, speed,height,lenght):
        super().__init__(health, fullHealth, x, y)
        self.name = name
        self.speed = speed
        self.height = height
        self.length = lenght

    # Andar
    def move(self):
        self.x -= self.speed

    # Frames de animação
    def step(self):
        if self.stepIndex >= 21:
            self.stepIndex = 0

    # Desenhar o enimigo
    def draw(self, win):
        self.hitbox = (self.x, self.y, self.height, self.length)
        pygame.draw.rect(win, (255, 0, 0), (self.x + 15, self.y, self.fullHealth, 10))
        if self.health >= 0:
            pygame.draw.rect(win, (0, 255, 0), (self.x + 15, self.y, self.health, 10))    
        self.step()
        if self.name == 'Chumbo':
            if self.health > 0:
                win.blit(Left_chumbo[0], (self.x, self.y))
                self.stepIndex += 1
        else:
            if self.health > 0:
                win.blit(Left_007[self.stepIndex // 3], (self.x, self.y))
                self.stepIndex += 1

    # Tirar vida ao jogador
    def hit(self,player):
        if player.hitbox[0] < self.x + 32 < player.hitbox[0] + player.hitbox[2] and player.hitbox[1] < self.y + 32 <player.hitbox[1] + player.hitbox[3]:
            if player.health > 0:
                player.health -= 1
                if player.health == 0 and player.lives > 0:
                    player.lives -= 1
                    player.health = 30
                    player.x = 150
                    player.y = 310
                elif player.health  == 0 and player.lives == 0:
                    player.alive = False    