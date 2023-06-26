import pygame
import random
import math

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
    def update(self, screen, people):
        self.move()
        if self.status == "sick":
            self.turnsSick += 1
            if self.turnsSick == self.recoveryTime:
                self.status = "recovered"
        self.checkCollidingWithWall(screen)
        for other in people:
            if self != other:  # ensure you don't check for collision with yourself
                if self.checkCollidingWithOther():
                    self.updateCollisionVelocities()
                    # update status
                    if self.status == "sick" and other.status == "healthy":
                        other.status = "sick"
                    elif other.status == "sick" and self.status == "healthy":
                        self.status = "sick"



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

    # return True if the self is colliding with the other, False otherwise
    def checkCollidingWithOther(self, other):
        distance = math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))
        if distance <= self.radius + other.radius:
            return True
        return False

    # update velocities on collision
    def updateCollisionVelocities(self, other):
        # type 1 collision - both objects are moving; neither is social distancing

        if not self.socialDistancing and not other.socialDistancing:
            tempVX = self.vx
            tempVY = self.vy
            self.vx = other.vx
            self.vy = other.vy
            other.vx = tempVX
            other.vy = tempVY

        # type 2 collision : one object that is social distancing and one that is not

        elif other.socialDistancing:
            # works okay, not great
            # self.vx *= -1
            # self.vy *= -1
            #
            # # works okay
            # tempVX = self.vx
            # self.vx = self.vy
            # self.vy = tempVX

            magV = math.sqrt(math.pow(self.vx, 2) + math.pow(self.vy, 2))
            tempVector = (self.vx + (self.x - other.x), self.vy + (self.y - other.y))
            magTempVector = math.sqrt(math.pow(tempVector[0], 2) + math.pow(tempVector[1], 2))
            normTempVector = (tempVector[0] / magTempVector, tempVector[1] / magTempVector)
            self.vx = normTempVector[0] * magV
            self.vy = normTempVector[1] * magV
