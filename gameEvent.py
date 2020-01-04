import math

def collision (pos1, rect1, pos2, rect2):
    if abs(pos1[0]+rect1[0] - (pos2[0]+rect2[0])) < (rect1[0]+rect2[0])/2 and abs((pos1[1]+rect1[1]) - (pos2[1]+rect2[1])) <  (rect1[1] + rect2[1])/2:
        return True
    return False
