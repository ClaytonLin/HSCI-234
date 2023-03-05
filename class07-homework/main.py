import js
p5 = js.window

program_timer = p5.millis()
program_state = 'state1'


def setup():
    p5.createCanvas(300, 300)  
    print('finished setup..')

def draw():
    global program_timer, program_state
    p5.background(253,242,112)   
    p5.fill(0)
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    
    # change the program state
    if (p5.millis() > program_timer + 2000):
        program_state = 'state2'
        program_timer = p5.millis()
        
    # draw compositions
    draw_hole(140,220)
    draw_hole(70,120)
    draw_hole(180,20)
    draw_hole(20,260)
    draw_hole(110,60)
    draw_hole(270,230)
    draw_hole(90,10)
    draw_hole(250,50)
    draw_hole(150,270)
    draw_hole(50,150)
    draw_shape1(80,120)
    draw_shape2(80,120)
    draw_shape3(80,120)
    draw_shape1(220,120)
    draw_shape2(220,120)
    draw_shape3(220,120)

# key interaction
def keyPressed(event):
    global program_state, program_timer
    print('keyPressed.. ' + str(p5.key))
    if (p5.key == '1'):  
        program_state = 'state1'
    elif (p5.key == '2'):  
        program_state = 'state2'
    elif (p5.key == '3'):  
        program_state = 'state3'
    program_timer = p5.millis()


def keyReleased(event):
    print('keyReleased.. ' + str(p5.key))

# mouse interaction
def mousePressed(event):
    global program_state, program_timer
    print('mousePressed..')
    if(program_state == 'state1'):
        program_state = 'state3'
    elif(program_state == 'state2'):
        program_state = 'state3'
        program_timer = p5.millis()

# stop mouse interaction
def mouseReleased(event):
    global program_state, program_timer
    print('mouseReleased..')
    if(program_state == 'state3'):
        program_state = 'state1'
        program_timer = p5.millis()

def draw_shape1(x,y):
    p5.fill(0)
    p5.strokeWeight(0)
    if(program_state == 'state2'):
        p5.fill(250)
    if(program_state == 'state3'):
        p5.fill(0)
    p5.ellipse(x, y, 100, 100)
    
def draw_shape2(x,y):
    p5.fill(250)
    p5.strokeWeight(0)
    if(program_state == 'state2'):
        p5.fill(0)
    if(program_state == 'state3'):
        p5.fill(0)
    p5.ellipse(x, y, 70, 70)

def draw_shape3(x,y):
    p5.fill(0)
    p5.strokeWeight(0)
    if(program_state == 'state2'):
        p5.fill(250)
    if(program_state == 'state3'):
        p5.fill(0)
    p5.ellipse(x, y, 20, 20)

def draw_hole(x,y):
    p5.fill(179,181,63)
    p5.strokeWeight(0)
    if(program_state == 'state2'):
        p5.fill(218,220,100)
    p5.ellipse(x, y, 40, 40)
