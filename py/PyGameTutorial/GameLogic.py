
                             


from this import d
from BlockObject import BlockObject

class GameLogic(object):
    def __init__(self, gc):
        self.gc=gc
       
    def stopInput(self):
        self.gc.inputdown=3
    
    def InverseBlockMovement(self,block,dx,dy):
        if dy == 1:
            block.MoveUp()
        if dx == -1:
            block.MoveHori(1)
        if dx == 1:
            block.MoveHori(-1)
    def CheckBlockCollisions(self,block,dx,dy):
        
        if self.gc.field.Overlaps(block):
            self.InverseBlockMovement(block,dx,dy)
            if(dx == 0):#downward movement found overlap = stuck
                self.LockCurrentBlock()

        elif self.gc.field.MovedOutsideHori(block):
            self.InverseBlockMovement(block,dx,dy)

        elif self.gc.field.MovedOutsideVerti(block):
            self.InverseBlockMovement(block,dx,dy)
            self.LockCurrentBlock()
            


    def MoveBlockDown(self):
        block = self.gc.currentBlock

        block.MoveDown()
        self.CheckBlockCollisions(block,0,1)
            

    def LockCurrentBlock(self):
        for s in self.gc.currentBlock.sprites:
            self.gc.field.PutBlock(s)

        self.gc. lineDown = self.gc.field.GetLineDown(self.gc.currentBlock)
        if(len(self.gc.lineDown)>0):
            self.gc.lineDownCycle=10
        print("self.gc. lineDown",self.gc. lineDown)

        self.gc.RandomNewBlock();

    def doLogic(self):
        gc = self.gc
        gc.downcount-=1
        if(gc.lineDownCycle>0):
            gc.lineDownCycle-=1
            if(gc.lineDownCycle == 0):
                #gc.field.ClearLines(gc.lineDown)
                for line in gc.lineDown:
                    gc.field.DragLineDownTo(line)
                gc.lineDown=[]
            return

        if(gc.inputdown > 0):
            gc.inputdown-=1

        if gc.downcount <= 0 and gc.currentBlock.isDropping == False:
            self.MoveBlockDown()
            gc.downcount=30
        if gc.currentBlock.isDropping:
            self.MoveBlockDown()
            gc.downcount=3

        if gc.rightDown and gc.inputdown == 0:
            gc.currentBlock.MoveHori(1)
            self.CheckBlockCollisions(gc.currentBlock,1,0)
            self.stopInput()
            #gc.player.R.x+=1
        if gc.leftDown and gc.inputdown == 0:
            gc.currentBlock.MoveHori(-1)
            self.CheckBlockCollisions(gc.currentBlock,-1,0)
            self.stopInput()
            #gc.player.R.x-=1
            
        if gc.rotL and gc.inputdown == 0:
            self.rotateCurrent(True)
        if gc.rotR and gc.inputdown == 0:
            self.rotateCurrent(False)
        #if gc.upDown:
            #gc.player.R.y-=1
        if gc.downDown:
            gc.currentBlock.isDropping = True
        else:
            gc.currentBlock.isDropping = False

    def rotateCurrent(self,left):
        self.gc.currentBlock.Rotate(left)
        block= self.gc.currentBlock

        if self.gc.field.Overlaps(block):
            self.gc.currentBlock.Rotate(left==False)
            #if(dx == 0):
            #    self.LockCurrentBlock()

        elif self.gc.field.MovedOutsideHori(block):
            self.gc.currentBlock.Rotate(left==False)

        elif self.gc.field.MovedOutsideVerti(block):
            self.gc.currentBlock.Rotate(left==False)
            self.LockCurrentBlock()
        self.stopInput()




