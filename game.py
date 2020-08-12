
import pygame
import time
pygame.init()
white = (255,255,255)
blue = (0,0,255)
red=(255,0,0)
black=(0,0,0)
dis_width = 500
dis_height = 400
dis = pygame.display.set_mode((dis_width,dis_width))
pygame.display.set_caption('Snake game by Milan')
gameovercondition = False
x1 = dis_width/2
y1 = dis_height/2
block_snake = 10
x1_change = 0
y1_change = 0
pygame.display.update()
clock = pygame.time.Clock()
snake_speed = 30
fontz = pygame.font.SysFont(None, 50)
def message(msg,color):
    mesg = fontz.render(msg,True,color)
    dis.blit(mesg, [dis_width/2,dis_height/2])

while not gameovercondition:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameovercondition=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -block_snake
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = block_snake
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -block_snake
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = block_snake
                x1_change = 0
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        gameovercondition = True
    
    x1 += x1_change
    y1 += y1_change
    dis.fill(blue)            
    pygame.draw.rect(dis, red, [x1, y1, block_snake, block_snake])
    
   
    pygame.display.update()
   
    clock.tick(snake_speed)

message("YOU LOST!!!",black)
pygame.display.update()
time.sleep(2)

        

pygame.quit()
quit()

