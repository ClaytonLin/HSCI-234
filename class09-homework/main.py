import js
p5 = js.window

# class definition for the Bullet object:
class Cube:  
    def __init__(self, x = 50, y = 250):
        self.x = x  
        self.y = y  

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.fill(225, 225, 225)
        p5.quad(20,0,30,-10,30,8,20,20)
        p5.fill(195, 195, 195)
        p5.quad(12,-10,30,-10,20,0,0,0)
        p5.fill(255, 255, 255)
        p5.rect(0, 0, 20, 20)
        p5.pop()
    
    def update(self):
        self.y -= 2
cube = Cube()  

def setup():
    p5.createCanvas(300, 300)  
    p5.rectMode(p5.CENTER)
    p5.imageMode(p5.CENTER)
    print('use space bar to shoot the invaders..')

def draw():
    global cube
    p5.background(0)    
    cube.draw()
        
def keyPressed(event):
    pass

def keyReleased(event):
    global bullet
    if(p5.key == ' '):
        # reset the bullet to spaceship coordinates:
        bullet.x = spaceship.x
        bullet.y = spaceship.y

def mousePressed(event):
    pass

def mouseReleased(event):
    pass
