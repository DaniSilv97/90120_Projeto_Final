import pygame
import os

# Pokemons ------------------------------------------------------------------
# Imgs Bulbasaur #001
Left_001 = [pygame.image.load(os.path.join("Assets/Pokemons/001", "L1.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/001", "L2.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/001", "L3.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/001", "L4.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/001", "L5.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/001", "L6.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/001", "L7.gif"))
            ]

Right_001 = [pygame.image.load(os.path.join("Assets/Pokemons/001", "R1.gif")),
             pygame.image.load(os.path.join("Assets/Pokemons/001", "R2.gif")),
             pygame.image.load(os.path.join("Assets/Pokemons/001", "R3.gif")),
             pygame.image.load(os.path.join("Assets/Pokemons/001", "R4.gif")),
             pygame.image.load(os.path.join("Assets/Pokemons/001", "R5.gif")),
             pygame.image.load(os.path.join("Assets/Pokemons/001", "R6.gif")),
             pygame.image.load(os.path.join("Assets/Pokemons/001", "R7.gif"))
             ]

# Img Squirtle #007
Left_007 = [pygame.image.load(os.path.join("Assets/Pokemons/007", "L1.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/007", "L2.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/007", "L3.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/007", "L4.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/007", "L5.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/007", "L6.gif")),
            pygame.image.load(os.path.join("Assets/Pokemons/007", "L7.gif"))
            ]
# Img Chumbo #chumbo
Left_chumbo = [pygame.image.load(os.path.join("Assets/Pokemons", "chumbo.gif"))]
            


# Skills ---------------------------------------------------------------------
# Skill 1
BulletSeed = pygame.image.load(os.path.join("Assets/Skills","BulletSeed.gif"))

# Skill 2
HyperBeam = pygame.image.load(os.path.join("Assets/Skills","HyperBeam.gif"))
HyperBeam_L = pygame.image.load(os.path.join("Assets/Skills","HyperBeam_L.gif"))

# Torre ----------------------------------------------------------------------
tower = pygame.image.load(os.path.join("Assets", "Tower.gif"))