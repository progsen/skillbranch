import pygame
import random
from Sprite import Sprite
from GameField import GameField
from BlockObject import BlockObject

class GameContext(object):
  def __init__(self):
    self.player= Sprite()
    self.rightDown=False
    self.leftDown=False
    self.upDown=False
    self.downDown=False
    self.rotR=False
    self.rotL=False
    self.ticks=pygame.time.get_ticks()
    self.frameticks=0
    self.frametime=0
    self.downcount=1/0.033
    self.inputdown=0
    self.sprites = [23,84,103,122,141,160,179]
    self.lineDown = []
    self.lineDownCycle = 0
    self.blockTypes = [
        [#long
            [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]],
            [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]]
            ],

        [#pyra
            [[0,0,0],[1,1,1],[0,1,0]],
            [[0,1,0],[1,1,0],[0,1,0]],
            [[0,1,0],[1,1,1],[0,0,0]],
            [[0,1,0],[0,1,1],[0,1,0]]
            ],
        [#block
            [[1,1],[1,1]],
            ],

        [#L
            [[0,0,0],[1,1,1],[0,0,1]],
            [[0,1,0],[0,1,0],[1,1,0]],
            [[1,0,0],[1,1,1],[0,0,0]],
            [[0,1,1],[0,1,0],[0,1,0]],
            ],
        [#inverseL
            [[0,0,0],[1,1,1],[1,0,0]],
            [[1,1,0],[0,1,0],[0,1,0]],
            [[0,0,1],[1,1,1],[0,0,0]],
            [[0,1,0],[0,1,0],[0,1,1]],
            ],
        [#z
            [[0,1,1],[1,1,0],[0,1,1]],
            [[0,1,0],[1,1,1],[1,0,1]]
            ],
        [#inverse z
            [[0,0,0],[0,1,1],[1,1,0]],
            [[0,1,0],[0,1,1],[0,0,1]]
            ],
      
        ]
    self.field = GameField(100,100)
    self.RandomNewBlock();


  def RandomNewBlock(self):

    random_item = random.choice(self.blockTypes)
    self.currentBlock = BlockObject(random_item,self.field.sx,self.field.sy,
                                    self.sprites[self.blockTypes.index(random_item)]
    )
  def SetCurrentBlock(self,i):

    self.currentBlock = BlockObject(self.blockTypes[i],
                                    self.field.sx,
                                    self.field.sy,
                                    
                                    
                                    self.sprites[i])



