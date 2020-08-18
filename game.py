'''
import pygame
import time
import random
pygame.init()


white = (255,255,255)
blue = (0,0,255)
red=(255,0,0)
black=(0,0,0)


bg = pygame.image.load('SNAKE.jpg')
char = pygame.image.load('snakes.png')
gameovercondition = False


dis_width = 480
dis_height = 360


dis = pygame.display.set_mode((dis_width,dis_width))
pygame.display.set_caption('Snake game by Milan')


clock = pygame.time.Clock()


block_snake = 10
snake_speed = 30

fontz = pygame.font.SysFont(None, 30)#creat a fonts object from the systems font

x1 = dis_width/2
y1 = dis_height/2
    
x1_change = 0 
y1_change = 0



def message(msg,color):
    mesg = fontz.render(msg,True,color)returns surface
    dis.blit(red,[dis_width/3,dis_height/3])
    
def redraw():    
    dis.blit(bg, (0,0))
    dis.blit(char,(x1,y1))   
    pygame.display.update()

def gameloop():
    gameovercondition = False
    game_close = False
    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_change = 0 
    y1_change = 0

    foodx = round(random.randrange(0,dis_width - block_snake) / 10.0) * 10,0
    foody = round(random.randrange(0,dis_width - block_snake) / 10.0) * 10.0
    
    while not gameovercondition:

        while game_close == True:
            dis.fill(bg)
            message("M-play again Q-quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or pygame.K_Q:
                        gameovercondition = True
                    if event.type == pygame.K_m or pygame.K_M:
                        gameloop()
    
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
        ##dis.fill(white) 
        pygame.draw.rect(dis, black, [x1, y1, block_snake, block_snake])    
        #pygame.draw.rect(dis, blue, [foodx, foody, block_snake, block_snake])

        #pygame.draw.rect(dis, red, [x1, y1, block_snake, block_snake])
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            print("mhmmmmmmmmm!!!!!!!!!!!!")
        clock.tick(snake_speed)


     
    redraw()
    pygame.quit()
    quit()

gameloop()    
'''


import pygame
import time
pygame.init()
white = (255,255,255)
blue = (0,0,255)
tp = (23,67,88)
red=(255,0,0)
black=(0,0,0)
dis_width = 600
dis_height = 500
dis = pygame.display.set_mode((dis_width,dis_width))
pygame.display.set_caption('Snake game by Milan')
gameovercondition = False
x1 = dis_width/2
y1 = dis_height/2
block_snake = 5
x1_change = 0
y1_change = 0
pygame.display.update()
clock = pygame.time.Clock()
snake_speed = 30
fontz = pygame.font.SysFont(None, 50)
bg = pygame.image.load('SNAKE.jpg')
char = pygame.image.load('snakes.png')



def message(msg,color):
    mesg = fontz.render(msg,True,color)
    dis.blit(mesg, [dis_width/2,dis_height/2])

def redraw():
    dis.blit(bg, (0,0))
    dis.blit(char,(x1,y1))   
    pygame.display.update()

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
    #dis.fill(blue)            
    pygame.draw.rect(dis, tp, [x1, y1, block_snake, block_snake])


    pygame.display.update()

    clock.tick(snake_speed)
        
    redraw()

message("YOU LOST!!!",black)
pygame.display.update()
time.sleep(2)


pygame.quit()
quit()
