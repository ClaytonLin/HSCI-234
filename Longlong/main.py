import js
p5 = js.window
program_state = 'START'
short_speed = 8
long_speed = 1
point_x = 0

def Winpoint():
  global point_x
  print('point', point_x)
  p5.text(point_x, 430, 20)
  
class Start():  
  def __init__(self):
    self.img = p5.loadImage('start.png')
    self.x = 215
    self.y = 160
  
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width/3.5, -self.img.height/3.5)
    p5.pop()

class Guide():  
  def __init__(self):
    self.img = p5.loadImage('guide.png')
    self.x = 225
    self.y = 190

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width/4.5, -self.img.height/4.5)
    p5.pop()

class Pinocchio():  
  def __init__(self):
    self.img = p5.loadImage('pinocchio.png')
    self.x = 120
    self.y = 250
    
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width/4.5, -self.img.height/4.5)
    p5.pop()

class Point():  
  def __init__(self):
    self.img = p5.loadImage('points.png')
    self.x = 250
    self.y = 17
    
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width/4, -self.img.height/4)
    p5.pop()
    

class Bubble():  
  def __init__(self):
    self.img = p5.loadImage('bubble.png')
    self.x = 215
    self.y = 130
    
  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width/4, -self.img.height/4)
    p5.pop()

class Short():
  def __init__(self):
    self.img = p5.loadImage('short.png')
    self.x = 130
    self.y = 275

  def draw(self):  
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, self.img.width/4, self.img.height/4)
    p5.pop()
    
class Long():
  def __init__(self):
    self.img = p5.loadImage('long.png')
    self.x = 130
    self.y = 275

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, 0, 0, self.img.width/4, self.img.height/4)
    p5.pop()

class Statement1():
  def __init__(self):
    self.x = 220
    self.y = 190

  def draw(self):
    p5.fill(0)
    p5.textSize(16)
    p5.text('Chocolate is made from wood,', self.x, self.y)
    p5.text('since they are all in brown.', self.x, self.y + 15)

class Statement2():
  def __init__(self):
    self.x = 240
    self.y = 190

  def draw(self):
    p5.fill(0)
    p5.textSize(16)
    p5.text('Cloud is made from marshmellow', self.x, self.y)
    
class Statement3():
  def __init__(self):
    self.x = 240
    self.y = 190

  def draw(self):
    p5.fill(0)
    p5.textSize(16)
    p5.text('Dogs cannot fly', self.x, self.y)

class HE():  
  def __init__(self):
    self.img = p5.loadImage('win.png')
    self.x = 215
    self.y = 160

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width/3.5, -self.img.height/3.5)
    p5.pop()

class BE():  
  def __init__(self):
    self.img = p5.loadImage('lose.png')
    self.x = 215
    self.y = 160

  def draw(self):
    p5.push()
    p5.translate(self.x, self.y)
    p5.image(self.img, self.x, self.y, -self.img.width/3.5, -self.img.height/3.5)
    p5.pop()
    
start = Start()
guide = Guide()
pinocchio = Pinocchio()
point = Point()
bubble = Bubble()
short = Short()
long = Long()
statement1 = Statement1()
statement2 = Statement2()
statement3 = Statement3()
he = HE()
be = BE()
      
def setup():
  global font1
  p5.createCanvas(500, 500) 
  p5.rectMode(p5.CENTER)
  # p5.imageMode(p5.CENTER)
  p5.textSize(24)
  
def draw():
  global program_state, font1, start, guide, pinocchio, point, bubble, short, short_speed, long_speed, statement1, statement2, statement3, point_x
  p5.background('#64C3EF') 
  print('program_state =' + program_state)
  p5.textFont(font1)
  
  if(program_state == 'START'):
    start.draw()
    p5.fill(255)
    p5.textSize(24)
    p5.text('Click Anywhere To Start', 130, 360)
  elif(program_state =='GUIDE'):
    guide.draw()
  elif(program_state == 'PLAY'):
    global short_speed, long_speed
    pinocchio.draw()
    point.draw()
    bubble.draw()
    statement1.draw()
    Winpoint()
    
    # longnose
    if(program_state == 'PLAY'):
      long.x += long_speed 
      print(long.x)
      print(long_speed) 
      if(long.x > p5.width - 250) \
      or(long.x < 20):
        long_speed *= -1  # change direction
    long.draw()
    
    # shortnose  
    if(program_state == 'PLAY'):
      short.x += short_speed 
      if(short.x > p5.width - 5) \
      or(short.x < 5):
        short_speed *= -1  # change direction
    short.draw()

    # change to play 2
    if(p5.keyIsPressed == True):
      if(p5.key == ' '):
        if(program_state == 'PLAY'):
          long_speed = 0
          short_speed = 0
          if(long.x > 66 and long.x < 192):
            program_state = 'PLAY2'
            point_x += 1
            
    
  elif(program_state == 'PLAY2'):
    pinocchio.draw()
    point.draw()
    bubble.draw()
    statement2.draw()
    Winpoint()
    long_speed = 4
    short_speed = 8

#   # longnose
#     if(program_state == 'PLAY2'):
#       long.x += long_speed 
#       print(long.x)
#       print(long_speed) 
#       if(long.x > p5.width - 250) \
#       or(long.x < 20):
#         long_speed *= -1  # change direction
#       long.draw()
    
# # shortnose
#     if(program_state == 'PLAY2'):
#       short.x += short_speed 
#     if (short.x > p5.width - 5) \
#     or (short.x < 5):
#       short_speed *= -1  # change direction
#     short.draw()
    
# longnose
  # change direction
    #short.draw()
    
    # #change to play 3
    # if(p5.keyIsPressed == True):
    #   if(p5.key == ' '):
    #     if(program_state == 'PLAY2'):
    #       long_speed = 0
    #       short_speed = 0
    #       if(long.x > 66 and long.x < 192):
    #         point_x += 1
    #         program_state = 'PLAY3'
    
  # elif(program_state == 'PLAY3'):
    # pinocchio.draw()
    # point.draw()
    # bubble.draw()
    # statement3.draw()
    
    
# longnose
#     if(program_state == 'PLAY3'):
#         long.x += long_speed 
#     if (long.x > p5.width - 250) \
#     or (long.x < 20):
#         long_speed *= -1  # change direction
#     long.draw()
    
# # shortnose
#     if(program_state == 'PLAY3'):
#         short.x += short_speed 
#     if (short.x > p5.width - 5) \
#     or (short.x < 5):
#         short_speed *= -1  # change direction
#     short.draw()
    
#     # change to eval
#     if(p5.keyIsPressed == True):
#       if(p5.key == ' '):
#         if(program_state == 'PLAY3'):
#           long_speed = 0
#           short_speed = 0
#           if(long.x > 150 and long.x < 250):
#             point_x += 1
#             program_state = 'EVAL'
            
  elif(program_state == 'EVAL'):
    pinocchio.draw()
    point.draw()
    bubble.draw()
    statement3.draw()
    if(program_state == 'EVAL'):
      if(point_x == 3):
        ge.draw()
        p5.fill(255)
        p5.textSize(48)
        p5.text('Click Anywhere To Restart', 190, 360)
      elif(point_x <= 2):
        be.draw()
        p5.fill(255)
        p5.textSize(48)
        p5.text('Click Anywhere To Restart', 190, 360) 
      
    # start.draw()
    # p5.fill(255)
    # p5.textSize(48)
    # p5.text('Click Anywhere To Restart', 190, 360)
    
  # show cursor coordinates:
  p5.text((int(p5.mouseX), int(p5.mouseY)), 10, 20)
  p5.strokeWeight(1)  # 1-pixel stroke
  
# # change to play 2
#   if(p5.keyIsPressed == True):
#     if(p5.key == ' '):
#       if(program_state == 'PLAY'):
#         long_speed = 0
#         short_speed = 0
#         # program_state = 'PLAY2'
#         if(long.x > 0 and long.x < 500):
#           program_state = 'PLAY2'
#           point_x += 1
# # change to play 3
#   if(p5.keyIsPressed == True):
#     if(p5.key == ' '):
#       if(program_state == 'PLAY2'):
#         long_speed = 0
#         short_speed = 0
#         program_state = 'PLAY3'
#         if(long.x > 0 and long.x < 500):
#           program_state = 'PLAY3'
#           point_x += 1
# # change to eval
#   if(p5.keyIsPressed == True):
#     if(p5.key == ' '):
#       if(program_state == 'PLAY3'):
#         long_speed =       0
#         short_speed = 0
#         program_state = 'EVAL'
#         if(long.x > 0 and long.x < 500):
#           program_state = 'EVAL'
#           point_x += 1
#           # if(point_x == 3):
            
  # if(point_x == 3) or (point_x <= 3)

        
  
def keyPressed(event):
  print('key pressed.. ' + p5.key)
  

def keyReleased(event):
  pass
  
def mousePressed(event):
  global program_state, long_speed, short_speed
  if(program_state == 'START'):
    program_state = 'GUIDE'
    print('program_state = ' + program_state)
  elif(program_state == 'GUIDE'):
    program_state = 'PLAY' 
    print('program_state = ' + program_state)

    
def mouseReleased(event):
  print('program_state = ' + program_state)
