import pygame


class FieldBlock(object):
    def __init__(self,x,y,size):
        self.R = pygame. Rect(x,y,size,size)
        self.sprite=None

class GameField(object):
    def __init__(self,sx,sy):
        self.F=[];
        self.sx=sx
        self.sy=sy
        self.blocksize=16
        for y in range(24):
            self.F.append([]);
            for x in range(10):
                self.F[y].append(FieldBlock((x* self.blocksize)+sx,
                                            (y* self.blocksize)+sy, self.blocksize))
    def printField(self):
        i =0
        for r in self.F:
            line=str(i)+":"
            for x in r:
                if(x.sprite is not None):
                    line += "X,"
                    #str(x.sprite.frames[0].x)+
                else:
                    line+= " ,"
            print(line)
            i+=1

    def ClearLine(self,rowI):
            row = self.F[rowI]
            for x in range(0,len(row)):
                row[x].sprite=None

    def ClearLines(self,lineDown):
        self.printField()
        for rowI in lineDown:
            self.ClearLine(rowI)
        self.printField()
 

    def DragLineDownTo(self,rowI):
           
        for r in reversed(range(1,rowI+1)):
            y =  self.sy + (r*self.blocksize)
            for x in range(0,len(self.F[r])):
                self.F[r][x].sprite = self.F[r-1][x].sprite
                if self.F[r][x].sprite is not None:
                    self.F[r][x].sprite.R.y = y
        
        self.ClearLine(0)

    def GetLineDown(self,block):
        
        linesDown =[]
        yI = []
        for s in block.sprites:
            relY = s.R.y-self.sy
            try:
                yI.index(relY) 
            except ValueError:
                yI.append(relY)
                print("checkline ", yI)

        for rowI in yI:#reversed( yI):
            count=0
            row = self.F[int(rowI/16)]
            for fb in row:
                if fb.sprite is not None:
                    count+=1
            if count == len(row):
                print("linecomplete")
                linesDown.append( self.F.index(row))

        print(linesDown)
        return linesDown
    def Overlaps(self, block):

        for s in block.sprites:
            for row in self.F:
                for fb in row:
                    if fb.sprite is not None and fb.R.x == s.R.x and fb.R.y == s.R.y:
                        return True
        return False
    
    def MovedOutsideVerti(self,block):
        for s in block.sprites:
            if s.R.bottom > self.F[len(self.F)-1][0].R.bottom:
                return True
        return False
    def MovedOutsideHori(self,block):
        for s in block.sprites:
            if s.R.left <self.F[0][0].R.x:
               return True
            if s.R.x >= self.F[0][len(self.F[0])-1].R.right:
               return True
        return False
    
    def Rotate(left):

        pass
    def PutBlock(self, s):
        
        for row in self.F:
            for fb in row:
                if fb.R.x == s.R.x and fb.R.y == s.R.y:
                    fb.sprite = s
                    return
