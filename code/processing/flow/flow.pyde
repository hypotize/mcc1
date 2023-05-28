w = 400
h = 400
t = 150
def setup():
    size(w, h)
    background(0)

def draw():
    background(0)
    for j in range(40):
        seed = (j - frameCount) * 0.02
        pre_y = noise(seed) * t - t / 2 + h / 4 * sin(0) + h / 2
        c = color(noise(seed) * 255, noise(seed + 1) * 255, noise(seed + 2) * 255)
        stroke(c)
        for i in range(0, w, 3):
            y = noise(seed + 0.01 * (i + 1)) * t - t / 2 + h / 4 * sin(TWO_PI / 360 * i * 0.8) + h / 2
            line(i, pre_y, i + 3, y)
            pre_y = y
