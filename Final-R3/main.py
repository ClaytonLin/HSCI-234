#move your hand to grab the cube to the target
#press tab to pause the game

import js
from pyodide.ffi import create_proxy
p5 = js.window
ml5 = js.ml5

handpose = None
detections = []

random_x_1 = p5.random(500)
random_y_1 = p5.random(300)
random_x_2 = p5.random(500)
random_y_2 = p5.random(300)

canvas = None
video = None

class Cube:

    def __init__(self, x = 0, y = 0):  
        self.x = x  
        self.y = y  
        self.img = p5.loadImage('Cube.png')
        

    def set_point(self, x, y):  
        self.x = x  
        self.y = y

    def draw(self): 
        p5.push()
        p5.translate(self.x, self.y)
        p5.strokeWeight(0)
        p5.image(self.img, 0, 0)
        p5.pop()


class Target:

    def __init__(self, x = 0, y = 0):  
        self.x = x  
        self.y = y  
        self.img = p5.loadImage('Target.png')

    def set_point(self, x, y):  
        self.x = x  
        self.y = y

    def draw(self): 
        p5.push()
        p5.translate(self.x, self.y);
        p5.strokeWeight(0)
        p5.image(self.img, 0, 0)
        p5.pop()

class Button:
        
    def __init__(self, x = 0, y = 0):  
        self.x = x  
        self.y = y  
        self.img = p5.loadImage('Button.png') 

    def draw(self): 
        p5.push()
        p5.translate(self.x, self.y)
        p5.strokeWeight(0)
        p5.fill(0,0,24)
        p5.rect(self.x - 30, self.y - 30, 140, 50, 100)
        p5.fill(255)
        p5.textFont('Helvetica', 72)
        p5.textStyle(p5.BOLD)
        p5.textSize(16)
        p5.text("Play Again", self.x, self.y)
        p5.pop()


cube1 = Cube(50,50)
target1 = Target(400,250)
button1 = Button(30,90)
program_state = "play"

def setup():
    global canvas, video, handpose
    p5.createCanvas(640, 480) 
    
    video = p5.createCapture(p5.VIDEO)
    video.id("video")
    video.size(p5.width, p5.height)
    video.style('transform', 'scaleX(-1)') 

    options = {
        "flipHorizontal": True,
        "maxContinuousChecks": float("inf"),
        "detectionConfidence": 0.8,
        "scoreThreshold": 0.75,
        "iouThreshold": 0.3,
    }
    print('ml5 version:', ml5.version)
    #handpose = ml5.handpose(video, options, model_ready)
    model_ready_proxy = create_proxy(model_ready)
    
    handpose = ml5.handpose(video, model_ready_proxy)
    p5.colorMode(p5.HSB)

    print('finished setup') 
    

def model_ready():
    print("Model ready!")
    #handpose.on('predict', process_results)
    process_results_proxy = create_proxy(process_results)
    handpose.on('predict', process_results_proxy)

def process_results(results):
    global detections
    detections = results

def draw():
    p5.clear()
    p5.push()
    p5.fill(0, 0, 0, 100)
    p5.rect(-1, 0, p5.width + 1, p5.height + 1)

    if (program_state == "play"):
        check_win_condition()
        
    if program_state != "paused" and detections:
        draw_lines([0, 5, 9, 13, 17, 0])  # palm
        draw_lines([0, 1, 2, 3, 4])  # thumb
        draw_lines([5, 6, 7, 8])  # index finger
        draw_lines([9, 10, 11, 12])  # middle finger
        draw_lines([13, 14, 15, 16])  # ring finger
        draw_lines([17, 18, 19, 20])  # pinky
        
        draw_landmarks([0, 1], 0)  # palm base
        draw_landmarks([1, 5], 60)  # thumb
        draw_landmarks([5, 9], 120)  # index finger
        draw_landmarks([9, 13], 180)  # middle finger
        draw_landmarks([13, 17], 240)  # ring finger
        draw_landmarks([17, 21], 300)  # pinky

        # Check if the palm is closed and close to the cube
        for detection in detections:
            avg_x, avg_y = get_average_position(detection)
            if is_palm_closed(detection) and abs(avg_x - cube1.x) < 50 and abs(avg_y - cube1.y) < 50:
                cube1.set_point(avg_x, avg_y)
                
        for detection in detections:
            if is_palm_closed(detection):
                print("palmClosed")

    if (program_state == "win"):
        button1.draw()
        p5.textSize(32)
        p5.strokeWeight(0)
        p5.fill(255)
        p5.textFont('Helvetica', 72)
        p5.textStyle(p5.BOLD)
        p5.text("SUCCESS!", 30, p5.height / 2 - 125)
        if detections:
            avg_x, avg_y = get_average_position(detections[0])
            if avg_x < 150 and avg_y < 200:
                reset_game()

    p5.pop()
    target1.draw()
    cube1.draw()

    if program_state == "paused":
        p5.fill(0,0,0)
        p5.rect(0,0,p5.width + 1, p5.height + 1)
        p5.textSize(32)
        p5.strokeWeight(0)
        p5.fill(255)
        p5.textFont('Helvetica', 72)
        p5.textStyle(p5.BOLD)
        p5.text("PAUSED", p5.width / 2 - 140, p5.height / 2 )
    

def reset_game():
    global program_state, cube1
    program_state = "play"
    cube1.set_point(random_x_1, random_y_1)
    target1.set_point(random_x_2, random_y_2)

def draw_landmarks(index_array, hue):
    p5.noFill()
    p5.strokeWeight(10)
    for detection in detections:
        for j in range(index_array[0], index_array[1]):
            x, y, z = detection.landmarks[j]
            p5.stroke(hue, 50, 255)
            p5.point(x, y)

def draw_lines(index):
    p5.stroke(0, 0, 255)
    p5.strokeWeight(3)
    for detection in detections:
        for j in range(len(index) - 1):
            x1, y1, z1 = detection.landmarks[index[j]]
            x2, y2, z2 = detection.landmarks[index[j + 1]]
            p5.line(x1, y1, x2, y2) 

def is_palm_closed(detection):
    threshold = 100  # adjust this value to fine-tune the detection sensitivity
    thumb_tip = detection.landmarks[4]
    index_tip = detection.landmarks[8]
    middle_tip = detection.landmarks[12]
    ring_tip = detection.landmarks[16]
    pinky_tip = detection.landmarks[20]

    def distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    if (distance(thumb_tip, index_tip) < threshold and
        distance(thumb_tip, middle_tip) < threshold and
        distance(thumb_tip, ring_tip) < threshold and
        distance(thumb_tip, pinky_tip) < threshold):
        return True
    return False

def get_average_position(detection):
    palm_base = detection.landmarks[0]
    thumb_tip = detection.landmarks[4]
    index_tip = detection.landmarks[8]
    middle_tip = detection.landmarks[12]
    ring_tip = detection.landmarks[16]
    pinky_tip = detection.landmarks[20]

    avg_x = (palm_base[0] + thumb_tip[0] + index_tip[0] + middle_tip[0] + ring_tip[0] + pinky_tip[0]) / 6
    avg_y = (palm_base[1] + thumb_tip[1] + index_tip[1] + middle_tip[1] + ring_tip[1] + pinky_tip[1]) / 6

    return avg_x, avg_y

def check_win_condition():
    global program_state
    threshold = 50  # adjust this value to fine-tune the win condition sensitivity

    def distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    if cube1.x > target1.x + 50 and cube1.x < target1.x + 150 and cube1.y > target1.y and cube1.y < target1.y + 10:
        program_state = "win"


def keyPressed(event):
    global program_state
    if (p5.keyCode == p5.TAB):
        if program_state == "play":
            program_state = "paused"
        elif program_state == "paused":
            program_state = "play"

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass
