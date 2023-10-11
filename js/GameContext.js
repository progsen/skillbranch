
class GameContext
{
   constructor()
   {
    this.player= new Sprite()
    this.rightDown=false
    this.leftDown=false
    this.upDown=false
    this.downDown=false
    this.rotR=false
    this.rotL=false
    this.ticks=0;//pygame.time.get_ticks()
    this.frameticks=0
    this.frametime=0
    this.downcount=1/0.033
    this.inputdown=0
    this.sprites = [23,84,103,122,141,160,179]
    this.lineDown = []
    this.lineDownCycle = 0
    this.blockTypes = [
        [////long
            [[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]],
            [[0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0]]
            ],

        [//pyra
            [[0,0,0],[1,1,1],[0,1,0]],
            [[0,1,0],[1,1,0],[0,1,0]],
            [[0,1,0],[1,1,1],[0,0,0]],
            [[0,1,0],[0,1,1],[0,1,0]]
            ],
        [//block
            [[1,1],[1,1]],
            ],

        [//L
            [[0,0,0],[1,1,1],[0,0,1]],
            [[0,1,0],[0,1,0],[1,1,0]],
            [[1,0,0],[1,1,1],[0,0,0]],
            [[0,1,1],[0,1,0],[0,1,0]],
            ],
        [//inverseL
            [[0,0,0],[1,1,1],[1,0,0]],
            [[1,1,0],[0,1,0],[0,1,0]],
            [[0,0,1],[1,1,1],[0,0,0]],
            [[0,1,0],[0,1,0],[0,1,1]],
            ],
        [//z
            [[0,0,0],[1,1,0],[0,1,1]],
            [[0,1,0],[1,1,0],[1,0,0]]
            ],
        [//inverse z
            [[0,0,0],[0,1,1],[1,1,0]],
            [[0,1,0],[0,1,1],[0,0,1]]
            ],
      
        ]
    this.field =new GameField(100,100)
    this.RandomNewBlock();
   }


   RandomNewBlock()
   {

   
        let i = Math.floor(Math.random() *this.blockTypes.length);
        let  random_item = this.blockTypes[i]
        this.currentBlock = new BlockObject(random_item,this.field.sx,this.field.sy, this.sprites[i])
   }
   SetCurrentBlock(i)
   {

        this.currentBlock =new  BlockObject(this.blockTypes[i],
                                        this.field.sx,
                                        this.field.sy,                                   
                                        
                                        this.sprites[i])

    }
}

