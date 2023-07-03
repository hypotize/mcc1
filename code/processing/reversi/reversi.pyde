board = [[0] * 10 for _ in range(10)]
passCnt = 0

def setup():
    global side
    size(400, 400)
    side = height // 8
    startPosition()
    showBoard()
    
def draw():
    passCheck()
    
def mousePressed():
    global bw
    i = mouseX // side + 1
    j = mouseY // side + 1
    if validMove(i, j):
        movePiece(i, j)
        bw = -bw
        showBoard()

def keyPressed():
    if key == 'r':
        startPosition()
        showBoard()
        
def startPosition():
    global bw
    bw = 1
    for i in range(10):
        for j in range(10):
            if (i == 4 and j == 5) or (i == 5 and j == 4):
                board[i][j] = 1
            elif (i == 4 and j == 4) or (i == 5 and j == 5):
                board[i][j] = -1
            elif i == 0 or j == 0 or i == 9 or j == 9:
                board[i][j] = 2
            else:
                board[i][j] = 0
                
def showBoard():
    global num0, numB, numW, passCnt
    background(0, 160, 0)
    stroke(0)
    for i in range(1, 9):
        line(i * side, 0, i * side, height)
        line(0, i * side, 8 * side, i * side)

    noStroke()
    num0, numB, numW = 0, 0, 0
    for i in range(1, 9):
        for j in range(1, 9):
            if board[i][j] == 1:
                fill(0)
                ellipse((i-1)*side+side/2, (j-1)*side+side/2, 0.9*side, 0.9*side)
                numB += 1
            elif board[i][j] == -1:
                fill(255)
                ellipse((i-1)*side+side/2, (j-1)*side+side/2, 0.9*side, 0.9*side)
                numW += 1
            elif validMove(i, j):
                passCnt = 0
                num0 += 1
                if bw == -1:
                    fill(255, 255, 255, 200)
                elif bw == 1:
                    fill(0, 0, 0, 200)
                ellipse((i-1)*side+side/2, (j-1)*side+side/2, side/3, side/3)

def validMove(i, j):
    if i < 1 or 8 < i or j < 1 or 8 < j:
        return False
    if board[i][j] != 0:
        return False
    for di in range(-1, 2):
        for dj in range(-1, 2):
            ri = i + di
            rj = j + dj
            while board[ri][rj] == -bw:
                ri += di
                rj += dj
                if board[ri][rj] == bw:
                    return True
    return False

def movePiece(i, j):
    board[i][j] = bw
    for di in range(-1, 2):
        for dj in range(-1, 2):
            ri = i + di
            rj = j + dj    
            while board[ri][rj] == -bw:
                ri += di
                rj += dj
                if board[ri][rj] == bw:
                    ri -= di
                    rj -= dj
                    while not (i == ri and j == rj):
                        board[ri][rj] = bw
                        ri -= di
                        rj -= dj

def passCheck():
    global passCnt, bw
    if num0 == 0 and passCnt <= 1:
        passCnt += 1
        bw = -bw
        showBoard()
    if passCnt == 2:
        fill(255, 0, 0)
        textSize(1.0*side)
        textAlign(CENTER)
        if numW < numB:
            text("Black win", width/2, height/2)
        elif numB < numW:
            text("White win", width/2, height/2)
        else:
            text("Draw", width/2, height/2)
