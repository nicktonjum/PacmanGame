#!/usr/bin/env python
# coding: utf-8

# In[37]:


import random
import sys
import pygame
import pygame.locals
from random import randint
from pygame import *

pygame.init()

#Mode 1 is windowed, using the screensize variable
#Mode 2 is full screen, using the screensize variable
#Mode 3 is full screen, automatically detecting the screen size
displaymode = 3
screensize = [1920, 1080]

#Game Options
start_time = 5 # Seconds from startup until the game starts.

tickrate = 60 # How many frames the game proceeds per second.
pacman_speed = 4 # How many pixels pacman will move every frame
shift_multiplier = 1.5 # When holding the turbo button (shift), pacman's speed is multiplied by this number
ghost_speed = 2 # How many pixels ghosts will move every frame
speed_increments = [1, 1] # After each level speeds will increase by this amount [pacman speed, ghost speed].
powerup_time = 300 # How many frames the powerup pellet will last
powerup_decrement = 10 # How many frames will be removed from the powerup time value after each level
resets = [20, 25, 50] # After how many levels should each value be reset [pacman speed, ghost speed, powerup time].
debug_info = 1
debug_font_size = 24
dumb_ghosts = 3 # How many "dumb" ghosts will spawn. These will move in random directions.
smart_ghosts = 1 # How many "smart" ghosts will spawn. These will target pacman.
pacman_spawn = [960, 540] # The coordinates where pacman will spawn at.
ghost_spawn = [screensize[0]/3, screensize[1]/3] # The coordinates where the ghosts will spawn.
hitbox = 60 #Pac-Man's hitbox size (pixels)
pacman_lives = 3


screeninfo = pygame.display.Info()
determinedssx = screeninfo.current_w
determinedssy = screeninfo.current_h

fpsClock = pygame.time.Clock()
background_color = (0,0,0)
start_time += 1
if displaymode == 1:
    screen = pygame.display.set_mode((screensize[0], screensize[1]))
elif displaymode == 2:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screensize = [determinedssx, determinedssy]



pygame.display.set_caption('Pac Man')
screen.fill(background_color)
pygame.display.flip()
running = True

pacchar = [pygame.image.load('pacman0.png'), pygame.image.load('pacman1.png'), pygame.image.load('pacman2.png')]
pacpos = pacman_spawn
pacdirection = 0
pacanim = 0
pacmanmoving = False
alive = True

font = pygame.font.SysFont('FreeSerif', debug_font_size)

def shutdowngame():
    pygame.quit()

    
ghostchar = [pygame.image.load('ghost0.png'), pygame.image.load('ghost1.png')]
ghostchar_rot = []
ghosts = []
ghostx = []
ghosty = []
ghostcolor = []
ghostdirection = []
state = []
ghosttype = []
turncooldown = []
deathanimation = 0
collidedghost = 0

def ghostsreset():
    ghostchar = [pygame.image.load('ghost0.png'), pygame.image.load('ghost1.png')]
    ghostchar_rot = []
    ghosts = []
    ghostx = []
    ghosty = []
    ghostcolor = []
    ghostdirection = []
    state = []
    ghosttype = []
    turncooldown = []
    deathanimation = 0

    
def spawn_ghost(id,pos,color,gtype):
    ghostchar_rot.append(ghostchar)
    ghosts.append(id)
    ghostx.append(pos[0])
    ghosty.append(pos[1])
    ghostcolor.append(color)
    ghostdirection.append(2)
    state.append(1)
    ghosttype.append(gtype)
    turncooldown.append(1)
    
def recolor(img, oldcolor, newcolor):
    recolored = pygame.Surface(img.get_size())
    recolored.fill(newcolor)
    img.set_colorkey(oldcolor)
    recolored.blit(img, (0,0))
    return recolored

rshift_antirepeat = False

while running:
    pygame.mouse.set_visible(False)
    pygame.event.get()    
    keys=pygame.key.get_pressed()
    screen.fill(background_color)
    statstext = "{} {} ({}x{}) [{}] {}({}) {} ({}, {}) {} ({}) [{}, {}, {}] ".format(int(pacpos[0]),int(pacpos[1]),screensize[0],screensize[1],tickrate,pacman_speed,shift_multiplier,ghost_speed,speed_increments[0],speed_increments[1],powerup_time,powerup_decrement,resets[0],resets[1],resets[2])
    statsdisp = font.render(statstext, False, (255, 255, 255))
    
    
        
    if keys[K_ESCAPE]:
        running = False
    

    
    if keys[K_RSHIFT]: ## Spawns a 'dumb' ghost with random color at a random position
        if not rshift_antirepeat:
            spawn_ghost(len(ghosts)+1,[randint(0,screensize[0]),randint(0,screensize[1])],(randint(0,255), randint(0,255), randint(0,255)),"dumb")
            rshift_antirepeat = True
    else:
        rshift_antirepeat = False
        
    if running == False:
            shutdowngame()
            
    if keys[K_UP]:
        pacmanmoving = True
        pacdirection = 1
    elif keys[K_RIGHT]:
        pacmanmoving = True
        pacdirection = 2
    elif keys[K_DOWN]:
        pacmanmoving = True
        pacdirection = 3
    elif keys[K_LEFT]:
        pacmanmoving = True
        pacdirection = 4
    
    if keys[K_LSHIFT]:
        pacman_newspeed = pacman_speed * shift_multiplier
    else:
        pacman_newspeed = pacman_speed
        
    if pacmanmoving == True:
        pacanim += 1
        if pacanim >= 9:
            pacanim = 0
        if pacdirection == 1:
            pacpos[1] -= pacman_newspeed
            pacman = pygame.transform.rotate(pacchar[pacanim//3], 90)
        elif pacdirection == 2:
            pacpos[0] += pacman_newspeed
            pacman = pygame.transform.rotate(pacchar[pacanim//3], 0)
        elif pacdirection == 3:
            pacpos[1] += pacman_newspeed
            pacman = pygame.transform.rotate(pacchar[pacanim//3], 270)
        elif pacdirection == 4:
            pacpos[0] -= pacman_newspeed
            pacman = pygame.transform.rotate(pacchar[pacanim//3], 180)
    if pacmanmoving == False:
        pacanim = 0
        pacman = pygame.transform.rotate(pacchar[pacanim//3], 0)
    
    
    for i in range(0,len(ghosts)):
        if len(ghosts) >= 1:
            if abs(ghostx[i] - pacpos[0]) < hitbox:
                if abs(ghosty[i] - pacpos[1]) < hitbox:
                    deathanimation = 300
                    collidedghost = i
        if ghostx[i] <= -64:
            ghostx[i] += screensize[0]+64
        if ghostx[i] >= screensize[0]:
            ghostx[i] -= screensize[0]+64
        if ghosty[i] <= -64:
            ghosty[i] += screensize[1]+64
        if ghosty[i] >= screensize[1]:
            ghosty[i] -= screensize[1]+64
        turncooldown[i] -= 1
        if turncooldown[i] <= 0:
            if ghosttype[i] == "dumb":
                ghostdirection[i] = randint(1,4)
            turncooldown[i] = randint(15,300)
        if ghostdirection[i] == 1:
            ghosty[i] -= 1
            ghostchar_rot[i] = pygame.transform.flip(ghostchar[pacanim//5], True, False)
        elif ghostdirection[i] == 2:
            ghostx[i] += 1
            ghostchar_rot[i] = pygame.transform.flip(ghostchar[pacanim//5], True, False)
        elif ghostdirection[i] == 3:
            ghosty[i] += 1
            ghostchar_rot[i] = ghostchar[pacanim//5]
        elif ghostdirection[i] == 4:
            ghostx[i] -= 1
            ghostchar_rot[i] = ghostchar[pacanim//5]
        else:
            ghostchar_rot[i] = ghostchar[pacanim//5]
            
        ghostchar_rot[i] = recolor(ghostchar_rot[i], (29, 184, 235), ghostcolor[i]).convert()
        ghostchar_rot[i].set_colorkey((0,0,0))
        screen.blit(ghostchar_rot[i], (ghostx[i], ghosty[i]))
    
    screen.blit(pacman, (pacpos[0],pacpos[1]))
    
    if pacpos[0] <= -64:
        pacpos[0] += screensize[0]+64
    if pacpos[0] >= screensize[0]:
        pacpos[0] -= screensize[0]+64
    if pacpos[1] <= -64:
        pacpos[1] += screensize[1]+64
    if pacpos[1] >= screensize[1]:
        pacpos[1] -= screensize[1]+64

    #Everything below this has to be ran at the end of the while loop
    while start_time >= 1:
        screen.fill(background_color)
        screen.blit(pacman, (pacpos[0],pacpos[1]))
        screen.blit(statsdisp, (0, 0))
        countdowntext = "Starting in {}..".format(start_time-1)
        cddisplay = font.render(countdowntext, False, (255, 255, 255))
        screen.blit(cddisplay, (screensize[0]/2 - debug_font_size, screensize[1]/2 - debug_font_size))
        pygame.display.update()
        fpsClock.tick(tickrate)
        pygame.time.wait(1000)
        start_time -= 1
        
    while deathanimation > 1:
        if 300 >= deathanimation >= 240:
            screen.fill(background_color)
            ghostchar_rot[collidedghost] = recolor(ghostchar_rot[collidedghost], (29, 184, 235), ghostcolor[collidedghost]).convert()
            ghostchar_rot[collidedghost].set_colorkey((0,0,0))
            screen.blit(ghostchar_rot[collidedghost], (ghostx[collidedghost], ghosty[collidedghost]))
            screen.blit(pacman, (pacpos[0],pacpos[1]))
        elif 240 > deathanimation >= 220:
            ghostchar_rot = []
            ghosts = []
            ghostx = []
            ghosty = []
            ghostcolor = []
            ghostdirection = []
            state = []
            ghosttype = []
            turncooldown = []
            screen.fill(background_color)
            pacman = pygame.transform.rotate(pacchar[2], 90)
            screen.blit(pacman, (pacpos[0],pacpos[1]))
        elif 220 > deathanimation >= 200:
            screen.fill(background_color)
            pacman = pygame.transform.rotate(pacchar[2], 180)
            screen.blit(pacman, (pacpos[0],pacpos[1]))
        elif 200 > deathanimation >= 180:
            screen.fill(background_color)
            pacman = pygame.transform.rotate(pacchar[2], 270)
            screen.blit(pacman, (pacpos[0],pacpos[1]))
        elif 180 > deathanimation >= 160:
            screen.fill(background_color)
            pacman = pygame.transform.rotate(pacchar[2], 0)
            screen.blit(pacman, (pacpos[0],pacpos[1]))
        elif 160 > deathanimation >= 140:
            screen.fill(background_color)
            pacman = pygame.transform.rotate(pacchar[2], 90)
            screen.blit(pacman, (pacpos[0],pacpos[1]))
        elif 140 > deathanimation >= 120:
            screen.fill(background_color)
            pacman = pygame.transform.rotate(pacchar[2], 180)
            screen.blit(pacman, (pacpos[0],pacpos[1]))
        elif 120 > deathanimation >= 100:
            screen.fill(background_color)
            pacman = pygame.transform.rotate(pacchar[2], 270)
            screen.blit(pacman, (pacpos[0],pacpos[1]))
        elif 100 > deathanimation >= 80:
            screen.fill(background_color)
            pacman = pygame.transform.rotate(pacchar[2], 0)
            screen.blit(pacman, (pacpos[0],pacpos[1]))
        elif 80 > deathanimation >= 60:
            screen.fill(background_color)
            pacman = pygame.transform.rotate(pacchar[2], 90)
            screen.blit(pacman, (pacpos[0],pacpos[1]))   
        elif deathanimation <= 2:
            pacpos[0] = 960
            pacpos[1] = 540
            pacdirection = 0
            pacanim = 0
            pacmanmoving = False
            
        pygame.display.update()
        fpsClock.tick(tickrate)
        deathanimation -= 1
        
    if debug_info == 1:
        screen.blit(statsdisp, (0, 0))
    pygame.display.update()
    fpsClock.tick(tickrate)


# In[ ]:





# In[ ]:




