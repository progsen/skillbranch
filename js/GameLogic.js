
                             


class GameLogic{
     constructor( gc){
        this.gc=gc;
     }
       
     stopInput(){
        this.gc.inputdown=3;
     }
     InverseBlockMovement(block,dx,dy){
        if (dy == 1){
            block.MoveUp()
        }
        if (dx == -1){
            block.MoveHori(1)}
        if (dx == 1){
            block.MoveHori(-1)
        }
     }
     CheckBlockCollisions(block,dx,dy)
     {
        
        if (this.gc.field.Overlaps(block))
        {
            this.InverseBlockMovement(block,dx,dy)
            if(dx == 0)
            {//downward movement found overlap = stuck
                console.log("locking");
                this.LockCurrentBlock()

            }
		}
        else if    ( this.gc.field.MovedOutsideHori(block))
            {
                console.log("MovedOutsideHori");
            this.InverseBlockMovement(block,dx,dy)
            
        }
        else if( this.gc.field.MovedOutsideVerti(block))
        {
            this.InverseBlockMovement(block,dx,dy)
            this.LockCurrentBlock()
            
        }

    }
     MoveBlockDown(){
       let  block = this.gc.currentBlock;

        block.MoveDown()
        this.CheckBlockCollisions(block,0,1)
     }

     LockCurrentBlock()
     {
        for (let s in this.gc.currentBlock.sprites)
        {
            s = this.gc.currentBlock.sprites[s];
            this.gc.field.PutBlock(s)
        }
        this.gc. lineDown = this.gc.field.GetLineDown(this.gc.currentBlock)
        if(this.gc.lineDown.length>0)
        {
            this.gc.lineDownCycle=10
            console.log("this.gc. lineDown"+ this.gc. lineDown)
}
            this.gc.RandomNewBlock();
        
    }
     doLogic()
     {
        let  gc = this.gc
        gc.downcount-=1
        if(gc.lineDownCycle>0)
        {
            gc.lineDownCycle-=1
            if(gc.lineDownCycle == 0)
            {
              //  #gc.field.ClearLines(gc.lineDown)
                for(let line in gc.lineDown)
                { 
                    line = gc.lineDown[line]
                    gc.field.DragLineDownTo(line)
                }
                gc.lineDown=[]
            }
            return
        }
        if(gc.inputdown > 0)
        {
            gc.inputdown-=1
        }
        if( gc.downcount <= 0 && gc.currentBlock.isDropping == false)
        {
            this.MoveBlockDown()
            gc.downcount=30
        }
        if( gc.currentBlock.isDropping)
        {
            this.MoveBlockDown()
            gc.downcount=3
        }
        if (gc.rightDown && gc.inputdown == 0)
        {
            gc.currentBlock.MoveHori(1)
            this.CheckBlockCollisions(gc.currentBlock,1,0)
            this.stopInput()
        //    #gc.player.R.x+=1
        }
        if( gc.leftDown && gc.inputdown == 0)
        {
            gc.currentBlock.MoveHori(-1)
            this.CheckBlockCollisions(gc.currentBlock,-1,0)
            this.stopInput()
        //    #gc.player.R.x-=1
        }  
        if (gc.rotL && gc.inputdown == 0)
        {
            this.rotateCurrent(true)
        }
        if (gc.rotR && gc.inputdown == 0)
        {
            this.rotateCurrent(false)
        }
        //#if gc.upDown{
          //  #gc.player.R.y-=1
        if( gc.downDown)
        {
            gc.currentBlock.isDropping = true
        }
        else{
            gc.currentBlock.isDropping = false
        }
    }
     rotateCurrent(left)
     {
        this.gc.currentBlock.Rotate(left)
        let  block= this.gc.currentBlock

        if( this.gc.field.Overlaps(block))
        {
            this.gc.currentBlock.Rotate(left==False)
        //    #if(dx == 0){
          //  #    this.LockCurrentBlock()
        }
        else if( this.gc.field.MovedOutsideHori(block))
        {
            this.gc.currentBlock.Rotate(left==False)
        }
        else if( this.gc.field.MovedOutsideVerti(block))
        {
            this.gc.currentBlock.Rotate(left==False)
            this.LockCurrentBlock()
        }
        this.stopInput()
    }



}