# import the connect_database function
# and the database_version variable
# from database.py into the current file
import pygame
from database import connect_database, database_version
from constants import *  

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
