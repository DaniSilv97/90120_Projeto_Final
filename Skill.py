from PokemonPlayer import *
import pygame

class Skill:
    def __init__(self, x, y, direction, skillName,height,lenght):
        self.x = x + 25
        self.y = y + 25
        self.direction = direction
        self.skillName = skillName
        self.height = height
        self.lenght = lenght

    # Movimento da habilidade
    def move(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15

    # Desenhar a habilidade
    def drawSkill(self, win):
        win.blit(self.skillName, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.lenght, self.height)