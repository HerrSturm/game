import sys, pygame, time, math, movement, gameEvent
pygame.init()

size = width, height = 700, 700
speed = 3
ballPos = [350,350]
goal = [300,0,100,20]
direction = [speed,0]
black = 0, 0, 0
hit = False
counter = 0

pygame.init()
screen = pygame.display.set_mode(size)

ball = pygame.draw.circle(screen,(255,255,255), ballPos,10)
goal = pygame.draw.rect(screen,(255,255,0),goal,0)
pygame.display.flip()




while not(hit):
    #handles the shutting down of the programm
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed() #gets the pressed keys
    #movement handling
    if keys[pygame.K_LEFT]:
        direction = movement.drehungLeft(direction,speed)
    if keys[pygame.K_RIGHT]:
        direction = movement.drehungRight(direction,speed)
    #handling of closing the game via ESC
    if keys[pygame.K_ESCAPE]:
        sys.exit()

    #updating the screen
    ballPos = movement.bewegung(ballPos, direction)
    screen = pygame.display.set_mode(size)
    goal = pygame.draw.rect(screen,(255,255,0),(300,0,100,20),0)
    ball = pygame.draw.circle(screen,(255,255,255), ballPos,10)
    time.sleep(0.025)

    #checking out if goal is hit
    hit = gameEvent.collision(ballPos,[10,10],goal,[100,20])

    #accelerating the ball
    counter+= 1
    if counter == 1000:
        speed +=1
        counter = 0
        print(speed)
    pygame.display.flip()
    print(direction)
