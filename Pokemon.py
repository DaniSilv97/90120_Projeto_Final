from LoadImages import *

class Pokemon:
    def __init__(self, health, fullHealth, x, y):
        # Movimento
        self.x = x
        self.y = y
        self.velx = 6
        self.vely = 6
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0

        # HP
        self.health = health
        self.fullHealth = fullHealth
