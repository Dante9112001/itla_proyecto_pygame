import pygame
import random
import time
from sys import exit
pygame.init()
clock = pygame.time.Clock()

limite_salto = 15

backgroundS = pygame.Surface((1000, 400))
backgroundrect = backgroundS.get_rect(topleft = (0,0))
backgroundS.fill('blue')

ground1S = pygame.Surface((60, 100))
ground1rect = ground1S.get_rect(topleft = (0, 300))
ground1S.fill('green')


ground2S = pygame.Surface((70, 100))
ground2rect = ground2S.get_rect(topleft = ( 930, 300))
ground2S.fill('green')

sunsurf = pygame.Surface((40,40))
sunrect = sunsurf.get_rect(topleft = (900, 50))
sunsurf.fill('yellow')

playersurf = pygame.Surface((10,20))
playerrect = playersurf.get_rect(topleft = (0, 280))
playersurf.fill('red')

plataformaunosurf = pygame.Surface((50, 10))
plataformaunorect = plataformaunosurf.get_rect(topleft = (60, 260))
plataformaunosurf.fill('brown')

platdosur = pygame.Surface((100,10))
platdorect = platdosur.get_rect(topleft = (280, 300))

plattrisur = pygame.Surface((100,10))
plattrirect = plattrisur.get_rect(topleft = (480, 260))
plattrisur.fill('brown')

platcuasur = pygame.Surface((100,10))
platcuarect = platcuasur.get_rect(topleft = (700, 220))
platcuasur.fill('brown')
screen = pygame.display.set_mode((1000, 400))

cloudsurf = pygame.Surface((200, 60))
cloudsurf.fill('white')



gameovercol = pygame.Surface((1000, 20))
gameoverrect = gameovercol.get_rect(topleft= (0, 1000))
def gravedad():
    fuerzagrav = 5
    if playerrect.colliderect(ground1rect) or playerrect.colliderect(ground2rect) or playerrect.colliderect(plataformaunorect) or playerrect.colliderect(platdorect) or playerrect.colliderect(plattrirect) or playerrect.colliderect(platcuarect)  :
        fuerzagrav = 0
    playerrect.y += fuerzagrav
def playermovement():    
    pressing = pygame.key.get_pressed()
    saltolim = 10000
    if pressing[pygame.K_d]:
        playerrect.x += 8
    if pressing[pygame.K_a]:
        playerrect.x -= 8
    if  pressing[pygame.K_w] and playerrect.colliderect(ground1rect):
        for i in range(0, limite_salto):
            playerrect.y -= i
    if  pressing[pygame.K_w] and playerrect.colliderect(ground2rect):
        for i in range(0, limite_salto):
            playerrect.y -= i
    if  pressing[pygame.K_w] and playerrect.colliderect(plataformaunorect):
        for i in range(0, limite_salto):
            playerrect.y -= i
    if  pressing[pygame.K_w] and playerrect.colliderect(platdorect):
        for i in range(0, limite_salto):
            playerrect.y -= i
    if  pressing[pygame.K_w] and playerrect.colliderect(plattrirect):
        for i in range(0, limite_salto):
            playerrect.y -= i
    if  pressing[pygame.K_w] and playerrect.colliderect(platcuarect):
        for i in range(0, limite_salto):
            playerrect.y -= i   
def salida():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



         
while True:

    gravedad()
    salida()
    playermovement()    
    screen.blit(backgroundS, backgroundrect)
    screen.blit(cloudsurf, (100, 200))    
    screen.blit(ground1S, ground1rect)
    screen.blit(sunsurf, sunrect)
    screen.blit(playersurf, playerrect)
    screen.blit(ground2S, ground2rect)
    screen.blit(plataformaunosurf, plataformaunorect)
    screen.blit(platdosur, platdorect)
    screen.blit(plattrisur, plattrirect)
    screen.blit(platcuasur, platcuarect)
    screen.blit(gameovercol, gameoverrect)
    
    clock.tick(30)
    pygame.display.update()