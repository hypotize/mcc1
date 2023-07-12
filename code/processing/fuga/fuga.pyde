w = 800
h = 800
t = 150
tt = 0
x = 0
y = 300
d = 5
dd = 5

def setup():
    size(w, h)
    background(0)

def draw():
    global x, y, tt, d, dd
    background(0) 
    c = color(tt,255,0)
    fill(c)
    noStroke() 
    ellipse(x, y, 100, 100)
    x += dd
    y += d

    if y+100 > h: 
        tt += 51
        d = random(-4,-50)
    if x+100 > w:
        tt += 51
        dd = random(-4,-50)
    if y < 0:
        tt += 51
        d = random(4,50)
    if x < 0:
        tt += 51
        dd = random(4,50)
    if tt > 255:
        tt = 0
