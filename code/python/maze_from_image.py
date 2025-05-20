import pygame
import sys
from pygame.locals import *
import random
from PIL import Image

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

size = 20

cursor_x = 1
cursor_y = 1

def is_black(r, g, b, threshold=60):
    """Return True if the pixel is considered black based on brightness."""
    return (r + g + b) / 3 < threshold

def image_to_maze(image_path, size=30):
    """Convert an image to a Python maze matrix of 0s and 1s."""
    img = Image.open(image_path).convert("RGB")
    img = img.resize((size, size), Image.Resampling.NEAREST)

    matrix = []
    for y in range(size):
        row = []
        for x in range(size):
            r, g, b = img.getpixel((x, y))
            row.append(1 if is_black(r, g, b) else 0)
        matrix.append(row)

    return matrix

image_path = sys.argv[1] if len(sys.argv) > 1 else "maze.jpg"
maze = image_to_maze(image_path)

goal_x = len(maze) -2
goal_y = len(maze) -2

create_random = False

if create_random:
    row = 1
    while row < len(maze) -1: 
        col = 1
        m = maze[row]
        while col < len(m) -1:
            r = random.randint(0,4)
            if r == 0:
                val = 1
            else:
                val = 0
            maze[col][row] = val
            col += 1
        row += 1
    maze[-2][-2] = 0
    maze[1][1] = 0        

def draw():
    row = 0
    while row < len(maze): 
        col = 0
        m = maze[row]
        while col < len(m):
            val = maze[col][row]
            if val == 1:
                pygame.draw.rect(screen,black,[row * size, col * size, size,size], 0)
            col += 1
        row += 1

    pygame.draw.rect(screen,green,[cursor_x * size, cursor_y * size, size,size], 0)
    pygame.draw.rect(screen,red,[goal_x * size, goal_y * size, size,size], 0)

pygame.init()
 
# Set the height and width of the screen
screen_size = [size * len(maze), size * len(maze)]
screen = pygame.display.set_mode(screen_size)
 
pygame.display.set_caption("Maaaaaaze")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# RUNNING | WON | LOST 
game_state = "RUNNING"
start_time = pygame.time.get_ticks()
running_time  = "0"

# -------- Main Program Loop -----------
while not done:

    #イベント処理
    had_event = False
    for event in pygame.event.get():
        had_event = True

        #画面を閉じるボタン
        if event.type == QUIT:
            pygame.quit()
        
        #キーが押されたとき
        if event.type == KEYDOWN:
            if event.key == K_q or event.key == K_ESCAPE:
                pygame.quit()
            
            if game_state == "RUNNING":                 
                #カーソル移動
                if event.key == K_UP:
                    cursor_y -= 1
                if event.key == K_DOWN:
                    cursor_y += 1
                if event.key == K_LEFT:
                    cursor_x -= 1
                if event.key == K_RIGHT:
                    cursor_x += 1
            elif event.key == K_r:
                cursor_x = 1
                cursor_y = 1
                start_time = pygame.time.get_ticks()
                game_state = "RUNNING"

    sz = len(maze)
    if cursor_x < 0:
        cursor_x = 0
    if cursor_y < 0:
        cursor_y = 0
    if cursor_x >= sz:
        cursor_x = sz -1
    if cursor_y >= sz:
        cursor_y = sz -1
            
    screen.fill(white)
    draw()

    if cursor_x == goal_x and cursor_y == goal_y:
        game_state = "WON -                R TO RESTART"
    if maze[cursor_y][cursor_x] == 1:
        game_state = "LOST -               R TO RESTART"

    font = pygame.font.SysFont('arial', 15)
    if game_state == "RUNNING":
        running_time = str(pygame.time.get_ticks() - start_time)        
    else:
        statetext = font.render(game_state, True, green)
        screen.blit(statetext, (2,2)) 

    timetext = font.render(running_time, True, green)
    screen.blit(timetext, (52,2))
        
    pygame.display.flip()
    clock.tick(20)
 
pygame.quit()
