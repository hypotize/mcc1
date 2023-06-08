w = 800
h = 800
t = 150

x = 0
y = 0 

def setup():
    size(w, h)
    background(0)

def draw():
    global x, y
    background(0) 
    c = color(255,0,0)
    fill(c)
    noStroke() 
    rect(x, y, 100, 100)
    x += 1
    y += 1
    if x > w: 
        x = 0
        y = 0
    
