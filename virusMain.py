import pygame
import random
from person import *


def main():
    pygame.init()
    # screen setup
    WIDTH = HEIGHT = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Virus simulation")
    screen.fill(pygame.Color('gray'))

    # clock setup
    clock = pygame.time.Clock()
    MAX_FPS = 20

    # variables
    running = True
    spawnBuffer = 10
    numPeople = 200
    factorOfPeopleSocialDistancing = 0.50

    # create people
    patientZero = Person(random.randint(spawnBuffer, WIDTH - spawnBuffer),
                         random.randint(spawnBuffer, HEIGHT - spawnBuffer), "sick", False)
    people = [patientZero]
    for i in range(numPeople - 1):
        socialDistancing = False
        if i < factorOfPeopleSocialDistancing * numPeople:  # percent of population that will practice social distancing
            socialDistancing = True

        person = None

        colliding = True
        while colliding:
            person = Person(random.randint(spawnBuffer, WIDTH - spawnBuffer),
                            random.randint(spawnBuffer, HEIGHT - spawnBuffer), "healthy", socialDistancing)
            colliding = False
            for person2 in people:
                if person.checkCollidingWithOther(person2):
                    colliding = True
                    break

        people.append(person)

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:  # clicked X in top right
                running = False

        # update people
        for person in people:
            person.update(screen, people)

        # update graphics
        screen.fill(pygame.Color('gray'))
        for person in people:
            person.draw(screen)
        pygame.display.flip()

        # pause for frames
        clock.tick(MAX_FPS)

    pygame.quit()


main()
