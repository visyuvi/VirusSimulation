import pygame
import random

minMovement = 0.5
maxSpeed = 5


class Person:
    colors = {"healthy": "white", "sick": "red", "recovered": "blue"}

    # status - "healthy" , "sick" or "recovered"
    def __init__(self, x, y, status, socialDistancing):
        self.x = x
        self.y = y
        self.status = status
        self.socialDistancing = socialDistancing
        self.radius = 6
        self.vx = 0
        self.vy = 0
        self.turnsSick = 0
        self.recoveryTime = random.randint(100, 150)

        if not self.socialDistancing:
            while -minMovement < self.vx < minMovement and -minMovement < self.vy < minMovement:
                self.vx = random.uniform(-maxSpeed, maxSpeed)
                self.vy = random.uniform(-maxSpeed, maxSpeed)

    # screen - the main surface
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(self.colors[self.status]), (round(self.x), round(self.y)), self.radius)

    # execute once per frame
    def update(self):
        self.move()
        if self.status == "sick":
            self.turnsSick += 1
            if self.turnsSick == self.recoveryTime:
                self.status = "recovered"

    def move(self, ):
        if not self.socialDistancing:
            self.x += self.vx
            self.y += self.vy
