turn = 0
press = 0
left = 0
middle = 0
right = 0

def setup():    # 最初に１回だけ実行
    size(600, 400)
    font = createFont("Noto Sans CJK JP", 25)
    textFont(font)

def draw():     # 繰り返し実行
    background(0)
    fill(255)
    textSize(25)
    text(u"スロットマシーン", 200, 50)
    text(u"マウスをクリックしてください", 140, 250)
    stroke(255)
    noFill()
    rect(100, 100, 100, 100)
    rect(250, 100, 100, 100)
    rect(400, 100, 100, 100)
    numberDisp()
    
def numberDisp():
    global turn, left, middle, right
    textSize(60)
    fill(255)
    if press == 0:
        left = turn
    if press <= 1:
        middle = turn
    if press <= 2:
        right = turn
    if press == 3:
        judge()
    text(str(left), 130, 170)
    text(str(middle), 280, 170)
    text(str(right), 430, 170)
    turn = (turn + 1) % 10
    
def mousePressed():
    global press
    press += 1
    if press == 4:
        press = 0
    
def judge():
    if left == middle and middle == right:
        text(u"大当たり！！！", 140, 350)
    elif left == middle or left == right or middle == right:
        text(u"当たり！！！", 140, 350)
    else:
        text(u"外れ！！！", 140, 350)
