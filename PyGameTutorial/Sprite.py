
import pygame

class Sprite(object):
    def __init__(self):
        self.R = pygame.Rect(0,0,16,16)
        self.frames=[
                   pygame.Rect(43, 9, 16, 16),
                   pygame.Rect(60, 9, 16, 16),
                   pygame.Rect(77, 9, 16, 16)]
        self.frame = 0.0;
        self.animationSpeed = 10.0
        self.hidden=False

    def MoveFrame(self,frametime):
        
        self.frame += frametime * self.animationSpeed;
        #print(self.frame,frametime)
        if self.frame >= len(self.frames):
           self.frame = 0;
        

