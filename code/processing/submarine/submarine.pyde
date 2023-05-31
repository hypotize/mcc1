class Game:
    INIT = -1
    TITLE = 0
    PLAY = 1
    OVER = 2
    titleImg = None
    bgImg = None
    KEY_LEFT = 0
    KEY_RIGHT = 1
    KEY_SPACE = 2
    keyState = [False] * 3
    @classmethod
    def loadImage(cls, titleFile, bgFile):
        cls.titleImg = loadImage(titleFile)
        cls.bgImg = loadImage(bgFile)
    @classmethod
    def setKey(cls, keyNo):
        Game.keyState[keyNo] = True
    @classmethod
    def clrKey(cls, keyNo):
        Game.keyState[keyNo] = False
    @classmethod
    def getKey(cls, keyNo):
        return Game.keyState[keyNo]
    def __init__(self):
        self.seq = Game.INIT
        self.score = -1
    def isTitle(self):
        return self.seq == Game.TITLE
    def isPlay(self):
        return self.seq == Game.PLAY
    def done(self):
        self.seq = Game.OVER
    def init(self):
        self.seq = Game.TITLE
        player.init()
        BombPlayer.cnt = 6
        for i in range(len(enemy)):
            enemy[i] = Enemy(Enemy.UNUSED, i * 20, 100 + i * 26, random(0.5, 2.5))
        for i in range(len(bombP)):
            bombP[i] = BombPlayer()
        for i in range(len(bombE)):
            bombE[i] = BombEnemy()
        for i in range(len(Game.keyState)):
            Game.keyState[i] = False
        self.score = 0        
        self.tcnt = 0
    def title(self):
        image(Game.titleImg, 0, 0, 600, 450)
        self.tcnt += 1
        if self.tcnt > 60 and (self.tcnt % 60) < 40:
            textSize(30)
            fill(40, 250, 40)
            text("Push any key!", 210, 320)
    def play(self):
        player.move()
        image(Game.bgImg, 0, 90, 600, 360)
        player.display()
        enemyMove()
        enemyDisp()
        bombPlayerMove()
        bombEnemyMove()
        self.scoreDisp()
    def over(self):
        print("game over")
        player.display()
        image(Game.bgImg, 0, 90, 600, 360)
        enemyDisp()
        bombEnemyMove()
        self.scoreDisp()
        if player.sink < 100:
            player.sink += 1
        if player.sink > 60:
            textSize(70)
            fill(255, 0, 0)
            text("GAME OVER", 110, 240)
            if self.tcnt > 60 and (self.tcnt % 60) < 40:
                textSize(30)
                fill(40, 250, 40)
                text("Push any key!", 210, 320)
            self.tcnt += 1
    def addScore(self, i):
        self.score += i
    def scoreDisp(self):
        textSize(24)
        fill(0, 0, 0)
        text("score: {}".format(self.score), 10, 25)
    def checkWaiting(self):
        if self.seq == Game.TITLE and self.tcnt > 60:
            self.seq = Game.PLAY
            self.tcnt = 0
        if self.seq == Game.OVER and self.tcnt > 60:
            self.init()
            self.seq = Game.PLAY
            self.tcnt = 0
    
game = Game()

class Player:
    img = None
    @classmethod
    def loadImage(cls, filename):
        cls.img = loadImage(filename)
    def __init__(self):
        self.w = 120
        self.init()
    def init(self):
        self.x = 240
        self.sink = 0
    def move(self):
        if Game.getKey(Game.KEY_LEFT) and self.x > 0:
            self.x -= 3
        if Game.getKey(Game.KEY_RIGHT) and self.x < width - self.w:
            self.x += 3
        if BombPlayer.wait > 0:
            BombPlayer.wait -= 1
        if Game.getKey(Game.KEY_SPACE) and BombPlayer.wait == 0:
            BombPlayer.wait = 10
            bombPlayerAdd()
    def display(self):
        image(Player.img, self.x, 58 + (self.sink / 2))
        
player = Player()

class Enemy:
    LEFT = 0
    RIGHT = 1
    EXPL1 = 2
    EXPL2 = 3
    UNUSED = 4
    img = [None] * 4
    @classmethod
    def loadImage(cls, files):
        for i in range(len(files)):
            cls.img[i] = loadImage(files[i])
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
    @classmethod
    def loadImage(cls, file):
        cls.img = loadImage(file)
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
    @classmethod
    def loadImage(cls, file):
        cls.img = loadImage(file)
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
    game.init()
    
def draw():
    background(0, 255, 255)
    if game.isTitle():
        game.title()
    elif game.isPlay():
        game.play()
    else:
        game.over()
           
def imgLoad():
    Game.loadImage("sm_title.png", "sm_bg.png")
    Player.loadImage("sm_player.png")
    Enemy.loadImage(["sm_enemyL.png", "sm_enemyR.png",
        "sm_explosion1.png", "sm_explosion2.png"])
    BombPlayer.loadImage("sm_bombP.png")
    BombEnemy.loadImage("sm_bombE.png")
               
def enemyMove():
    for e in enemy:
        e.move()
    if random(1000) < 20:
        enemyAdd()
    
def enemyDisp():
    for e in enemy:
        e.display()
        if e.isAlive():
            for b in bombP:
                if b.y < e.y + 21 and b.y + 16 > e.y and \
                    b.x < e.x + 76 and b.x + 10 > e.x:
                    b.unuse()
                    e.explosion()
                    game.addScore(100)
                    break
            else:
                if game.isPlay() and random(1000) < 10:
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
    for b in bombE:
        b.move()
        if b.y == 60 and b.x < player.x + player.w and b.x + 16 > player.x:
            game.done()
                           
def keyPressed():
    if key == CODED:
        if keyCode == LEFT:
            Game.setKey(Game.KEY_LEFT)
        if keyCode == RIGHT:
            Game.setKey(Game.KEY_RIGHT)
    if key == ' ':
        Game.setKey(Game.KEY_SPACE)
    game.checkWaiting()
        
def keyReleased():
    if key == CODED:
        if keyCode == LEFT:
            Game.clrKey(Game.KEY_LEFT)
        if keyCode == RIGHT:
            Game.clrKey(Game.KEY_RIGHT)
    if key == ' ':
        Game.clrKey(Game.KEY_SPACE)
