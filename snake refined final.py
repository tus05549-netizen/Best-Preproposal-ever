# importing libraries
import pygame
import time
import random

user_speed = input("Do you want the snake to go fast, normal or slow: ")
if user_speed.lower().strip() in ["fast", 'f']:
    snake_speed = 30
elif user_speed.lower().strip() in ["slow", 's']:
    snake_speed = 15
else:
    snake_speed = 22 

# What mode?
mode = input("How many players: one or two")
# Window size
window_size = input("How big should the window be (pocket_sized, small, medium, large, boulder-sized): ")
window_size = window_size.lower().strip()
current_size = ""
while current_size == "":
    if window_size in ["s", "small"]:
        window_x = 480
        window_y = 480
        current_size = window_size
    elif window_size in ["m", "medium"]:
        window_x = 600
        window_y = 600
        current_size = window_size
    elif window_size in ["l", "large"]:
        window_x = 720
        window_y = 720
        current_size = window_size
    elif window_size in ["p", "pocket", "pocket-sized"]:
        window_x = 360
        window_y = 360
        current_size = window_size
    elif window_size in ["b", "boulder", "boulder-sized"]:
        window_x = 840
        window_y = 840
        current_size = window_size
    else:
        window_size = input("Please enter small, medium, or large! ")
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
orange = pygame.Color(255, 165, 0)
yellow = pygame.Color(255, 255, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
grey = pygame.Color(122, 122, 122)
lime = pygame.Color(65, 255, 0)
maroon = pygame.Color(128, 0, 0)
pink = pygame.Color(255, 105, 180)
purple = pygame.Color(191, 0, 255)
cerulean = pygame.Color(135, 206, 250)
navy = pygame.Color(25, 25, 112)
coral = pygame.Color(255, 127, 80)
# color schemes
dark = [black, green, 'impact']
light = [grey, orange, 'calibri']
classic = [lime, blue, 'bookantiqua']
neon = [pink, purple, 'bauhaus93']
sky = [cerulean, black, 'comicsansms']
futuristic = [coral, navy, 'ocraextended']
'''hue_s = input("What color should the snake be: lime, green, yellow, blue, navy, purple, pink grey")
hue_b = input("What color should the snake be: orange, lime, green, yellow, blue, navy, purple, grey")
custom = []'''
scheme = input("What color scheme do you want (dark, light, classic, neon, sky, futuristic): ")
current = []
while current == []:
    scheme = scheme.lower().strip()
    if scheme in ['dark', "d"]:
        current = dark
    elif scheme in ["light", 'l']:
        current = light
    elif scheme in ["neon", 'n']:
        current = neon
    elif scheme in ["sky", 's']:
        current = sky
    elif scheme in ["futuristic", 'f']:
        current = futuristic
    elif scheme in ['classic', 'c']:
        current = classic
    else:
        scheme = input("Please enter the themes provided above! ")
# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()
# defining snake default position 
snake_position = [100, 50]

# defining first 4 blocks of snake
# body
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70, 50]
            ]
# fruit position 
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = False
pop_spawn = False
# power up border position
def random_border_position():
    side = random.choice(['top', 'bottom', 'left', 'right'])

    if side == 'top':
        return [random.randrange(0, window_x // 10) * 10, 0]
    elif side == 'bottom':
        return [random.randrange(0, window_x // 10) * 10, window_y - 10]
    elif side == 'left':
        return [0, random.randrange(0, window_y // 10) * 10]
    elif side == 'right':
        return [window_x - 10, random.randrange(0, window_y // 10) * 10]
pop_position = random_border_position()
# powerup position

 #[random.randrange(1, (window_x//10)) * 10,
                  #random.randrange(1, (window_y//10)) * 10]
# setting default snake direction 
# towards right
direction = 'RIGHT'
change_to = direction
# initial score
score = 0
fruit_count = 0

# displaying Score function
def show_score(choice, color, font, size):
  
    # creating font object score_font 
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the 
    # text surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)
    
# game over function
def game_over():
  
    # creating font object my_font
    my_font = pygame.font.SysFont(current[2], 36)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, maroon)
    
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # after 2 seconds we will quit the 
    # program
    time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()


# Main Function
while True:
  
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # If two keys pressed simultaneously 
    # we don't want snake to move into two directions
    # simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism 
    # if fruits and snakes collide then scores will be 
    # incremented by 10
    # Draw fruit
    game_window.fill(current[0])
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
        fruit_spawn = True
        
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1] and fruit_spawn:
        score += 10
        fruit_count += 1
        fruit_spawn = False
        game_window.fill(current[0])
    else:
        snake_body.pop()
        
    '''if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))'''
        
    #fruit_spawn = True
    #game_window.fill(current[0])
    
    '''for pos in snake_body:
        pygame.draw.rect(game_window, current[1], pygame.Rect(
          pos[0], pos[1], 10, 10))'''
        
    pygame.draw.rect(game_window, white, pygame.Rect(
      fruit_position[0], fruit_position[1], 10, 10))



# Clear screen ONCE
    #game_window.fill(current[0])

# Draw snake
    for pos in snake_body:
        pygame.draw.rect(game_window, current[1],
                     pygame.Rect(pos[0], pos[1], 10, 10))


# Draw powerup
    if fruit_count % 5 == 4:
        pop_spawn = True
    if pop_spawn:
        pygame.draw.rect(game_window, red,
                     pygame.Rect(pop_position[0], pop_position[1], 10, 10))
    # if powerups and snakes collide then scores will be 
    # incremented by 100
    #########
    '''
    #snake_body.insert(0, list(snake_position))
    
    
    #if snake_position[0] == pop_position[0] and snake_position[1] == pop_position[1]:
       # score += 100
        #pop_spawn = False
    #else:
        #snake_body.pop()
    
    #if not pop_spawn:
        #time.sleep(20)
    '''
    if snake_position[0] == pop_position[0] and snake_position[1] == pop_position[1]:
        score += 100
        game_window.fill(current[0])
        pop_spawn = False
        pop_position = random_border_position()
        fruit_count += 1
    '''else:
        pop_spawn = True #False'''

    '''if not pop_spawn:
        pygame.draw.rect(game_window, red,
                     pygame.Rect(pop_position[0], pop_position[1], 10, 10))'''
    
    '''if snake_position[0] == pop_position[0] and snake_position[1] == pop_position[1]:
        score += 100
        pop_spawn = False'''
    '''
    game_window.fill(current[0])
    
    for pos in snake_body:
        pygame.draw.rect(game_window, current[1], pygame.Rect(
          pos[0], pos[1], 10, 10))
        '''
    '''pygame.draw.rect(game_window, red, pygame.Rect(
      pop_position[0], pop_position[1], 10, 10))'''
    ##########
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    # displaying score continuously
    show_score(1, white, current[2], 20)
    
    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
