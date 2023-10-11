from re import X
from pygame import Rect
from Sprite import Sprite

class BlockObject(object):

  def __init__(self,blocks,x,y,gfx):
    self.sprites=[]
    self.blocks = blocks;
    self.isDropping=False
    self.rot =0
    self.gfx= gfx
    self.R = Rect(x,y, 16*len(self.blocks[0]), 16*len(self.blocks[0][0]))
    self.MakeSprites()


  def MoveDown(self):
      self.R.y+= 16
      for s in self.sprites:
          s.R.y+= 16


  def MoveUp(self):
      self.R.y-= 16
      for s in self.sprites:
          s.R.y-= 16


  def MoveHori(self,dx):
      self.R.x+= dx*16

      for s in self.sprites:
          s.R.x+= dx*16

  def TopLeft(self):
    minx = 90000
    miny=900000

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
                s.frames=[Rect(self.gfx, 75, 16, 16)]
                s.R.x =x*16
                s.R.y = y*16
                s.R.x+=self.R.x
                s.R.y+=self.R.y
                self.sprites.append(s)
   #for pair in self.blocks[self.rot]:
   #    s = Sprite()
   #    s.frames=[Rect(self.gfx, 75, 16, 16)]
   #    s.R.x = pair[0]*16
   #    s.R.y = pair[1]*16
   #    s.R.x+=x
   #    s.R.y+=y
   #    self.sprites.append(s)

  def Rotate(self,left):
    currentBlockDef= self.blocks[self.rot]
    topleft = self.TopLeft()


    start = (self.sprites[0].R.x,self.sprites[0].R.y)
    
    if left:
        self.rot -= 1
    else:
        self.rot+= 1
    if self.rot >= len(self.blocks):
        self.rot =0
    elif self.rot < 0:
        self.rot= len(self.blocks)-1
    self.MakeSprites()






