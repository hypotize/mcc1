import pygame
 
# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


bigsquare = 800
smallsquare = 10
boost = 3
 
def draw(i):

    x = smallsquare * i
    y = smallsquare * i
    width = smallsquare * boost
    height = smallsquare * boost
    # https://www.pygame.org/docs/ref/draw.html

    pygame.draw.rect(screen,red,[x, y, width, height],1)
    #pygame.draw.circle(screen,red,[x, y],width,1)

    bluex = bigsquare - x - smallsquare 
    
    pygame.draw.rect(screen,blue,[bluex, y, width, height],1)
        
 
pygame.init()
 
# Set the height and width of the screen
screensize = [bigsquare, bigsquare]
screen = pygame.display.set_mode(screensize)
 
pygame.display.set_caption("Miura Computer Club")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
screen.fill(white)

count = (bigsquare - smallsquare) / smallsquare
i = count

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Set the screen background
    if i >=0:
        draw(i)
        i -=1 
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(10)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
