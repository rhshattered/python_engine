import pygame , sys, time, pygame_gui
import psutil

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
HEIGHT = 500
WIDTH = 500
C1CIRCUMFRENCE = 75
screen = pygame.display.set_mode((HEIGHT, WIDTH), 0, 32)
pygame.display.set_caption("Python Engine")
font = pygame.font.SysFont("Arial", 18)
posx = WIDTH/2
posy = HEIGHT/2
framerate = 60
velocity = 100
last_time = time.time()
logDT = False
xBool = True
yBool = False
def update_fps():
	fps = str(int(mainClock.get_fps()))
	fps_text = font.render("FPS: " + fps, 1, pygame.Color("coral"))
	return fps_text

def update_posx():
    posx_text = font.render("Posx: " + str(int(posx)), 1, pygame.Color("coral"))
    return posx_text
    
def update_posy():
    posy_text = font.render("Posy: " + str(int(posy)), 1, pygame.Color("coral"))
    return posy_text

def drawhud_elements(): 
    screen.blit(update_fps(), (10, 0))
    screen.blit(update_posx(), (100, 0))
    screen.blit(update_posy(), (190, 0))

while True:
    dt = time.time() - last_time
    last_time = time.time()
    prevPos = posx
    screen.fill((0, 0, 0))
    # r = pygame.Rect(pos, 200, 100, 100)
    pygame.draw.circle(screen, (0, 0, 255),  (posx, posy), C1CIRCUMFRENCE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            if event.key == K_a:
                xBool = not xBool
                yBool = not yBool

            if event.key == K_0:
                logDT = not logDT

            if event.key == K_UP:
                if framerate * 2 < 1000:
                    framerate = framerate * 2
            
            if event.key == K_DOWN:
                framerate = framerate / 2
    
    keys_pressed = pygame.key.get_pressed()

    if xBool and posx < WIDTH - C1CIRCUMFRENCE:
        posx += velocity * dt
        if posy < HEIGHT - C1CIRCUMFRENCE:
            posy += velocity * dt
    elif not xBool and posx > C1CIRCUMFRENCE:
        posx -= velocity * dt
        if posy > C1CIRCUMFRENCE:
            posy -= velocity * dt


    if logDT:
        print("Delta Time: " + str(dt))
   # print("Position Y: " + str(posy))
    drawhud_elements()
    pygame.display.update()
    mainClock.tick(framerate)