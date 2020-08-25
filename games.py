
import pygame
import time                  # importting libarys 
import random

pygame.init()#starting the program using init which initialize all pygame modules

white = (255,255,255)
black = (0,0,0)
red = (213,50,80) #assigng colours to there hexidecimal numbers
blue = (50,153,213)
green = (0,255,0)
yellow = (255,255,102)

dis_width = 600  #assignig the height and width to intergers 
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height)) #setting the height and width so the pop up box is the same size
pygame.display.set_caption("Snake game by Milan") #the name on top of the pop up box is in the string
clock = pygame.time.Clock()#this is created to keep track of time

snake_block = 10# these are the borders of how far the snake can go
snake_speed = 15 #assigning speed of snake to int

font_style = pygame.font.SysFont("bahnschrift",25)# these are font objects created from the system
score_font = pygame.font.SysFont("comicsansms",35)#the string is a type of font
'''
bg = pygame.image.load('SNAKE.jpg')
char = pygame.image.load('snakes.png')
'''
x1 = dis_width / 2 # new variable x1 divides the width and height of di
y1 = dis_height / 2


def Your_score(score):#definng the score that is diplayed on the top left
    value = score_font.render("Your Score: " + str(score), True, yellow) #defing a variavle value and drawing text on the surfaceand using a colour variable and displaying the score
    dis.blit(value, [0, 0])#putting it on the value/cooridinates of the pop up box
 
def our_snake(snake_block, snake_list):#defing making the snake
    for x in snake_list:#for loop to show everytime the score goes up then the snake gets bigger
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])#making the snake bigger by one everytime the score goes up

def message(msg,color):#this defines message so later o n you can write a message and it will output on the screen
    mesg = font_style.render(msg, True, color) #assigning a variable so you can display text onto the display 
    dis.blit(mesg, [dis_width / 6, dis_height / 3]) #the will draw or display the image or letter
'''
def redraw():
    dis.blit(bg, (0,0))
    dis.blit(char,(x1,y1))   
   pygame.display.update()
'''
def gameLoop():#this is defing the loop of the game
    game_over = False#setting conditions to the game so if is true game will be over
    game_close = False
    
    x1 = dis_width / 2 # new variable x1 divides the width and height of di
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []#making an array
    Lenght_of_snake = 1#giving the lenght of the snake

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0#this is where the food is placed as it is rounded so it is placed anywhere on the grid and it does not land on the same play again and a again
    foody = round(random.randrange(0,dis_height - snake_block) / 10.0) * 10.0#also it selects a random number inbetwwen the equation
    
    while not game_over:#stating a loop

        while game_close == True: #whilke loop with condition
            #dis.fill(blue)#this makes the pop up box blue you can change the colour 
            message("You Lost! Press C-Play Again or Q-Quit", red)#This is where the message function comes in use and if you lose it will output this on the screen
            Your_score(Lenght_of_snake - 1)#this will display lenght of snake - 1 because that is the initial size of the snake
            pygame.display.update()
            
            for event in pygame.event.get():#return lists of pending events
                if event.type == pygame.KEYDOWN:#this is to see if the key on the keyboard is presses and is checing
                    if event.key == pygame.K_q:#this is saying that if the key is q then gane over 
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:#if the key pressed is c continue
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:#this is used if you pressed the left arrow
                    x1_change = -snake_block#if you pressed left then it is minus as that is left
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:#used if you press right arrow
                    x1_change = snake_block#then it remains posotive as youyo go right
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block#negative as the grid works like that
                    x1_change = 0
                elif event.key == pygame.K_DOWN:         
                    y1_change = snake_block
                    x1_change = 0
            
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:#if any of these conditions are truie the game is closed
            game_close = True
        x1 += x1_change#this just adds it after the loop
        y1 += y1_change
        #dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])#this draws a green rectangle on the surface/display that cannot go ou the snake block 
        snake_head = []#new array
        snake_head.append(x1)#appending into array
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > Lenght_of_snake:#condition
            del snake_list[0]#delete first item in the listand will loop through
        
        for x in snake_list[:-1]:#prits on newline
            if x == snake_head:#condition
                game_close = True

        our_snake(snake_block, snake_list)#calling functions
        Your_score(Lenght_of_snake - 1)
        
        pygame.display.update()

        if x1 == foodx and y1 == foody:#condition
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Lenght_of_snake += 1#add lenght to snake
 
        clock.tick(snake_speed)#this will output with the time it took
        
       # redraw()

    pygame.quit()#code finished
    quit()



gameLoop()#calling the loop

