import pygame
from sys import exit
import random
pygame.init()
 
mainfont = pygame.font.Font( None, 50)

x = 0
y = 37
fondo1 = pygame.Surface((1000,150))
fondorect1 = fondo1.get_rect(topleft = (0,0))
fondo1.fill('white')
 
fondo2= pygame.Surface((1000,150))
fondorect2 = fondo2.get_rect(topleft = (0, 151))
fondo2.fill('white')

avatarsurf = pygame.Surface((75, 75))
avatarect = avatarsurf.get_rect(topleft = (x, y))

screen= pygame.display.set_mode((600, 300))

projectilesurf = pygame.Surface((100, 37))
projectilerect = projectilesurf.get_rect(topleft = (700, 37))
projectilesurf.fill('black')

dianasurf = pygame.Surface((10, 1000 ))
dianarect = dianasurf.get_rect(topright = (0,0))


score = 0
ranx = 0

speed = 10
clock = pygame.time.Clock()


def disparo ():
    pass
    
        



def get_position():
    pressing = pygame.key.get_pressed()
    position = 1
    
    if pressing[pygame.K_w]:
        position = 1
    if pressing[pygame.K_s]:
        position = 2
    
    if position == 1:
        avatarect.y = 37
    if position == 2:
        avatarect.y = 187


def salida():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
medidor = False
while True:
    medidor = False
    text = mainfont.render(str(score),False,'black' )
    salida()
    get_position()
    disparo()
    screen.blit(fondo1, fondorect1)
    screen.blit(fondo2, fondorect2)
    screen.blit (avatarsurf, avatarect)
    screen.blit(projectilesurf, projectilerect)
    screen.blit(dianasurf, dianarect)
    screen.blit(text, (500, 20))
    
    if ranx == 1:
        projectilerect.y = 37
    else : 
        projectilerect.y = 187

    
    projectilerect.x -= speed
    if projectilerect.colliderect(avatarect):
        projectilerect.x = 1100
        score -= 500
        
    if projectilerect.colliderect(dianarect):
        projectilerect.x = 1100
        score += 100
        medidor = True 
    if medidor:
        ranx = random.randrange(1,3)
    
    if score >= 500:
        speed = 20
    elif score >= 1000:
        speed = 40
    elif score >= 1500:
        speed = 80
    elif score >= 2000:
        speed = 150
    elif score >= 2500:
        speed = 2000
    
    

  
    
    clock.tick(60)
    pygame.display.update()