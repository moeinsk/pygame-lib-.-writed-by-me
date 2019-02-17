# writed by = moeinpro
import pygame
import time
import random

pygame.init()

#it's for play sound on game
crash_sound = pygame.mixer.Sound("lose-m.wav")
pygame.mixer.music.load("world-m.ogg")



#width and  height for game window
display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)


gameDisplay = pygame.display.set_mode((display_width,display_height))
#it's name the game
pygame.display.set_caption('Race Car')

clock = pygame.time.Clock()
#for locationing img
carImg = pygame.image.load("bug.png")

car_width = 48  
#for mouse
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    #print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
            #if action == "play":
                #game_loop()
            #elif action == "quit":
                #pygame.quit()
                #quit()    
            
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    TextSurf,TextRect = text_objects(msg,smallText)
    TextRect.center = ((x+(w/2)),(y + (h/2)))
    gameDisplay.blit(TextSurf,TextRect)  

#seconde ravesh for exit
def quitgame():
    pygame.quit()
    quit()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = text_objects("Let's Play Game",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        button("Try Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()

#stuff_dodged func
def stuff_dodged(count):
    font = pygame.font.SysFont(None , 25)
    text = font.render("score : "+str(count) , True , red)
    gameDisplay.blit(text,(0,0))


def stuff(stuffx,stuffy,stuffw,stuffh,color):
    pygame.draw.rect(gameDisplay,color,[stuffx,stuffy,stuffw,stuffh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True , black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()
#lose func
def crash ():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
#Game exite font thise fontt at www.pygame
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects("You Crashed",largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Try Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)        

        pygame.display.update()

            
#Game loop fu

def game_loop():

    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)   

    x_change = 0

    stuff_startx = random.randrange(0,display_width)
    stuff_starty = -700
    stuff_speed = 7
    stuff_width = 100
    stuff_height = 100

    dodged = 0

    gameExit = False
    #game exit .... YOU CRASHED

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0          


        x += x_change
        gameDisplay.fill(white)

        #stuffx,stuffy,stuffw,stuffh,color
        stuff(stuff_startx,stuff_starty,stuff_width,stuff_height,red)
        stuff_starty += stuff_speed

        stuff_dodged(dodged)

        car(x,y)        

        if x > display_width - car_width or x < 0:
            crash()

        if stuff_starty > display_height:
            stuff_starty = 0 - stuff_height
            stuff_startx = random.randrange(0,display_width)   
            dodged += 1
            stuff_speed += 1

            #if (dodged % 5 == 0):
                

            

        if y < stuff_starty + stuff_height:
            if x > stuff_startx and x < stuff_startx + stuff_width or x + car_width > stuff_startx and x + car_width < stuff_startx + stuff_width:
                crash()    


        pygame.display.update()
        #frame persconde
        clock.tick(60)
        #صدا زدن فانکشن ها
game_intro()
game_loop()
pygame.quit()
quit()
