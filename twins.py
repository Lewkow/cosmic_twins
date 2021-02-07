
from __future__ import division
import math
import sys
import os
import datetime
import random
import pygame
from helpers import *
from planet import Planet
from spaceship import Spaceship    


class MyGame(object):
    
    # defining and initializing game states
    PLAYING, DYING, GAME_OVER, STARTING, WELCOME = range(5)

    # defining custom events
    REFRESH, START, RESTART = range(pygame.USEREVENT, pygame.USEREVENT+3)
    
    
    def __init__(self):
        """Initialize a new game"""
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        self.width = 1300
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_scale = 1

        # use a black background
        self.bg_color = 0, 0, 0

        # get the default system font (with different sizes of 100, 50, 25)
        self.big_font = pygame.font.SysFont(None, 100)
        self.medium_font = pygame.font.SysFont(None, 50)
        self.small_font = pygame.font.SysFont(None, 25)
        # and make the game over text using the big font just loaded
        self.gameover_text = self.big_font.render('GAME OVER',\
            True, (255, 0, 0))

        # load a spaceship image (only used to display number of lives)
        self.lives_image = load_image_convert_alpha('spaceship.png')

        # Setup a timer to refresh the display FPS times per second
        self.FPS = 30
        pygame.time.set_timer(self.REFRESH, 1000//self.FPS)

        # display the welcome screen
        self.do_welcome()
    
    
    def get_screen_scale(self):
        current_space_x = self.spaceship.position.x * self.screen_scale
        current_space_y = self.spaceship.position.y * self.screen_scale
        
    
    def do_init(self):
        """This function is called in the beginning or when
        the game is restarted."""

        # holds the rocks
        self.rocks = []

        # minimum distance from spaceship when making rocks
        # this changes based on difficulty as the time passes
        self.min_rock_distance = 350

        # starting the game
        self.start()

        # initialize the number of lives and the score
        self.lives = 3
        self.score = 0

        # counter used to help count seconds
        self.counter = 0
    
    
    def do_welcome(self):
        """make a welcome screen"""

        # go to WELCOME state
        self.state = MyGame.WELCOME

        # making the welcome title and description
        self.welcome_asteroids = self.big_font.render("Cosmic Twins",\
                                                True, (255, 215, 0))
        self.welcome_desc =  self.medium_font.render(\
            "[Click anywhere/press Enter] to begin!", True, (35, 107, 142))
    

    def start(self):
        """Start the game by creating the spaceship object"""
        self.spaceship = Spaceship((self.width//2, self.height//2))
        self.planet = Planet((self.width//4, self.height//4))
        self.state = MyGame.PLAYING


    def physics(self):
        """Do spaceship physics here"""
        
        if self.state == MyGame.PLAYING:

            # call the move function of the object
            self.spaceship.move()


    def run(self):
        """Loop forever processing events"""
        running = True
        while running:
            event = pygame.event.wait()

            # player is asking to quit
            if event.type == pygame.QUIT:
                running = False

            # time to draw a new frame
            elif event.type == MyGame.REFRESH:
                
                if self.state != MyGame.WELCOME:

                    keys = pygame.key.get_pressed()

                    if self.state == MyGame.PLAYING:
                        angle_chunk = 5
                        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                            self.spaceship.angle -= angle_chunk
                            self.spaceship.angle %= 360

                        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                            self.spaceship.angle += angle_chunk
                            self.spaceship.angle %= 360

                        if keys[pygame.K_UP] or keys[pygame.K_w]:
                            
                            if self.spaceship.speed < 20:
                                boost = 0.01
                                self.spaceship.velocity.x += math.sin(-math.radians(self.spaceship.angle))*boost
                                self.spaceship.velocity.y += -math.cos(math.radians(self.spaceship.angle))*boost
                                self.spaceship.speed = self.spaceship.velocity.magnitude()

                        self.physics()

                self.draw()

            elif event.type == MyGame.START:
                pygame.time.set_timer(MyGame.START, 0)
                if self.lives < 1:
                    self.game_over()
                else:
                    self.start()

            # switch from game over screen to new game
            elif event.type == MyGame.RESTART:
                pygame.time.set_timer(MyGame.RESTART, 0) # turn the timer off
                self.state = MyGame.STARTING

            # user is clicking to start a new game
            elif event.type == pygame.MOUSEBUTTONDOWN \
                    and (self.state == MyGame.STARTING or\
                            self.state == MyGame.WELCOME):
                self.do_init()

            # user is pressing enter to start a new game
            elif event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_RETURN and \
                        (self.state == MyGame.STARTING or \
                            self.state == MyGame.WELCOME):
                self.do_init()

            else:
                pass # an event type we don't handle      


    def draw(self):
        """Update the display"""
        # everything we draw now is to a buffer that is not displayed
        self.screen.fill(self.bg_color)
    
        # if we are not on the welcome screen
        if self.state != MyGame.WELCOME:

            # draw the spaceship
            self.spaceship.draw_on(self.screen)
            self.planet.draw_on(self.screen)

            # if we are in game play mode
            if self.state == MyGame.PLAYING:

                # increment the counter by 1
                self.counter += 1

                if self.counter == 20*self.FPS:

                    # set the counter back to zero
                    self.counter = 0
                    
            draw_info(self.screen, self.width, self.medium_font, self.planet, self.spaceship)
            
            # update object clocks
            self.spaceship.progress_object_time()
            self.planet.progress_object_time()

        else:
            # draw the welcome texts
            draw_centered(self.welcome_asteroids, self.screen,\
                (self.width//2, self.height//2\
                    -self.welcome_asteroids.get_height()))

            draw_centered(self.welcome_desc, self.screen,\
                (self.width//2, self.height//2\
                    +self.welcome_desc.get_height()))

        # flip buffers so that everything we have drawn gets displayed
        pygame.display.flip()



MyGame().run()
pygame.quit()
sys.exit()
