

class FieldBlock
{
     constructor(x,y,size)
     {
        this.R = new Rect(x,y,size,size)
        this.sprite=null
     }
}

class GameField
{
     constructor(sx,sy)
     {
        this.F=[];
        this.sx=sx
        this.sy=sy
        this.blocksize=16
        for (let y = 0 ; y < 24;y++)
        {
            this.F.push([]);
            for (let x =0 ; x <  10;x++)
            {
                let b=new FieldBlock((x* this.blocksize)+sx, (y* this.blocksize)+sy, this.blocksize)
                this.F[y].push(b)
            }
        }
    }

    printField()
    {
        let   i =0
        for (let r in this.F)
        {
            r= this.F[r];

            let line=i+"{"
            for (let x in r)
            {
                x = r[x];
                if(x.sprite !=null)
                {
                    line += "X,"
                    //#str(x.sprite.frames[0].x)+
                }
                else
                {
                    line+= " ,"
                }
            }
            console.log(line)
            i+=1
        }
    }

     ClearLine(rowI)
     {
            let    row = this.F[rowI]
            for (let x = 0 ; x < row.length;x++)
            {
                row[x].sprite=null
            }
    }
     ClearLines(lineDown)
     {
        this.printField()
        for (let rowI in lineDown)
        {
            rowI = lineDown[rowI]
            this.ClearLine(lineDown[rowI])
        }
        this.printField()
    }

     DragLineDownTo(rowI)
     {
           
        //for( let r = rowI+1;)
        for (let r = rowI; r > 1; r--)
        //for (let r in reversed(range(1,rowI+1)))
        {
            let y = this.sy + (r*this.blocksize)
            for(let  x = 0; x< this.F[r].length; x++)
            {
                this.F[r][x].sprite = this.F[r-1][x].sprite
                if( this.F[r][x].sprite != null)
                {
                    this.F[r][x].sprite.R.y = y
                }
            }
        }
        this.ClearLine(0)
    }
     GetLineDown(block)
     {
        
        let linesDown =[]
        let  yI = []
        for (let s in block.sprites)
        {
            s=  block.sprites[s];

            let   relY = s.R.y-this.sy
            try{
                yI.index(relY)
            }
            catch 
            //except ValueError
            {
                yI.push(relY)
              //  print("checkline ", yI)
            }
        }
        for (let rowI in yI)//{#reversed( yI){
        {
            rowI= yI[rowI];
            let  count=0
            let   row = this.F[Math.floor(rowI/16)]
            for( let fb in row)
            {
                fb= row[fb];

                if (fb.sprite != null)
                {
                    count+=1
                }
            }
            if( count == row.length)
            {
                console.log("linecomplete")
                let index=this.F.indexOf(row);
                linesDown.push(index);
                //linesDown.append( this.F.index(row))
            }
        }
        console.log(linesDown)
        return linesDown
    }
    Overlaps( block)
    {

        for (let s in block.sprites)
        {
            s = block.sprites[s];

            for (let row in this.F)
            {
                row = this.F[row]
                for( let fb in row)
                {
                    fb = row[fb]
                    if (fb.sprite != null && fb.R.x == s.R.x && fb.R.y == s.R.y)
                    {
                        return true
                    }
                }
            }
        }
        return false
    }
   
     MovedOutsideVerti(block){
        for( let s in block.sprites)
        {
            s = block.sprites[s]
            if (s.R.bottom() > this.F[this.F.length-1][0].R.bottom())
            {
                return true
            }
        }
        return false
     }
     MovedOutsideHori(block)
     {
        for (let s in block.sprites)
        { 
            s =block.sprites[s]
            if( s.R.left() <this.F[0][0].R.x)
            {
               return true
            }
            if( s.R.x >= this.F[0][this.F[0].length-1].R.right())
            {
               return true
            }
        }
        return false
     }
     Rotate(left)
     {

      //  pass
     }
     PutBlock( s)
     {
        
        for( let  row in this.F)
        {
            row = this.F[row]
            for (let fb in row)
            {
                fb = row[fb]
                if (fb.R.x == s.R.x && fb.R.y == s.R.y)
                {
                    fb.sprite = s
                    return
                }
            }
        }
    }
}