# import the connect_database function
# and the database_version variable
# from database.py into the current file
import pygame
import sys
from logger import *
from player import Player
from database import connect_database, database_version
from constants import *  
from logger import log_state
from asteroid import Asteroid
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # starting positions 
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # create a new game clock object
    clock = pygame.time.Clock()

    # dela time var
    dt = 0

    #create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()   
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #add the player class to the groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)    
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    
    # create an instance of the Player, Asteroid, and AsteroidField class
    p1 = Player(x, y)
    af1 = AsteroidField()

    # log the game state
    # check to see if the user has closed the game
    # fill the screen with black
    # update the items in the updatable group
    # for all the asteroids in the asteroids group, 
        # check to see if they collide with the player
            # if so,log a player hit, print game over, and exit
    # for each item in the drawable group
        # draw them to the screen
    # flip the display (tick over)
    while (True):
        log_state()
        # check to see if the user has closed the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        updatable.update(dt)

        for asteroid in asteroids:
            if p1.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

            for shot in shots: 
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        
        for item in drawable:
            item.draw(screen)
        #for all the drawables 
        dt = clock.tick(60)/1000
        pygame.display.flip()
        # print(dt)

if __name__ == "__main__":
    main()
