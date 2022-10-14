import pygame 
import sys
import time

from GameContext import GameContext
from GameLogic import GameLogic
from Renderer import Renderer
from Core import Core

# initialize pygame
pygame.init()
pygame.font.init()
pygame.font.get_init()
g = pygame.display.set_mode((400,600))

# https://www.geeksforgeeks.org/how-to-change-screen-background-color-in-pygame/

pygame.display.set_caption(f"Can't rotate this | Score: {str(Core.user_score)}")

gc = GameContext()
logic = GameLogic(gc)
renderer = Renderer(g, gc)

for x in range(0,4):
    for y in range(0,2):
        gc.SetCurrentBlock(2)
        gc.currentBlock.MoveHori(x*2)

        for z in range(0,23):
            logic.MoveBlockDown()
 
for x in range(0,3):  
    gc.SetCurrentBlock(1)
    gc.currentBlock.MoveHori(x*2)
    for z in range(0,23):
        logic.MoveBlockDown()
 
gc.SetCurrentBlock(0)
gc.currentBlock.MoveHori(8)   
for z in range(0,23):
    logic.MoveBlockDown()

gc.SetCurrentBlock(0)
gc.currentBlock.MoveHori(8)   

def handleKey(event, pos):
    
    if event.key == pygame.K_a:
        gc.leftDown = pos

    if event.key == pygame.K_d:
        gc.rightDown = pos

    if event.key == pygame.K_w:
        gc.upDown = pos

    if event.key == pygame.K_s:
        gc.downDown = pos

    if event.key == pygame.K_k:
        gc.rotL = pos

    if event.key == pygame.K_l:
        gc.rotR = pos

if __name__ == '__main__':
    running = True

    while running:  

        # update the title every frame
        pygame.display.set_caption(f"Can't rotate this | Score: {str(Core.user_score+1)}")
    
        newticks = pygame.time.get_ticks()
        gc.frameticks= newticks - gc.ticks

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                handleKey(event, True)
            
            elif event.type == pygame.KEYUP:
                handleKey(event, False)

            elif event.type == pygame.QUIT:  
                running = False

        logic.doLogic()

        renderer.renderFrame()
        time.sleep(0.033)

        gc.frametime = 0.033
        
    pygame.quit()
    sys.exit(f'\n\n\nYour final score: {str(Core.user_score+1)}')