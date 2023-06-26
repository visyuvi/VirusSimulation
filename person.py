import random

minMovement = 0.5
maxSpeed = 5


class Person:

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

        if not self.socialDistancing:
            while -minMovement < self.vx < minMovement and -minMovement < self.vy < minMovement:
                self.vx = random.uniform(-maxSpeed, maxSpeed)
                self.vy = random.uniform(-maxSpeed, maxSpeed)

    def move(self, ):
        if not self.socialDistancing:
            self.x += self.vx
            self.y += self.vy
