import js
p5 = js.window
angle = 0.0
angle_2 = 30.0
robot_x = 0
robot_y = 0
head_x = 0
head_y = 0
explode_x = 0
explode_y = 0

def setup():
    p5.createCanvas(300, 300)   
    p5.rectMode(p5.CENTER)  # set rectangle drawing mode to CENTER

# draw
def draw():
    global robot_x
    global robot_y
    global head_x
    global head_y
    global explode_x
    global explode_y
    p5.background(220)
    if (p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            p5.background(100)
    p5.fill(120)
    p5.text('p5.mouseIsPressed: ' + str(p5.mouseIsPressed), 10, 20)
    p5.text('p5.mouseButton: ' + str(p5.mouseButton), 10, 35)
    p5.text('p5.keyIsPressed: ' + str(p5.keyIsPressed), 10, 50)
    p5.text('p5.key: ' + str(p5.key), 10, 65)
    p5.push()
    p5.translate(150, 150)
    draw_body()
    draw_head()
    draw_eye()
    draw_eye_2()
    draw_eye_3()
    body_pattern_2(robot_x + 10,robot_y + 45,30,30)
    body_pattern_2(robot_x + -5,robot_y + 100,30,30)
    body_pattern_2(robot_x + 5,robot_y + 70,40,40)
    body_pattern_2(robot_x + 40,robot_y + 65,50,50)
    body_pattern(robot_x + -20,robot_y + 30,60,60)
    p5.pop()

    # control the robot
    if (p5.keyIsPressed == True):
        if (p5.keyCode == p5.LEFT_ARROW):
            robot_x = robot_x - 1
        elif (p5.keyCode == p5.RIGHT_ARROW): 
            robot_x = robot_x + 1
        elif (p5.keyCode == p5.UP_ARROW):
            robot_y = robot_y - 1
        elif (p5.keyCode == p5.DOWN_ARROW):  
            robot_y = robot_y + 1
            
    # control the head of the robot
        elif (p5.key == 'a'):  
            head_x = head_x - 1
        elif (p5.key == 'd'):  
            head_x = head_x + 1
        elif (p5.key == 'w'):  
            head_y = head_y - 1
        elif (p5.key == 's'):  
            head_y = head_y + 1
        elif (p5.key == 'r'):  
            robot_x = 0
            robot_y = 0
            head_x = 0
            head_y = 0
            explode_x = 0
            explode_y = 0
    # stop when key is not pressed
        if (p5.keyIsPressed == False):
            p5.pop()

# draw notice
def draw_notice():
    p5.fill(255,255,0)
    p5.strokeWeight(0)
    p5.rect(60,-120,10,50)
    p5.rect(60,-60,10,10)

# draw head
def draw_head():
    global explode_x
    global explode_y
    p5.strokeWeight(0)
    if(p5.mouseX >= 100 and p5.mouseX <= 200 and p5.mouseY >= 100 and p5.mouseY <= 200):
        draw_notice()
        p5.fill(180,10,10)
        explode_x = explode_x + 1
        explode_y = explode_y + 1
    else:
        p5.fill(255)
    if (p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            p5.fill(50)
    p5.ellipse(robot_x + head_x, robot_y - 50 + head_y, explode_x + 100, explode_y + 100)
    p5.strokeWeight(0)

# draw body
def draw_body():
    p5.fill(255)
    p5.strokeWeight(0)
    if (p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            p5.fill(50)
        elif (p5.mouseButton == p5.RIGHT):
            p5.fill(150)
    p5.ellipse(robot_x, robot_y + 50, 150, 150)

# draw eye
def draw_eye():
    p5.fill(90)
    if (p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            p5.fill(130)
        elif (p5.mouseButton == p5.RIGHT):
            p5.fill(130)
    p5.ellipse(robot_x + head_x, robot_y - 60 + head_y, 30, 30)

# draw eye2
def draw_eye_2():
    p5.fill(50)
    if (p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            p5.fill(170)
        elif (p5.mouseButton == p5.RIGHT):
            p5.fill(170)
    p5.ellipse(robot_x + head_x, robot_y - 60 + head_y, 20, 20)

# draw eye3
def draw_eye_3():
    p5.fill(255,87,51)
    p5.ellipse(robot_x + head_x, robot_y - 60 + head_y, 10, 10)

# draw body pattern
def body_pattern(x, y,radius1,radius2):
    p5.fill(230)
    p5.strokeWeight(0)
    if (p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            p5.fill(130)
        elif (p5.mouseButton == p5.RIGHT):
            p5.fill(130)
    p5.ellipse(x, y, radius1, radius2)
    p5.fill(210)
    if (p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            p5.fill(150)
        elif (p5.mouseButton == p5.RIGHT):
            p5.fill(150)
    p5.ellipse(x, y, radius1/1.5, radius2/1.5)
    rotate_rec_1()
    rotate_rec_2()
    rotate_rec_3()

# draw body pattern2
def body_pattern_2(x,y,radius1,radius2):
    p5.fill(230)
    p5.strokeWeight(0)
    if (p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            p5.fill(130)
        elif (p5.mouseButton == p5.RIGHT):
            p5.fill(130)
    p5.ellipse(x, y, radius1, radius2)
    p5.fill(210)
    if (p5.mouseIsPressed == True):
        if (p5.mouseButton == p5.LEFT):
            p5.fill(150)
        elif (p5.mouseButton == p5.RIGHT):
            p5.fill(150)
    p5.ellipse(x, y, radius1/1.5, radius2/1.5)

# draw rotate_rec1
def rotate_rec_1():
    global angle 
    p5.push()
    p5.translate(robot_x - 20, robot_y + 30)
    p5.rotate(angle)  # rotate by angle
    p5.rect(0, 9, 10, 20)
    angle = angle + 0.05  # increment angle
    p5.pop()

# draw rotate_rec2
def rotate_rec_2():
    global angle_2 
    p5.push()
    p5.translate(robot_x - 20, robot_y + 30)
    p5.rotate(angle_2)  # rotate by angle
    p5.rect(0, 9, 10, 20)
    angle_2 = angle + 90  # increment angle
    p5.pop()

# draw rotate_rec3
def rotate_rec_3():
    global angle_2 
    p5.push()
    p5.translate(robot_x - 20, robot_y + 30)
    p5.rotate(angle_2)  # rotate by angle
    p5.rect(0, 9, 10, 20)
    angle_2 = angle + 180  # increment angle
    p5.pop()
