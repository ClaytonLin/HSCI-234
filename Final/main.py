import js
p5 = js.window
ml5 = js.window

handpose = None
detections = []

canvas = None
video = None

def setup():
    global canvas, video, handpose
    canvas = p5.create_canvas(640, 480)
    canvas.id("canvas")

    video = p5.create_capture(p5.VIDEO)
    video.id("video")
    video.size(p5.width, p5.height)

    options = {
        "flipHorizontal": False,
        "maxContinuousChecks": float("inf"),
        "detectionConfidence": 0.8,
        "scoreThreshold": 0.75,
        "iouThreshold": 0.3,
    }

    handpose = ml5.handpose(video, options, model_ready)
    p5.color_mode(p5.HSB)

def model_ready():
    print("Model ready!")
    handpose.on('predict', process_results)

def process_results(results):
    global detections
    detections = results

def draw():
    p5.clear()
    p5.translate(-p5.width / 2, -p5.height / 2)

    if detections:
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

def draw_landmarks(index_array, hue):
    p5.no_fill()
    p5.stroke_weight(10)
    for detection in detections:
        for j in range(index_array[0], index_array[1]):
            x, y, z = detection.landmarks[j]
            p5.stroke(hue, 40, 255)
            p5.point(x, y)

def draw_lines(index):
    p5.stroke(0, 0, 255)
    p5.stroke_weight(3)
    for detection in detections:
        for j in range(len(index) - 1):
            x1, y1, z1 = detection.landmarks[index[j]]
            x2, y2, z2 = detection.landmarks[index[j + 1]]
            p5.line(x1, y1, z1, x2, y2, z2)
