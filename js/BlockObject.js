class Rect
{
    constructor(x,y,w,h)
    {
        this.x=x;
        this.y=y;
        this.w=w;
        this.h=h;
    }

    bottom()
    {
        return this.y+this.h;
    }
    right()
    {
        return this.x+this.w;
    }
    left()
    {
        return this.x;
    }
}
class BlockObject
{

   constructor(blocks,x,y,gfx){
    this.sprites=[]
    this.blocks = blocks;
    this.isDropping=false
    this.rot =0
    this.gfx= gfx
    this.R = new Rect(x,y, 16*this.blocks[0].length, 
        16*this.blocks[0][0].length)
    this.MakeSprites()
   }


   MoveDown(){
      this.R.y+= 16
      for(let s in this.sprites)
      {
            s = this.sprites[s]
            s.R.y+= 16

      }
    }
   MoveUp(){
      this.R.y-= 16
      for(let s in this.sprites)
      {
        s = this.sprites[s];
          s.R.y-= 16
        }

    }

   MoveHori(dx)
   {
      this.R.x+= dx*16

        for (let s in this.sprites)
        {
            s = this.sprites[s]
            s.R.x+= dx*16
        }
    }

   TopLeft()
   {
        let  minx = 90000
        let miny=900000

        for (let s in this.sprites)
        {
            s = this.sprites[s];
            if(s.R.x < minx){
                minx = s.R.x
            }
            if (s.R.y < miny){
                miny = s.R.y
            }
        }
        return (minx,miny)

}
   MakeSprites()
   {
    this.sprites=[]


    for (let y = 0; y < this.blocks[this.rot].length; y++) 
    //for (y in range(0,len(this.blocks[this.rot])))
    {
        let   yrow = this.blocks[this.rot][y]
        for (let x = 0; x < yrow.length; x++) 
        {
            
        //for (x in range(0,len(yrow))){
            if (yrow[x] == 1)
            {
                let s =new  Sprite()
                s.frames=[ new Rect(this.gfx, 75, 16, 16)]
                s.R.x =x*16
                s.R.y = y*16
                s.R.x+=this.R.x
                s.R.y+=this.R.y
                this.sprites.push(s)
            }
 // #for pair in this.blocks[this.rot]{
 // #    s = Sprite()
 // #    s.frames=[Rect(this.gfx, 75, 16, 16)]
 // #    s.R.x = pair[0]*16
 // #    s.R.y = pair[1]*16
 // #    s.R.x+=x
 // #    s.R.y+=y
 // #    this.sprites.append(s)
        }
    }
}

   Rotate(left)
   {
        let currentBlock= this.blocks[this.rot]
        let topleft = this.TopLeft()


        let start = (this.sprites[0].R.x,this.sprites[0].R.y)

        if (left){
            this.rot -= 1
        }
        else{
            this.rot+= 1
        }
        if (this.rot >= this.blocks.length){
            this.rot =0
        }
        else if (this.rot < 0){
            this.rot= this.blocks.length-1
        }
        this.MakeSprites()
    }
}






