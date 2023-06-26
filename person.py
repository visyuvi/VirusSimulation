import pygame
import random

minMovement = 0.5
maxSpeed = 20


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
    def update(self, screen):
        self.move()
        self.checkCollidingWithWall(screen)
        if self.status == "sick":
            self.turnsSick += 1
            if self.turnsSick == self.recoveryTime:
                self.status = "recovered"

    def move(self, ):
        if not self.socialDistancing:
            self.x += self.vx
            self.y += self.vy

    # check for collisions with walls and update velocities
    def checkCollidingWithWall(self, screen):
        if self.x + self.radius >= screen.get_width() and self.vx > 0:  # self.vx > 0 is to prevent it from getting
            # stuck to the wall
            self.vx *= -1
        elif self.x - self.radius <= 0 and self.vx < 0:
            self.vx *= -1
        if self.y + self.radius >= screen.get_height() and self.vy > 0:
            self.vy *= -1
        elif self.y - self.radius <= 0 and self.vy < 0:
            self.vy *= -1
