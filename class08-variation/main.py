# press 'a' to increase the speed of Earth to Level 1
# press arrow to move Earth


import js
p5 = js.window


# Create class Player
class Player:  
    # initialize x and y
    def __init__(self, x = 0, y = 0, speed = 0, color = 0, color2 = 0, state = "forward"):  
        self.x = x  
        self.y = y  
        self.speed = speed  
        self.color = color
        self.color2 = color2
        self.state = state

    def update(self,state):
        self.state=state
        
    def set_point(self, x, y):  
        self.x = x  
        self.y = y

    # Draw player
    def draw(self):  
        p5.push()
        if(self.state == 'Down'):
            p5.rotate(3.1415/2)
        
        if(self.state == 'Back'):  
            p5.rotate(3.1415/2*3) 
        
        if(self.state == 'Up'):
            p5.rotate(3.1415)
            
        p5.fill(self.color) 
        p5.ellipse(self.x, self.y, 50, 50) 
        p5.fill(self.color2)
        p5.ellipse(self.x - 10, self.y - 12, 15, 10)
        p5.ellipse(self.x + 10, self.y + 5, 20, 30)
        p5.ellipse(self.x + 2, self.y + 5, 20, 20)
        p5.ellipse(self.x + 5, self.y + 10, 20, 20)
        p5.ellipse(self.x - 15, self.y + 10, 10, 12)
        p5.pop

    
    def move_point(self, distance_x, distance_y):  
        self.x += distance_x  
        self.y += distance_y


player1 = Player(50, 50)
player2 = Player(250, 150)


def setup():  
    p5.createCanvas(300, 300)  
    print('finished setup..')


def draw():  
    global distance  
    p5.background(50) 
    p5.fill(200)
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)  
    p5.strokeWeight(0)


    # assign player1 a different color  
    player1.color = 200  
    player1.speed = 1  
    player2.color = p5.color(46, 79, 157)
    player1.color2 = 200
    player2.color2 = p5.color(147, 189, 82)
    
    # Move Moon automatically
    if player1.x < 250 and player1.y == 50:  
        player1.x += player1.speed  
    elif player1.x == 250 and player1.y < 250:  
        player1.y += player1.speed  
    elif player1.x <= 250 and player1.x > 50 and player1.y == 250:  
        player1.x -= player1.speed  
    elif player1.x == 50 and player1.y <= 250:  
        player1.y -= player1.speed

    # Change the level of speed of the Earth
    if (p5.keyIsPressed == True):  
        if (p5.key == 'a'):  
            player2.speed = 1  
        elif (p5.key == 's'):  
            player2.speed = 2  
        elif (p5.key == 'd'):  
            player2.speed = 3

    # Change the level of speed of the Earth
    if (p5.keyIsPressed == True):  
        if (p5.keyCode == p5.LEFT_ARROW):  
            player2.x = player2.x - player2.speed  
            player2.update("Back")
        elif (p5.keyCode == p5.RIGHT_ARROW):  
            player2.x = player2.x + player2.speed
            player2.update("Forward")
        elif (p5.keyCode == p5.UP_ARROW):  
            player2.y = player2.y - player2.speed
            player2.update("Up")
        elif (p5.keyCode == p5.DOWN_ARROW):  
            player2.y = player2.y + player2.speed
            player2.update("Down")
    
    # colliding response  
    distance = p5.dist(player1.x, player1.y, player2.x, player2.y)  
    if distance < 80:   
        player2.color = p5.color(220, 10, 0)
        player2.color2 = p5.color(220, 220, 50)
    
    # reset after colliding
    if distance < 50:  
        player1.x = 50  
        player1.y = 50  
        player2.x = 250  
        player2.y = 150
    
    player1.draw()  
    player2.draw()


def keyPressed(event):  
    print('keyPressed.. ' + str(p5.key))


def keyReleased(event):  
    print('keyReleased.. ' + str(p5.key))


def mousePressed(event):  
    print('mousePressed..')


def mouseReleased(event):  
    print('mouseReleased..')
