w = 400
h = 400
point1 = [None, None]
point2 = [None, None]
r = 200
def setup():
    global d, seed1, seed2
    size(w, h)
    background(255)
    d = TWO_PI / 360
    seed1 = random(0, 1)
    seed2 = random(0, 1)
    
def draw():
    pushMatrix()
    translate(w / 2, h / 2)
    n1 = noise(seed1 + 0.02 * frameCount) * r
    n2 = noise(seed2 + 0.02 * frameCount) * r
    point1[0] = cos(d * frameCount) * n1
    point1[1] = sin(d * frameCount) * n1
    point2[0] = cos(d * frameCount + HALF_PI) * n2
    point2[1] = sin(d * frameCount + HALF_PI) * n2
    stroke(frameCount / 5)
    if frameCount > 1250:
        noLoop()
    line(point1[0], point1[1], point2[0], point2[1])
    popMatrix()
