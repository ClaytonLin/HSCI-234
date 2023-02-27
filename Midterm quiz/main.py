import js
p5 = js.window

# question 1
random_size = p5.int(p5.random(25, 125))
random_size2 = p5.int(p5.random(25, 125))
random_size3 = p5.int(p5.random(25, 125))
random_size4 = p5.int(p5.random(25, 125))

alpha = 0

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
    print('finished setup')

def draw():
    global alpha
    global i
    p5.background(255)           # white background
    p5.strokeWeight(0)
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.text(random_size, 10, 30)
    p5.text(inside_square(),10,45)
    p5.strokeWeight(2)  # set stroke thickness

    # question 6
    # question 7
    if (p5.mouseIsPressed == True):
        p5.stroke(127, 0, 255)
        random_square_at(10, 10, random_size)

    p5.stroke(255, 127, 54, alpha)
    random_square_at(140, 140, random_size2)
    #question 8
    alpha = alpha + 1
    if (alpha == 255):
        alpha = 0

    #question 9
    p5.stroke(127, 200, 0) 
    inside_square()
    random_square_at(10, 140, random_size3)

    # question 12
    p5.stroke(255, 0, 127)
    for i in range(4):
        random_square_at(140, 10, random_size4 * i / 4)

def moveto(x1, y1):
    x1 = 10
    y1 = 10

def lineto(x2, y2):
    x2 = size
    y2 = size

# question 3
def random_square(size):
    # question 2
    p5.line(10,10,10 + size,10)
    p5.line(10 + size,10,10 + size,10 + size)
    p5.line(10 + size,10 + size,10,10 + size)
    p5.line(10,10 + size,10,10)

# question 5
def random_square_at(x, y, size):
    # question 4
    p5.push()
    p5.translate(x, y)
    random_square(size)
    p5.pop()
    
# question 10
def inside_square():
    # question 9
    if(p5.mouseX >= 10 + 10 and p5.mouseX <= 10 + 10 + random_size3 and p5.mouseY >= 140 and p5.mouseY <= 140 + random_size3):
        p5.stroke(240, 203, 22)
        return True
    else:
        return False
