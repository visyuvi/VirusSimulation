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

    # create people
    patientZero = Person(random.randint(spawnBuffer, WIDTH - spawnBuffer), random.randint(spawnBuffer, HEIGHT - spawnBuffer), "sick", False)

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:  # clicked X in top right
                running = False

        # update people
        patientZero.update(screen, [])

        # update graphics
        screen.fill(pygame.Color('gray'))
        patientZero.draw(screen)
        pygame.display.flip()

        # pause for frames
        clock.tick(MAX_FPS)

    pygame.quit()


main()
