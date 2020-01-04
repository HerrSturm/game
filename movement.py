import math

def bewegung(ballPos, direction):
    ballPos[0] = ballPos[0] + int(round(direction[0]))
    ballPos[1] = ballPos[1] + int(round(direction[1]))
    if ballPos[0] > 700:
        ballPos[0] = 0
    if ballPos[1] > 700:
        ballPos[1] = 0
    if ballPos[0] < 0:
        ballPos[0] = 700
    if ballPos[1] < 0:
        ballPos[1] = 700
    return ballPos


def drehungRight(direction,speed):
    #x und y positiv
    if  direction[1] >= 0 and direction[0] > 0:
        direction[1] += 1
        direction[0] = math.sqrt(speed**2-direction[1]**2)
    #x negativ, y positiv
    elif direction[1] > 0 and direction[0] <= 0:
        direction[1] -= 1
        direction[0] = math.sqrt(speed**2-direction[1]**2)*-1
    #x negativ, y negativ
    elif direction[1] <= 0 and direction[0] < 0:
        direction[1] -= 1
        direction[0] = math.sqrt(speed**2-direction[1]**2)*-1
    #x positiv y negativ
    elif direction[1] < 0 and direction[0] >= 0:
        direction[1] += 1
        direction[0] = math.sqrt(speed**2-direction[1]**2)
    return direction

def drehungLeft(direction,speed):
    #x positiv y negativ
    if direction[1] <= 0 and direction[0] > 0:
        direction[1] -= 1
        direction[0] = math.sqrt(speed**2-direction[1]**2)
    #x und y positiv
    elif  direction[1] > 0 and direction[0] >= 0:
        direction[1] -= 1
        direction[0] = math.sqrt(speed**2-direction[1]**2)
    #x negativ, y positiv
    elif direction[1] >= 0 and direction[0] < 0:
        direction[1] += 1
        direction[0] = math.sqrt(speed**2-direction[1]**2)*-1
    #x negativ, y negativ
    elif direction[1] < 0 and direction[0] <= 0:
        direction[1] += 1
        direction[0] = math.sqrt(speed**2-direction[1]**2)*-1
    return direction
