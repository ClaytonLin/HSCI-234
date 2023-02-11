import js
p5 = js.window
random_x_1 = p5.random(150)
random_y_1 = p5.random(100)
random_x_2 = p5.random(150)
random_y_2 = p5.random(100)
random_x_3 = p5.random(150)
random_y_3 = p5.random(100)
random_x_4 = p5.random(150)
random_y_4 = p5.random(100)
random_x_5 = p5.random(150)
random_y_5 = p5.random(100)

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(210,210,210)         # white background
    p5.push()
    p5.translate(150, 150)  # move coordinates by (150, 150)
    draw_face()  # call function to draw the face
    draw_hair(0,-80)
    draw_hair(0,-100)
    draw_hair(-20,-70)
    draw_hair(-10,-90)
    draw_hair(-40,-60)
    draw_hair(0,-100)
    draw_hair(-50,-90)
    draw_hair(-60,-100)
    draw_hair(-60,-80)
    draw_hair(20,-80)
    draw_hair(30,-100)
    draw_hair(40,-70)
    draw_hair(50,-80)
    draw_eye(-38,0)
    draw_eye(22,0)
    draw_eye_black(-43+p5.mouseX/100,0+p5.mouseY/100)
    draw_eye_black(18+p5.mouseX/100,0+p5.mouseY/100)
    draw_nose(-10,25)
    draw_mouth(-10,55,40+p5.mouseX/20+p5.mouseY/20)
    draw_glasses(-43,0+p5.mouseY/10)
    p5.pop()
    p5.fill(240,240,240)
    p5.ellipse(random_x_1,random_y_1,30,30)    # draw random white ball
    p5.ellipse(random_x_2,random_y_2,30,30)
    p5.ellipse(random_x_3,random_y_3,30,30)
    p5.ellipse(random_x_4,random_y_4,30,30)
    p5.ellipse(random_x_5,random_y_5,30,30)

# draw face
def draw_face():
    p5.line(-80, -80, -75, 0)
    p5.line(-75, 0, -60, 50)
    p5.line(-60, 50, -20, 80)
    p5.line(-20, 80, 0, 80)
    p5.line(0, 80, 40, 50)
    p5.line(40, 50, 55, 0)
    p5.line(55, 0, 60, -80)

# draw hair
def draw_hair(x,y):
    p5.fill(0,0,0)
    p5.ellipse(x,y,75,60)

# draw eye
def draw_eye(x,y):
    p5.fill(255,255,255,0)
    p5.stroke(0)
    p5.arc(x-3, y, 30, 20, p5.radians(180), p5.radians(0))
    p5.arc(x-3, y, 30, 20, p5.radians(0), p5.radians(180))

# draw eye black
def draw_eye_black(x,y):
    p5.fill(0)
    p5.ellipse(x,y,15,13)

# draw nose
def draw_nose(x,y):
    p5.fill(0)
    p5.ellipse(x,y,5,10)

# draw mouth
def draw_mouth(x,y,radius):
    p5.fill(0)
    p5.ellipse(x,y,radius/4, radius/4)

# draw glasses
def draw_glasses(x,y):
    p5.fill(0,0,0,0)
    p5.strokeWeight(5)
    p5.ellipse(x,y,60,45)
    p5.ellipse(x+65,y,60,45)
