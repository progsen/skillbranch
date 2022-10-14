import pygame 
from Sprite import Sprite

class Renderer(object):

    def __init__(self, g,gc):
        self.gc=gc
        self.g = g
        self.image = pygame.image.load('sprites.png')
        self.font1 = pygame.font.SysFont('freesanbold.ttf', 50)
        self.empty = Sprite()
        self.empty.frames=[pygame.Rect(2, 75, 16, 16)]
    
    def renderField(self):
        
        gc =self.gc
        for row in gc.field.F:
            blink=False
            if gc.field.F.index(row) in gc.lineDown:
                blink = gc.lineDownCycle %2==0
            
            for r in row:
                self.empty.R = r.R
                #pygame.draw.rect(self.g, (255,0,0), r.R,1)
                self.RenderObject(self.empty)
                if r.sprite is not None and blink == False:
                    self.RenderObject(r.sprite)


    def renderFrame(self):
        g= self.g
        g.fill( (0,0, 0))

        #render mario sprite test
        #self.RenderObject(self.gc.player)
        
        
        #render text test
        # text1 = self.font1.render('GeeksForGeeks', True, (0, 255, 0))
        #textRect1 = text1.get_rect()
        #g.blit(text1, textRect1)

        self.renderField()
        
        gc =self.gc 
        for s in gc.currentBlock.sprites:
            if s.hidden == False:
                self.RenderObject(s)

        pygame.display.flip()

    def RenderObject(self, renderObject):
        frame= int(renderObject.frame)
        area = renderObject.frames[frame]
        self.g.blit(self.image,renderObject.R,area =area)
        renderObject.MoveFrame(self.gc.frametime);





