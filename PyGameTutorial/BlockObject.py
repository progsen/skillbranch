from re import X
from pygame import Rect
from Sprite import Sprite

class BlockObject(object):

  def __init__(self,blocks,x,y,gfx):
    self.sprites=[]
    self.blocks = blocks
    self.isDropping=False
    self.rot =0
    self.gfx= gfx

    self.Rect = Rect(
        x,
        y, 
        16 * len(self.blocks[0]), 
        16 * len(self.blocks[0][0])
    )

    self.MakeSprites()

  def MoveDown(self):
      self.Rect.y+= 16
      for s in self.sprites:
          s.R.y+= 16


  def MoveUp(self):
      self.Rect.y-= 16
      for s in self.sprites:
          s.R.y-= 16


  def MoveHori(self,dx):
      self.Rect.x+= dx*16

      for s in self.sprites:
          s.R.x+= dx*16

  def TopLeft(self):
    minx = 90000
    miny = 900000

    for s in self.sprites:
        if s.R.x < minx:
            minx = s.R.x

        if s.R.y < miny:
            miny = s.R.y

    return (minx,miny)

  def MakeSprites(self):
    self.sprites=[]


    for y in range(0,len(self.blocks[self.rot])):
        yrow = self.blocks[self.rot][y]

        for x in range(0,len(yrow)):

            if yrow[x] == 1:

                s = Sprite()
                s.frames=[Rect(
                    self.gfx, 
                    75, 
                    16, 
                    16
                )]

                s.R.x = x * 16
                s.R.y = y * 16

                s.R.x+=self.Rect.x
                s.R.y+=self.Rect.y

                self.sprites.append(s)

  def Rotate(self,left):    
    if left:
        self.rot -= 1

    else:
        self.rot+= 1

    if self.rot >= len(self.blocks):
        self.rot =0

    elif self.rot < 0:
        self.rot= len(self.blocks)-1

    self.MakeSprites()






