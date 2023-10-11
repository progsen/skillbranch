let canvas = document.getElementById("canvas");

let running  = true
//g = pygame.display.set_mode((400,600))



let gc = new GameContext()
let logic = new GameLogic(gc)
let  renderer = new Renderer(canvas,gc)
let  adown=false
for (let x =0 ; x <4; x++)
{
    for (let y =0 ; y < 2;y++)
    {
        gc.SetCurrentBlock(2)
        gc.currentBlock.MoveHori(x*2)
        for (let z = 0; z <23; z++)
        {
            logic.MoveBlockDown()
        }
    }
}
for (let x =0 ; x <3; x++)
{
        gc.SetCurrentBlock(1)
        gc.currentBlock.MoveHori(x*2)
        for (let z= 0; z <23; z++)
        {
            logic.MoveBlockDown()
        }
    }
gc.SetCurrentBlock(0)
gc.currentBlock.MoveHori(8)   
for (let z= 0; z <23; z++)
{
    logic.MoveBlockDown()
}
gc.SetCurrentBlock(0)
gc.currentBlock.MoveHori(8)   
//#gc.SetCurrentBlock(2)
//#gc.currentBlock.MoveHori(8)
 function handleKeyUp(event)
 {
    
    if (event.key == "a"){
        gc.leftDown=false
    }
    if (event.key == "d"){
        gc.rightDown=false
    }
    if (event.key == "w"){
        gc.upDown=false
    }
    if (event.key == "s"){
        gc.downDown=false
    }
    if (event.key == "k"){
        gc.rotL=false
    }
    if (event.key == "l"){
        gc.rotR=false
    }    
 }
 function handleKeyDown(event)
 {
    if (event.key == "a"){
        gc.leftDown=true
    
    }
        if (event.key == "d"){
        gc.rightDown=true
        }
    if (event.key == "w"){
        gc.upDown=true
    }
    if (event.key == "s"){
        gc.downDown=true
    }
    if (event.key == "k"){
        gc.rotL=true
    }
    if (event.key == "l"){
        gc.rotR=true
 }
}

 function gameFrame()
 {
  
    //newticks=pygame.time.get_ticks()
    gc.frameticks= 33;//newticks-gc.ticks
    //events = pygame.event.get()

  // for event in events{
  //     if (event.type == pygame.KEYDOWN{
  //        handleKeyDown(event);
  //     if (event.type == pygame.QUIT{  
  //        running = false
  // 
  // for event in events{
  //     if (event.type == pygame.KEYUP{
  //         handleKeyUp(event);
    logic.doLogic()
    renderer.renderFrame()
  //  time.sleep(0.033)
    gc.frametime=0.033
 }
    


 //canvas.addEventListener("click", canvasClicked);

 let sprites = ["sprites.png?v=7"];
 loadSprites(sprites,()=>{

    renderer.sprites = sprites;
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);
    setInterval(gameFrame,33);

 })
