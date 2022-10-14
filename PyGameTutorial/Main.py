import pygame 
import sys
import time

from GameContext import GameContext
from GameLogic import GameLogic
from Renderer import Renderer



pygame.init()
#https://www.geeksforgeeks.org/how-to-change-screen-background-color-in-pygame/
pygame.font.init()
 
pygame.font.get_init()
running  = True
g = pygame.display.set_mode((400,600))

pygame.display.set_caption("Can't rotate tris")


gc = GameContext()
logic = GameLogic(gc)
renderer = Renderer(g,gc)
adown=False
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
#gc.SetCurrentBlock(2)
#gc.currentBlock.MoveHori(8)
def handleKeyUp(event):
    
    if event.key == pygame.K_a:
        gc.leftDown=False
    if event.key == pygame.K_d:
        gc.rightDown=False
    if event.key == pygame.K_w:
        gc.upDown=False
    if event.key == pygame.K_s:
        gc.downDown=False
    if event.key == pygame.K_k:
        gc.rotL=False
    if event.key == pygame.K_l:
        gc.rotR=False
        

def handleKeyDown(event):
    if event.key == pygame.K_a:
        gc.leftDown=True
    if event.key == pygame.K_d:
        gc.rightDown=True
    if event.key == pygame.K_w:
        gc.upDown=True
    if event.key == pygame.K_s:
        gc.downDown=True
    if event.key == pygame.K_k:
        gc.rotL=True
    if event.key == pygame.K_l:
        gc.rotR=True

while running:  
  
    newticks=pygame.time.get_ticks()
    gc.frameticks= newticks-gc.ticks
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.KEYDOWN:
           handleKeyDown(event);
        if event.type == pygame.QUIT:  
           running = False
    
    for event in events:
        if event.type == pygame.KEYUP:
            handleKeyUp(event);
    logic.doLogic()
    renderer.renderFrame()
    time.sleep(0.033)
    gc.frametime=0.033
    
    
pygame.quit()
sys.exit()

