# import pygame and other modules
import pygame
import time
import random

# set the snake speed
snake_speed = 15

# set the window size
window_x = 720
window_y = 480

# set the color values in RGB format
black = pygame.Color (0, 0, 0)
white = pygame.Color (255, 255, 255)
red = pygame.Color (255, 0, 0)
green = pygame.Color (0, 255, 0)
blue = pygame.Color (0, 0, 255)

# initialize pygame
pygame.init ()

# create a game window
pygame.display.set_caption ('Snake Game')
game_window = pygame.display.set_mode ((window_x, window_y))

# create a clock object
fps = pygame.time.Clock ()

# initialize snake position and size
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# initialize food position randomly
food_position = [random.randrange (1, (window_x//10)) * 10,
                 random.randrange (1, (window_y//10)) * 10]
food_spawn = True

# initialize direction and change variables
direction = 'RIGHT'
change_to = direction

# initialize score
score = 0

# create a function to display the score
def show_score (choice, color, font, size):
    # create a font object
    score_font = pygame.font.SysFont (font, size)

    # create a surface object with the text
    score_surface = score_font.render ('Score : ' + str (score), True, color)

    # create a rectangular object for the text surface object
    score_rect = score_surface.get_rect ()

    # display the score at the given position
    game_window.blit (score_surface, score_rect)

# create a function to display the game over message
def game_over ():
    # create a font object
    my_font = pygame.font.SysFont ('times new roman', 50)

    # create a surface object with the text
    game_over_surface = my_font.render ('Your Score is : ' + str (score), True, red)

    # create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect ()

    # set the position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    # display the text on the window
    game_window.blit (game_over_surface, game_over_rect)
    pygame.display.flip ()

    # pause the game for 2 seconds
    time.sleep (2)

    # quit pygame and python
    pygame.quit ()
    quit ()

# main loop of the game
while True:
    # handle keyboard events
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit ()
            quit ()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # validate direction changes