
function loadSprites(sprites,done)
{
    let loaded = 0;
    for (let i = 0; i < sprites.length; i++)
    {
        let src = sprites[i];
        sprites[i] = new Image();
        sprites[i].onload = function ()
        {
            loaded++;
            if (loaded == sprites.length)
            {
                console.log("sprites loaded");
                done();
            }
        }
        sprites[i].src = src ;
    }
}

class Renderer
{

     constructor(canvas,gc)
     {
        this.canvas=canvas;
        this.gc=gc
        this.g =    canvas.getContext("2d");
       // this.image = pygame.image.load('sprites.png')
        this.empty = new Sprite()
        this.empty.frames=[new Rect(2, 75, 16, 16)]
     }
    
     renderField(){
        
       let  gc =this.gc
        for (let row in gc.field.F)
        {
            row= gc.field.F[row];
            let blink=false
            let index =  gc.field.F.indexOf(row);

            if(gc.lineDown.indexOf(index) != -1)// gc.field.F.index(row) in gc.lineDown)
            {
                blink = gc.lineDownCycle %2==0
            }
            for(let r in row)
            {
                r= row[r];
                this.empty.R = r.R
            //    #pygame.draw.rect(this.g, (255,0,0), r.R,1)
                this.RenderObject(this.empty)
                if( r.sprite != null && blink == false)
                {
                    this.RenderObject(r.sprite)
                }
            }
        }
    }

     renderFrame()
     {
        let  g= this.g
        g.fillStyle = "#000000"
        g.fillRect( 0,0, 400,600)

     //   #render mario sprite test
        //#this.RenderObject(this.gc.player)
        
        
      //  #render text test
      //  # text1 = this.font1.render('GeeksForGeeks', true, (0, 255, 0))
      //  #textRect1 = text1.get_rect()
      //  #g.blit(text1, textRect1)

        this.renderField()
        
        let  gc =this.gc 
        for (let s in gc.currentBlock.sprites)
        {
            s = gc.currentBlock.sprites[s]
            if (s.hidden == false)
            {
                this.RenderObject(s)
            }
        }

     //   pygame.display.flip()
    }
     RenderObject( renderObject)
     {
        let  g= this.g
       let  frame= Math.floor(renderObject.frame)
       let  area = renderObject.frames[frame]
       // this.g.drawImage(this.image,renderObject.R,area =area)

        let r=renderObject.R;
        
        g.drawImage(sprites[0], area.x, area.y, area.w, area.h, 
            r.x, r.y, r.w, r.h);
            
            


        renderObject.MoveFrame(this.gc.frametime);
     }
}




