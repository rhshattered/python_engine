import pygame , sys, time


mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((500, 500), 0, 32)
font = pygame.font.SysFont("Arial", 18)
pos = 0

framerate = 60
velocity = 100
last_time = time.time()
fpsBool = True
logDT = False

def update_fps():
	fps = str(int(mainClock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text

while True:

    dt = time.time() - last_time
    last_time = time.time()

    screen.fill((0, 0, 0))
    screen.blit(update_fps(), (10, 0))

    r = pygame.Rect(pos, 200, 100, 100)
    pygame.draw.rect(screen, (255, 255, 255), r)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            if event.key == K_e:
                fpsBool = not fpsBool

            if event.key == K_0:
                logDT = not logDT

            if event.key == K_UP:
                if framerate * 2 < 1000:
                    framerate = framerate * 2
            
            if event.key == K_DOWN:
                if framerate > 30:
                    framerate = framerate / 2
    if fpsBool:
        pos += velocity * dt

    elif not fpsBool:
        pos -= velocity * dt

    if logDT:
        print("Delta Time: " + str(dt))


    pygame.display.update()
    mainClock.tick(framerate)