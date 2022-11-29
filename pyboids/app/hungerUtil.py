import pygame
from . import boid


def __init__(self):
        self.count = 0
        self.boidList = []

def addBoid(self, boid):
        self.boidList.add(boid)
        self.count = self.count + 1
     
def tick(self):
        for i in range(len(self.boidList) - 1, -1, -1):
            self.boidList[i].hunger = self.boidList[i].hunger - 1
            if self.boidList[i] <= 0:
                # TODO: kill boid here
                del self.boidList[i]
                
def init():
    hungerTick = pygame.USEREVENT + 1
    pygame.time.set_timer(hungerTick, 3000)