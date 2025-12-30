# import the connect_database function
# and the database_version variable
# from database.py into the current file
import pygame
from player import Player
from database import connect_database, database_version
from constants import *  
from logger import log_state


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # starting positions 
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    p1 = Player(x, y)

    # create a new game clock object
    clock = pygame.time.Clock()

    # dela time var
    dt = 0

    while (True):
        log_state()
        # check to see if the user has closed the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        p1.update(dt)
        p1.draw(screen)
        dt = clock.tick(60)/1000
        pygame.display.flip()
        # print(dt)

if __name__ == "__main__":
    main()
