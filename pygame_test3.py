import pygame
import sys
import random
import time                      
pygame.init()


clock = pygame.time.Clock()

mainfont = pygame.font.Font(None, 50)

screen = pygame.display.set_mode((400, 400))
skysurf = pygame.Surface((400,400))
skyrect = skysurf.get_rect(topleft = (0,0))
skysurf.fill('blue')

groundsurf = pygame.Surface((400, 100))
groundrect = groundsurf.get_rect(topleft = (0, 300))
groundsurf.fill('green')

woodsurf = pygame.Surface((30, 50))
woodrect = woodsurf.get_rect(topleft = (70, 250))
woodsurf.fill('brown')

leavessurf = pygame.Surface((90, 40))
leavesrect = leavessurf.get_rect(topleft = (40, 225))
leavessurf.fill('green')

sunsurf = pygame.Surface((60, 60))
sunrect = sunsurf.get_rect(topleft = (320, 50))
sunsurf.fill('yellow')

playersurf = pygame.Surface((30, 50))
playerrect = playersurf.get_rect(topleft = (0,100))
playersurf.fill('red')

punterosurf = pygame.Surface((20,20))
punterorect = punterosurf.get_rect(midtop = (0,0))
punterosurf.fill('purple')

moving_platform = pygame.Surface((50, 10))
moving_platform_rect = moving_platform.get_rect(topleft = (250, 200))
moving_platform.fill('brown')

youwin_background = pygame.Surface((500,500))
youwin_background.fill('black')

youwin = mainfont.render('you win', True, 'white')
def ganar():
    if playerrect.colliderect(sunrect):
        screen.blit(youwin_background, (0,0))
        screen.blit(youwin, (0,0 ))   
def gravedad_jugador(playerspeedY):
    playerspeedY = 6
    if playerrect.colliderect(groundrect) or playerrect.colliderect(moving_platform_rect):
        playerspeedY = 0
    playerrect.y += playerspeedY


        
    
def playermovement(button_press):
    button_press = pygame.key.get_pressed()
    if button_press[pygame.K_d]:
        playerrect.x += 2
    elif button_press[pygame.K_a]:
        playerrect.x -= 2
    elif button_press[pygame.K_w] and playerrect.colliderect(groundrect):
        playerrect.y -= 100 
    elif button_press[pygame.K_w] and playerrect.colliderect(moving_platform_rect):
        playerrect.y -= 100 
def salida ():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
def change ():
    if playerrect.colliderect(sunrect):
        open("proyecto_pygame_itla.py")
        exec("proyecto_pygame_itla.py")
while True:
    change()
    gravedad_jugador(0)
    playermovement(0)
    screen.blit(skysurf, skyrect)    
    screen.blit(groundsurf, groundrect)
    screen.blit(woodsurf, woodrect)
    screen.blit(leavessurf, leavesrect)
    screen.blit(sunsurf, sunrect)
    screen.blit(playersurf, playerrect)
    screen.blit(punterosurf,pygame.mouse.get_pos())
    screen.blit(moving_platform, moving_platform_rect)
  
    salida()
    

    
    clock.tick(30)
    pygame.display.update()