import pygame
import os
import time
import random
pygame.font.init()


WIDTH, HEIGHT = 760,760
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#PacMan 
pacmanChar = [pygame.image.load('pacman0.png'),
              pygame.image.load('pacman1.png'),
              pygame.image.load('pacman2.png'),
              ] 

#Background
BG = pygame.transform.scale((pygame.image.load('background-black.png')), (WIDTH, HEIGHT))

def draw_map(color):
    x = 80
    # Border
    pygame.draw.line(WIN, color, (x,x),(600+x,x), 2)
    pygame.draw.line(WIN, color, (x,x),(x,240+x), 2)
    pygame.draw.line(WIN, color, (x,240+x),(0,240+x), 2)
    pygame.draw.line(WIN, color, (0,360+x),(x,360+x), 2)
    pygame.draw.line(WIN, color, (x,360+x),(x,600+x), 2)
    pygame.draw.line(WIN, color, (x,600+x),(600+x,600+x), 2)
    pygame.draw.line(WIN, color, (600+x,600+x),(600+x,360+x), 2)
    pygame.draw.line(WIN, color, (600+x,360+x),(760,360+x), 2)
    pygame.draw.line(WIN, color, (760,240+x),(600+x,240+x), 2)
    pygame.draw.line(WIN, color, (600+x,240+x),(600+x,x), 2)
    # Top
    pygame.draw.line(WIN, color, (40+x,40+x),(560+x,40+x), 2)
    # Top Left
    pygame.draw.line(WIN, color, (40+x,40+x),(40+x,240+x), 2) 
    pygame.draw.line(WIN, color, (40+x,240+x),(80+x,240+x), 2) 
    pygame.draw.line(WIN, color, (80+x,240+x),(80+x,280+x), 2) 
    pygame.draw.line(WIN, color, (80+x,280+x),(0,280+x), 2) 
    # Bottom Left
    pygame.draw.line(WIN, color, (0,320+x),(80+x,320+x), 2)
    pygame.draw.line(WIN, color, (80+x,320+x),(80+x,360+x), 2)
    pygame.draw.line(WIN, color, (80+x,360+x),(40+x,360+x), 2)
    pygame.draw.line(WIN, color, (40+x,360+x),(40+x,560+x), 2)
    # Bottom
    pygame.draw.line(WIN, color, (40+x,560+x),(560+x,560+x), 2)
    # Bottom Right
    pygame.draw.line(WIN, color, (560+x,560+x),(560+x,360+x), 2)
    pygame.draw.line(WIN, color, (560+x,360+x),(520+x,360+x), 2)
    pygame.draw.line(WIN, color, (520+x,360+x),(520+x,320+x), 2)
    pygame.draw.line(WIN, color, (520+x,320+x),(760,320+x), 2)
    pygame.draw.line(WIN, color, (760,280+x),(520+x,280+x), 2)
    pygame.draw.line(WIN, color, (520+x,280+x),(520+x,240+x), 2)
    pygame.draw.line(WIN, color, (520+x,240+x),(560+x,240+x), 2)
    pygame.draw.line(WIN, color, (560+x,240+x),(560+x,40+x), 2)
    # Top Left Block
    pygame.draw.line(WIN, color, (80+x,80+x),(80+x,200+x), 2)
    pygame.draw.line(WIN, color, (80+x,200+x),(120+x,200+x), 2)
    pygame.draw.line(WIN, color, (120+x,200+x),(120+x,120+x), 2)
    pygame.draw.line(WIN, color, (120+x,120+x),(200+x,120+x), 2)
    pygame.draw.line(WIN, color, (200+x,120+x),(200+x,80+x), 2)
    pygame.draw.line(WIN, color, (200+x,80+x),(80+x,80+x), 2)
    # Top Right Block
    pygame.draw.line(WIN, color, (400+x,80+x),(520+x,80+x), 2)
    pygame.draw.line(WIN, color, (520+x,80+x),(520+x,200+x), 2)
    pygame.draw.line(WIN, color, (520+x,200+x),(480+x,200+x), 2)
    pygame.draw.line(WIN, color, (480+x,200+x),(480+x,120+x), 2)
    pygame.draw.line(WIN, color, (480+x,120+x),(400+x,120+x), 2)
    pygame.draw.line(WIN, color, (400+x,120+x),(400+x,80+x), 2)
    # Bottom Left Block
    pygame.draw.line(WIN, color, (80+x,400+x),(80+x,520+x), 2)
    pygame.draw.line(WIN, color, (80+x,520+x),(200+x,520+x), 2)
    pygame.draw.line(WIN, color, (200+x,520+x),(200+x,480+x), 2)
    pygame.draw.line(WIN, color, (200+x,480+x),(120+x,480+x), 2)
    pygame.draw.line(WIN, color, (120+x,480+x),(120+x,400+x), 2)
    pygame.draw.line(WIN, color, (120+x,400+x),(80+x,400+x), 2)
    #Bottom Right Block
    pygame.draw.line(WIN, color, (400+x,520+x),(520+x,520+x), 2)
    pygame.draw.line(WIN, color, (520+x,520+x),(520+x,400+x), 2)
    pygame.draw.line(WIN, color, (520+x,400+x),(480+x,400+x), 2)
    pygame.draw.line(WIN, color, (480+x,400+x),(480+x,480+x), 2)
    pygame.draw.line(WIN, color, (480+x,480+x),(400+x,480+x), 2)
    pygame.draw.line(WIN, color, (400+x,480+x),(400+x,520+x), 2)
    # Low Middle Block
    pygame.draw.line(WIN, color, (240+x,520+x),(360+x,520+x), 2)
    pygame.draw.line(WIN, color, (360+x,520+x),(360+x,480+x), 2)
    pygame.draw.line(WIN, color, (360+x,480+x),(240+x,480+x), 2)
    pygame.draw.line(WIN, color, (240+x,480+x),(240+x,520+x), 2)
    # Bigger Low Middle Block
    pygame.draw.line(WIN, color, (120+x,320+x),(200+x,320+x), 2)
    pygame.draw.line(WIN, color, (200+x,320+x),(200+x,400+x), 2)
    pygame.draw.line(WIN, color, (200+x,400+x),(400+x,400+x), 2)
    pygame.draw.line(WIN, color, (400+x,400+x),(400+x,320+x), 2)
    pygame.draw.line(WIN, color, (400+x,320+x),(480+x,320+x), 2)
    pygame.draw.line(WIN, color, (480+x,320+x),(480+x,360+x), 2)
    pygame.draw.line(WIN, color, (480+x,360+x),(440+x,360+x), 2)
    pygame.draw.line(WIN, color, (440+x,360+x),(440+x,440+x), 2)
    pygame.draw.line(WIN, color, (440+x,440+x),(160+x,440+x), 2)
    pygame.draw.line(WIN, color, (160+x,440+x),(160+x,360+x), 2)
    pygame.draw.line(WIN, color, (160+x,360+x),(120+x,360+x), 2)
    pygame.draw.line(WIN, color, (120+x,360+x),(120+x,320+x), 2)
    # Ghost Spawn
    pygame.draw.line(WIN, color, (240+x,280+x),(240+x,360+x), 2)
    pygame.draw.line(WIN, color, (240+x,360+x),(360+x,360+x), 2)
    pygame.draw.line(WIN, color, (360+x,360+x),(360+x,280+x), 2)
    pygame.draw.line(WIN, color, (360+x,280+x),(240+x,280+x), 2)
    # Top Middle Trap
    pygame.draw.line(WIN, color, (240+x,80+x),(240+x,240+x), 2)
    pygame.draw.line(WIN, color, (240+x,240+x),(360+x,240+x), 2)
    pygame.draw.line(WIN, color, (360+x,240+x),(360+x,80+x), 2)
    pygame.draw.line(WIN, color, (360+x,80+x),(320+x,80+x), 2)
    pygame.draw.line(WIN, color, (320+x,80+x),(320+x,200+x), 2)
    pygame.draw.line(WIN, color, (320+x,200+x),(280+x,200+x), 2)
    pygame.draw.line(WIN, color, (280+x,200+x),(280+x,80+x), 2)
    pygame.draw.line(WIN, color, (280+x,80+x),(240+x,80+x), 2)
    # Upper Mid Left Thing
    pygame.draw.line(WIN, color, (120+x,280+x),(200+x,280+x), 2)
    pygame.draw.line(WIN, color, (200+x,280+x),(200+x,160+x), 2)
    pygame.draw.line(WIN, color, (200+x,160+x),(160+x,160+x), 2)
    pygame.draw.line(WIN, color, (160+x,160+x),(160+x,240+x), 2)
    pygame.draw.line(WIN, color, (160+x,240+x),(120+x,240+x), 2)
    pygame.draw.line(WIN, color, (120+x,240+x),(120+x,280+x), 2)
    # Upper Mid Right Thing
    pygame.draw.line(WIN, color, (400+x,160+x),(400+x,280+x), 2)
    pygame.draw.line(WIN, color, (400+x,280+x),(480+x,280+x), 2)
    pygame.draw.line(WIN, color, (480+x,280+x),(480+x,240+x), 2)
    pygame.draw.line(WIN, color, (480+x,240+x),(440+x,240+x), 2)
    pygame.draw.line(WIN, color, (440+x,240+x),(440+x,160+x), 2)
    pygame.draw.line(WIN, color, (440+x,160+x),(400+x,160+x), 2)
    

    
    
def all_cells_pacman_is_in(x, y):
    cell_len = 40
    
    list_of_cells = []
    
    # Adding extra row to top and left side
    row = (x + cell_len) // cell_len
    column = (y + cell_len) // cell_len
    
    list_of_cells.extend((row, column))
    
    
    
    
    # If pacman is centered in cell
    def is_centered_in_cell(x, y):
        cell_len = 40
        return (x % cell_len == cell_len/2) and (y % cell_len == cell_len/2)
    
    # If pacman is centered in cell on y axis
    def is_centered_y(y):
        cell_len = 40
        return (y % cell_len == cell_len/2)
    
    # If pacman is centered in cell on x axis
    def is_centered_x(x):
        cell_len = 40
        return (x % cell_len == cell_len/2)
    

    
    if not is_centered_in_cell(x, y):
        if is_centered_y(y):
            # Since the cell is 40, if the location of pacman is
            # less than 19 or greater than 19, we need to add the
            # adjacent cell the the list of cells pacman is in
            if (x + cell_len) % cell_len >= (cell_len / 2 + 1):
                list_of_cells.extend((row+1, column))
            
            elif (x + cell_len) % cell_len <= (cell_len / 2 - 1):
                list_of_cells.extend((row-1, column))
    
    
    
    if not is_centered_in_cell(x, y):
        if is_centered_x(x):
            # Since the cell is 40, if the location of pacman is
            # less than 19 or greater than 19, we need to add the
            # adjacent cell the the list of cells pacman is in
            if (y + cell_len) % cell_len >= (cell_len / 2 + 1):
                list_of_cells.extend((row, column+1))
            
            elif (y + cell_len) % cell_len <= (cell_len / 2 - 1):
                list_of_cells.extend((row, column-1))
    
    
    
    list_of_x_values = list_of_cells[::2]
    list_of_y_values = list_of_cells[1::2]
    
    output_list = []
    
    for index in range(len(list_of_x_values)):
        output_list.append((list_of_x_values[index], list_of_y_values[index]))
        
    return output_list
    
    
    
    

    
    
    
    
    
def where_is_pacman(x, y):
    cell_len = 40
    
    # Adding extra row to top and left side
    row = (x + cell_len) // cell_len
    column = (y + cell_len) // cell_len
    
    return (row, column)



def is_centered_in_cell(x, y):
    cell_len = 40
    return (x % cell_len == cell_len/2) and (y % cell_len == cell_len/2)   
    

def is_centered_y(y):
    cell_len = 40
    return (y % cell_len == cell_len/2)
    
    
def is_centered_x(x):
    cell_len = 40
    return (x % cell_len == cell_len/2)









pacman_movements = {
    # Column 4
    (4,4): {'can_up':False, 'can_down':True, 'can_left':False, 'can_right':True},
    (5,4): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (6,4): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (7,4): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (8,4): {'can_up':False, 'can_down':True, 'can_left':True, 'can_right':True},
    (9,4): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (10,4): {'can_up':False, 'can_down':True, 'can_left':True, 'can_right':True},
    (11,4): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (12,4): {'can_up':False, 'can_down':True, 'can_left':True, 'can_right':True},
    (13,4): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (14,4): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (15,4): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (16,4): {'can_up':False, 'can_down':True, 'can_left':True, 'can_right':False},
    
    
    # Column 5
    (4,5): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (8,5): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (10,5): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (12,5): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (16,5): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    
    # Column 6
    (4,6): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (6,6): {'can_up':False, 'can_down':True, 'can_left':False, 'can_right':True},
    (7,6): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (8,6): {'can_up':True, 'can_down':True, 'can_left':True, 'can_right':False},
    (10,6): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (12,6): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':True},
    (13,6): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (14,6): {'can_up':False, 'can_down':True, 'can_left':True, 'can_right':False},
    (16,6): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    
    # Column 7
    (4,7): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (6,7): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (8,7): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (10,7): {'can_up':True, 'can_down':False, 'can_left':False, 'can_right':False},
    (12,7): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (14,7): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (16,7): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    
    # Column 8
    (4,8): {'can_up':True, 'can_down':False, 'can_left':False, 'can_right':True},
    (5,8): {'can_up':False, 'can_down':True, 'can_left':True, 'can_right':True},
    (6,8): {'can_up':True, 'can_down':False, 'can_left':True, 'can_right':False},
    (8,8): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (12,8): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (14,8): {'can_up':True, 'can_down':False, 'can_left':False, 'can_right':True},
    (15,8): {'can_up':False, 'can_down':True, 'can_left':True, 'can_right':True},
    (16,8): {'can_up':True, 'can_down':False, 'can_left':True, 'can_right':False},
    
    # Column 9
    (5,9): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (8,9): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':True},
    (9,9): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (10,9): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (11,9): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (12,9): {'can_up':True, 'can_down':True, 'can_left':True, 'can_right':False},
    (15,9): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    
    # Column 10
    (-2,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (-1,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (0,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (1,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (2,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (3,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (4,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (5,10): {'can_up':True, 'can_down':True, 'can_left':True, 'can_right':True},
    (6,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (7,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (8,10): {'can_up':True, 'can_down':True, 'can_left':True, 'can_right':False},
    (12,10): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':True},
    (13,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (14,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (15,10): {'can_up':True, 'can_down':True, 'can_left':True, 'can_right':True},
    (16,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (18,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (19,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (20,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (21,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (22,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (23,10): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    
    
    # Column 11
    (5,11): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (8,11): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (12,11): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (15,11): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    
    # Column 12
    (4,12): {'can_up':False, 'can_down':True, 'can_left':False, 'can_right':True},
    (5,12): {'can_up':True, 'can_down':False, 'can_left':True, 'can_right':True},
    (6,12): {'can_up':False, 'can_down':True, 'can_left':True, 'can_right':False},
    (8,12): {'can_up':True, 'can_down':False, 'can_left':False, 'can_right':True},
    (9,12): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (10,12): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (11,12): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (12,12): {'can_up':True, 'can_down':False, 'can_left':True, 'can_right':False},
    (14,12): {'can_up':False, 'can_down':True, 'can_left':False, 'can_right':True},
    (15,12): {'can_up':True, 'can_down':False, 'can_left':True, 'can_right':True},
    (16,12): {'can_up':False, 'can_down':True, 'can_left':True, 'can_right':False},
    
    # Column 13
    (4,13): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (6,13): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (14,13): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (16,13): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    
    
    # Column 14
    (4,14): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (6,14): {'can_up':True, 'can_down':False, 'can_left':False, 'can_right':True},
    (7,14): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (8,14): {'can_up':False, 'can_down':True, 'can_left':True, 'can_right':True},
    (9,14): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (10,14): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (11,14): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (12,14): {'can_up':False, 'can_down':True, 'can_left':True, 'can_right':True},
    (13,14): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (14,14): {'can_up':True, 'can_down':False, 'can_left':True, 'can_right':False},
    (16,14): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    
    # Column 15
    (4,15): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (8,15): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (12,15): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    (16,15): {'can_up':True, 'can_down':True, 'can_left':False, 'can_right':False},
    
    # Column 16
    (4,16): {'can_up':True, 'can_down':False, 'can_left':False, 'can_right':True},
    (5,16): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (6,16): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (7,16): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (8,16): {'can_up':True, 'can_down':False, 'can_left':True, 'can_right':True},
    (9,16): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (10,16): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (11,16): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (12,16): {'can_up':True, 'can_down':False, 'can_left':True, 'can_right':True},
    (13,16): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (14,16): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (15,16): {'can_up':False, 'can_down':False, 'can_left':True, 'can_right':True},
    (16,16): {'can_up':True, 'can_down':False, 'can_left':True, 'can_right':False},

}    
    
defined_cells = pacman_movements.keys()    
    

    
def where_can_pacman_move(x, y):
    cells = all_cells_pacman_is_in(x, y) 
    
    if len(cells) == 1:
        return pacman_movements[cells[0]]
    else:
        movements = cells
        moves1 = movements[0]
        moves2 = movements[1]
        
        # New dictionary that checks if both are True to move, starts with them all False
        combining_movement_dict = {'can_up':False, 'can_down':False, 'can_left':False, 'can_right':False}
        
        # Changing movements to True if both cell allow movement in those directions
        for key in combining_movement_dict.keys():
            if pacman_movements[moves1][key] or pacman_movements[moves2][key]:
                combining_movement_dict[key] = True
            
            
        return combining_movement_dict
    
      

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    x = 380
    y = 540
    white = (255, 255, 255)
    main_font = pygame.font.SysFont('comicsans', 50)
    clock = pygame.time.Clock()
    
    player_vel = 1
    
    
    
    
    
    def redraw_window():
        map_color = (255, 255, 255)
        WIN.blit(BG, (0,0))
        # Rendering fonts for variables
        lives_label = main_font.render(f'Lives: {lives}', 1, (255,255,255))
        level_label = main_font.render(f'Level: {level}', 1, (255,255,255))
        coordinates = main_font.render(f'Co: {x} {y}', 1, (255,255,255))
        where_is_pac = main_font.render(f'Cell: {where_is_pacman(x, y)}', 1, (255,255,255))
        is_pac_centered = main_font.render(f'Centered? {is_centered_in_cell(x, y)}', 1, (255,255,255))
        is_centered_on_x_coordinate = main_font.render(f'C on X? {is_centered_x(x)}', 1, (255,255,255))
        is_centered_on_y_coordinate = main_font.render(f'C on Y? {is_centered_y(y)}', 1, (255,255,255))
        cells_pac_is_in = main_font.render(f'ALL CELLS: {all_cells_pacman_is_in(x, y)}', 1, (255,255,255))
        
        # Where on the screen will the data be
        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        WIN.blit(coordinates, (175,10))
        WIN.blit(where_is_pac, (410, 10))
        WIN.blit(is_pac_centered, (200,200))
        WIN.blit(is_centered_on_y_coordinate, (400,400))
        WIN.blit(is_centered_on_x_coordinate, (200,600))
        WIN.blit(cells_pac_is_in, (200,700))
        
        
        # Drawing pacman and hitbox
        radius = 20
        pygame.draw.circle(WIN, (255,255,0), (x, y), radius)
        pygame.draw.rect(WIN, (255, 255, 0), (x-radius, y-radius, radius*2, radius*2), 2)
        
        #Draw map
        draw_map(map_color)
        
        pygame.display.update()
        
        
    
    while run:
        clock.tick(FPS)
        redraw_window()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        
        movement = where_can_pacman_move(x, y)
        
        if keys[pygame.K_LEFT] and movement['can_left']:
                x -= player_vel
        if keys[pygame.K_RIGHT] and movement['can_right']:
                x += player_vel
        if keys[pygame.K_UP] and movement['can_up']:
                y -= player_vel
        if keys[pygame.K_DOWN] and movement['can_down']:
                y += player_vel
        
        
main()
