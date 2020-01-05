import sys, pygame, time, math, random, movement, gameEvent, objectBox
pygame.init()

size = width, height = 700, 700
speed = 3
ballPos = [350,700]
goal = [300,0,100,20]
direction = [speed,0]
black = (0, 0, 0)
blue = (0,0, 255)
red = (255,0,0)
hit = False
counter = 0

pygame.init()
screen = pygame.display.set_mode(size)

ball = pygame.draw.circle(screen,(255,255,255), ballPos,10)
goal = pygame.draw.rect(screen,(255,255,0),goal,0)
flyingObjects =  []
for i in range (5):
    flyingObjects.append(objectBox.flyingBox([200+50*i,200+ 80*i],(10,20),[4,0], blue))




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
    for i in flyingObjects:
        i.update()
    time.sleep(0.025)

    #checking out if goal is hit
    if gameEvent.collision(ballPos,[10,10],goal,[100,20]):
        ballPos = [350,680]
        flyingObjects.append(objectBox.flyingBox([200,200],(10,20),[4,0], red))
        speed +=1
        direction = [0,-speed]
        for i in flyingObjects:
            i.changeSpeed(1)
            i.randomPosition()
            print(len(flyingObjects))

    for i in flyingObjects:
        if gameEvent.collision(ballPos,[10,10],i.position,i.rect):
            sys.exit()

    pygame.display.flip()
