# import the connect_database function
# and the database_version variable
# from database.py into the current file
import pygame
from database import connect_database, database_version
from constants import *  
from logger import log_state

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while (True):
        log_state()
        # check to see if the user has closed the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
