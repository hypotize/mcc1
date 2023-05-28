GAME_INIT = 0
GAME_EXEC = 1
GAME_OVER = 2
gseq = GAME_INIT
title = None
bg = None
score = 0

keyState = [False] * 3

class Player:
    img = None
    def __init__(self):
        self.w = 120
        self.init()
    def init(self):
        self.x = 240
        self.sink = 0
        
player = Player()

class Enemy:
    LEFT = 0
    RIGHT = 1
    EXPL1 = 2
    EXPL2 = 3
    UNUSED = 4
    img = [None] * 4
    def __init__(self, d, x, y, speed):
        self.d = d
        self.x = x
        self.y = y
        self.speed = speed
        self.cnt = 0
    def display(self):
        if self.d != Enemy.UNUSED:
            image(Enemy.img[self.d], self.x, self.y)
    def isUsed(self):
        return self.d != Enemy.UNUSED
    def unuse(self):
        self.d = Enemy.UNUSED
    def isAlive(self):
        return self.d < Enemy.EXPL1
    def explosion(self):
        self.d = Enemy.EXPL1
        self.cnt = 60
    def move(self):
        if self.isAlive():
            self.x += self.speed
        if self.d == Enemy.LEFT and self.x < -80:
            self.unuse()
        elif self.d == Enemy.RIGHT and self.x > width:
            self.unuse()
    def inExplosion(self):
        self.cnt -= 1
        self.d = (self.cnt // 3) % 2 + Enemy.EXPL1
        if self.cnt == 0:
            self.unuse()

enemy = [None] * 12

class BombPlayer:
    img = None
    cnt = 6
    wait = 0
    def __init__(self):
        self.x = 0
        self.y = 0
    def shot(self, x, y):
        self.x = x
        self.y = y
        BombPlayer.cnt -= 1
    def unuse(self):
        self.y = 0
        BombPlayer.cnt += 1
    def isUsed(self):
        return self.y > 0
    def move(self):
        if self.isUsed():
            self.y += 2
            if self.y > 450:
                self.unuse()
        if self.isUsed():
            image(BombPlayer.img, self.x, self.y)
        for i in range(BombPlayer.cnt):
            image(BombPlayer.img, 230 + i * 26, 20) 

class BombEnemy:
    img = None
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cnt = 0
    def shot(self, x, y):
        self.x = x
        self.y = y
    def unuse(self):
        self.y = 0
    def isUsed(self):
        return self.y > 0
    def explosion(self):
        self.y = 60
        self.cnt = 10
    def isExplosion(self):
        return self.cnt > 0
    def move(self):
        if self.y > 60:
            self.y -= 1
            if self.y < 90:
                self.explosion()
        if self.isExplosion():
            fill(255, 80, 10)
            rect(self.x, self.y, 16, 30)
            self.cnt -= 1
            if self.cnt == 0:
                self.unuse()
        elif self.isUsed():
            image(BombEnemy.img, self.x, self.y)              
       
bombP = [None] * 6
bombE = [None] * 20

def setup():
    size(600, 450)
    noStroke()
    frameRate(30)
    imgLoad()
    gameInit()
    
def draw():
    background(0, 255, 255)
    if gseq == GAME_INIT:
        gameTitle()
    elif gseq == GAME_EXEC:
        gamePlay()
    else:
        gameOver()
        
def gameInit():
    global gseq, player, enemy, bombP, bombE, keyState, score
    gseq = GAME_INIT
    player.init()
    BombPlayer.cnt = 6
    for i in range(12):
        enemy[i] = Enemy(Enemy.UNUSED, i * 20, 100 + i * 26, random(0.5, 2.5))
    for i in range(6):
        bombP[i] = BombPlayer()
    for i in range(20):
        bombE[i] = BombEnemy()
    for i in range(3):
        keyState[i] = False
    score = 0
    
tcnt = 0
def gameTitle():
    global tcnt
    image(title, 0, 0, 600, 450)
    tcnt += 1
    if tcnt > 60 and (tcnt % 60) < 40:
        textSize(30)
        fill(40, 250, 40)
        text("Push any key!", 210, 320)
    
def gamePlay():
    playerMove()
    image(bg, 0, 90, 600, 360)
    image(Player.img, player.x, 58)
    enemyMove()
    enemyDisp()
    bombPlayerMove()
    bombEnemyMove()
    scoreDisp()
    
def gameOver():
    global player, tcnt
    image(Player.img, player.x, 58 + (player.sink / 2))
    image(bg, 0, 90, 600, 360)
    enemyDisp()
    bombEnemyMove()
    scoreDisp()
    if player.sink < 100:
        player.sink += 1
    if player.sink > 60:
        textSize(70)
        fill(255, 0, 0)
        text("GAME OVER", 110, 240)
        if tcnt > 60 and (tcnt % 60) < 40:
            textSize(30)
            fill(40, 250, 40)
            text("Push any key!", 210, 320)
        tcnt += 1
    
def imgLoad():
    global bg, title
    bg = loadImage("sm_bg.png")
    Player.img = loadImage("sm_player.png")
    Enemy.img[Enemy.LEFT] = loadImage("sm_enemyL.png")
    Enemy.img[Enemy.RIGHT] = loadImage("sm_enemyR.png")
    Enemy.img[Enemy.EXPL1] = loadImage("sm_explosion1.png")
    Enemy.img[Enemy.EXPL2] = loadImage("sm_explosion2.png")
    BombPlayer.img = loadImage("sm_bombP.png")
    BombEnemy.img = loadImage("sm_bombE.png")
    title = loadImage("sm_title.png")
    
def playerMove():
    global player
    if keyState[0] and player.x > 0:
        player.x -= 3
    if keyState[1] and player.x < width - player.w:
        player.x += 3
    if BombPlayer.wait > 0:
        BombPlayer.wait -= 1
    if keyState[2] and BombPlayer.wait == 0:
        BombPlayer.wait = 10
        bombPlayerAdd()
            
def enemyMove():
    for e in enemy:
        e.move()
    if random(1000) < 20:
        enemyAdd()
    
def enemyDisp():
    global score
    for e in enemy:
        e.display()
        if e.isAlive():
            for b in bombP:
                if b.y < e.y + 21 and b.y + 16 > e.y and \
                    b.x < e.x + 76 and b.x + 10 > e.x:
                    b.unuse()
                    e.explosion()
                    score += 100
                    break
            else:
                if gseq == 1 and random(1000) < 10:
                    bombEnemyAdd(int(e.x), e.y)
        elif e.isUsed():
            e.inExplosion()

def enemyAdd():
    for e in enemy:
        if not e.isUsed():
            e.speed = random(0.5, 2.5)
            if random(100) < 50:
                e.d = Enemy.LEFT
                e.x = width
                e.speed = -e.speed
            else:
                e.d = Enemy.RIGHT
                e.x = -80
            e.y = int(random(120, 420))
            break

def bombPlayerAdd():
    for b in bombP:
        if not b.isUsed():
            b.shot(player.x + player.w / 2, 90)
            break
        
def bombPlayerMove():
    for b in bombP:
        b.move()
        
def bombEnemyAdd(x, y):
    for b in bombE:
        if not b.isUsed():
            b.shot(x + 38, y)
            break
        
def bombEnemyMove():
    global gseq
    for b in bombE:
        b.move()
        if b.y == 60 and b.x < player.x + player.w and b.x + 16 > player.x:
            gseq = GAME_OVER
            
def scoreDisp():
    textSize(24)
    fill(0, 0, 0)
    text("score: {}".format(score), 10, 25)
                
def keyPressed():
    global keyState, gseq, tcnt
    if key == CODED:
        if keyCode == LEFT:
            keyState[0] = True
        if keyCode == RIGHT:
            keyState[1] = True
    if key == ' ':
        keyState[2] = True
    if gseq == 0 and tcnt > 60:
        gseq = GAME_EXEC
        tcnt = 0
    if gseq == 2 and tcnt > 60:
        gameInit()
        gseq = GAME_EXEC
        tcnt = 0
        
def keyReleased():
    global keyState
    if key == CODED:
        if keyCode == LEFT:
            keyState[0] = False
        if keyCode == RIGHT:
            keyState[1] = False
    if key == ' ':
        keyState[2] = False
