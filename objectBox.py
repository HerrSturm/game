import sys, pygame

class flyingBox(object):
    def __init__(self,position,rect, direction, color):
        self.position = position
        self.rect = rect
        self.shape = [self.position[0],self.position[1],self.rect[0],self.rect[1]]
        self.color = color
        self.direction = direction
        self.screen = pygame.display.get_surface()
        pygame.draw.rect(self.screen, self.color, self.shape, 0)

    def update(self):
        self.move()
        pygame.draw.rect(self.screen, self.color, self.shape, 0)

    def move(self):
        self.shape[0] = self.shape[0] + self.direction[0]
        if self.shape[0] > 700:
            self.shape[0] = 0
        if self.shape[0] < 0:
            self.shape[0] = 700
        self.shape[1] = self.shape[1] + self.direction[1]
        if self.shape[1] > 700:
            self.shape[1] = 0
        if self.shape[1] < 0:
            self.shape[1] = 700
        self.position[0] = self.shape[0]
        self.position[1] = self.shape[1]
