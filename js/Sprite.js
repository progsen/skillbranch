

class Sprite
{
   constructor()
   {
      this.R = new Rect(0,0,16,16)
      this.frames=[
      new Rect(43, 9, 16, 16),
       new Rect(60, 9, 16, 16),
      new Rect(77, 9, 16, 16)]
      this.frame = 0.0;
      this.animationSpeed = 10.0
      this.hidden=false
   }
   MoveFrame(frametime)
   {

      this.frame += frametime * this.animationSpeed;
      // #print(this.frame,frametime)
      if (this.frame >= this.frames.length)
      {
         this.frame = 0;
      }
   }
}
  

