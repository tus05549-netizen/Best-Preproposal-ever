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

# What mode?
mode = input("Do you want to play one or two player? ").lower().strip()
two_snakes = mode in ["two", "2", "t"]

if two_snakes:
    snake2_position = [window_x - 100, window_y - 50]
    snake2_body = [
        [window_x - 100, window_y - 50],
        [window_x - 90, window_y - 50],
        [window_x - 80, window_y - 50],
        [window_x - 70, window_y - 50]
    ]
    direction2 = 'LEFT'
    change_to2 = direction2
# Alive Flags
snake_alive = True
snake2_alive = True
winner_text = ""
'''# Window size
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
        window_size = input("Please enter small, medium, or large! ")'''
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
orange = pygame.Color(255, 165, 0)
yellow = pygame.Color(255, 255, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
grey = pygame.Color(147, 147, 147)
lime = pygame.Color(141, 182, 0)
maroon = pygame.Color(128, 0, 0)
pink = pygame.Color(255, 105, 180)
purple = pygame.Color(191, 0, 255)
cerulean = pygame.Color(135, 206, 250)
navy = pygame.Color(25, 25, 112)
coral = pygame.Color(255, 127, 80)
brown = pygame.Color(111, 78, 55)
# color schemes
dark = [black, green, 'impact', coral]
light = [grey, orange, 'calibri', cerulean]
classic = [lime, blue, 'bookantiqua', pink]
neon = [pink, purple, 'bauhaus93', yellow]
sky = [cerulean, black, 'comicsansms', orange]
futuristic = [coral, navy, 'ocraextended', brown]
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
direction = 'RIGHT' #############
change_to = direction
# initial score
score1 = 0
score2 = 0

fruit_count = 0

# setting second snake direction
# towards left



# displaying Score function
def show_score(choice, color, font, size):
  
    # creating font object score_font 
    score_font = pygame.font.SysFont(font, size)
    '''if two_snakes:
        score_surface = score_font.render(f"P1: {score1}   P2: {score2}", True, color)#('Score : ' + str(score1), True, color)
    else:
        score_surface = score_font.render('Score : ' + str(score1), True, color)'''
    # Player 1 score (snake color)
    p1_surface = score_font.render(f"Player 1: {score1}", True, current[1])
    p1_rect = p1_surface.get_rect(topleft=(10, 10))
    game_window.blit(p1_surface, p1_rect)
    
    # create the display surface object
    # score_surface
    if two_snakes:
        p2_surface = score_font.render(f"Player 2: {score2}", True, current[3])
        p2_rect = p2_surface.get_rect(topright=(window_x - 10, 10))
        game_window.blit(p2_surface, p2_rect)
    '''if two_snakes:
        score_surface = score_font.render(f"P1: {score1}   P2: {score2}", True, color)#('Score : ' + str(score1), True, color)
    else:
        score_surface = score_font.render('Score : ' + str(score1), True, color)'''
    # create a rectangular object for the 
    # text surface object
    #score_rect = score_surface.get_rect()
    
    # displaying text
   # game_window.blit(score_surface, score_rect)
    
# game over function
def game_over():
    global snake_alive, snake2_alive
    global snake_position, snake_body, direction, change_to
    global snake2_position, snake2_body, direction2, change_to2
    global fruit_position, fruit_spawn, score1, fruit_count
    global pop_position, pop_spawn
    global winner_text
    global score1
    global score2
    # creating font object my_font
    if window_x == 840:
        my_font = pygame.font.SysFont(current[2], 40)
    else:
        my_font = pygame.font.SysFont(current[2], 32)
    
    # creating a text surface on which text 
    # will be drawn
    if two_snakes:
        game_over_surface = my_font.render(f"{winner_text}  P1: {score1}  P2: {score2}", True, maroon)
    else:
        game_over_surface = my_font.render('Your Score is : ' + str(score1), True, maroon)
    
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # after pressing enter we will quit the program
    # "Press ENTER to exit" text
    if window_x <= 600:
        restart_surface = my_font.render('Press R to restart', True, white)
        restart_rect = restart_surface.get_rect(center=(window_x/2, -20 + window_y/2))

        exit_surface = my_font.render('or ENTER to exit', True, white)
        exit_rect = exit_surface.get_rect(center=(window_x/2, 20 + window_y/2))
    else:
        next_surface = my_font.render('Press R to restart or ENTER to exit', True, white)
        next_rect = next_surface.get_rect(center=(window_x/2, -20 + window_y/2))
    waiting = True
    while waiting:
        game_window.fill(current[0])
        game_window.blit(game_over_surface, game_over_rect)
        if window_x <= 600:
            game_window.blit(restart_surface, restart_rect)
            game_window.blit(exit_surface, exit_rect)
        else:
            game_window.blit(next_surface, next_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_r:
                    # RESET GAME VARIABLES ONLY
                    snake_alive = True
                    if two_snakes:
                        snake2_alive = True
                    snake_position = [100, 50]
                    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
                    direction = 'RIGHT'
                    change_to = 'RIGHT'
                    if two_snakes:
                        snake2_position = [window_x - 100, window_y - 50]
                        snake2_body = [
                                [window_x - 100, window_y - 50],
                                [window_x - 90, window_y - 50],
                                [window_x - 80, window_y - 50],
                                [window_x - 70, window_y - 50]
                                ]

                        '''snake2_body = [
                                        [300, 50],
                                       [290, 50],
                                       [280, 50],
                                       [270, 50]
                                       ]'''
                        direction2 = 'LEFT'
                        change_to2 = 'LEFT'

                    fruit_position = [random.randrange(1, (window_x//10)) * 10,
                                      random.randrange(1, (window_y//10)) * 10]
                    fruit_spawn = True

                    pop_position = random_border_position()
                    pop_spawn = False

                    score1 = 0
                    score2 = 0
                    fruit_count = 0

                    # Return to main loop
                    return
                else:
                    print("Press R to restart or ENTER to exit!")
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    '''time.sleep(2)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()'''
# two-player ending screen
#def game_over_two_player(winner, score1, score2):
    

#starting screen
if window_x == 360:
    start_font = pygame.font.SysFont(current[2], 30)
else:
    start_font = pygame.font.SysFont(current[2], 40)

waiting = True
while waiting:
    game_window.fill(current[0])

    text_surface = start_font.render("Press SPACE to start", True, white)
    text_rect = text_surface.get_rect(center=(window_x//2, window_y//2))
    game_window.blit(text_surface, text_rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                waiting = False
        if event.type == pygame.QUIT:
            pygame.quit()
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
    # key events for second snake
            if two_snakes:
                if event.key == pygame.K_w:
                    change_to2 = 'UP'
                if event.key == pygame.K_s:
                    change_to2 = 'DOWN'
                if event.key == pygame.K_a:
                    change_to2 = 'LEFT'
                if event.key == pygame.K_d:
                    change_to2 = 'RIGHT'

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
    # second snake 
    if two_snakes:
        if change_to2 == 'UP' and direction2 != 'DOWN':
            direction2 = 'UP'
        if change_to2 == 'DOWN' and direction2 != 'UP':
            direction2 = 'DOWN'
        if change_to2 == 'LEFT' and direction2 != 'RIGHT':
            direction2 = 'LEFT'
        if change_to2 == 'RIGHT' and direction2 != 'LEFT':
            direction2 = 'RIGHT'

    # Moving the snake
    if snake_alive:
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10
    # move second snake
    if two_snakes and snake2_alive :
        if direction2 == 'UP':
            snake2_position[1] -= 10
        if direction2 == 'DOWN':
            snake2_position[1] += 10
        if direction2 == 'LEFT':
            snake2_position[0] -= 10
        if direction2 == 'RIGHT':
            snake2_position[0] += 10

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
    if snake_alive:
        snake_body.insert(0, list(snake_position))
    if snake_alive:
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1] and fruit_spawn:
            score1 += 10
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
     # second snake fruit collision
    if two_snakes and snake2_alive:
        snake2_body.insert(0, list(snake2_position))

        if snake2_position[0] == fruit_position[0] and snake2_position[1] == fruit_position[1]:
            fruit_spawn = False
            score2 += 10
        else:
            snake2_body.pop()
        
    pygame.draw.rect(game_window, white, pygame.Rect(
      fruit_position[0], fruit_position[1], 10, 10))
    
   

# Clear screen ONCE
    #game_window.fill(current[0])

# Draw snake
    if snake_alive:
        for pos in snake_body:
            pygame.draw.rect(game_window, current[1],
                         pygame.Rect(pos[0], pos[1], 10, 10))
    if two_snakes and snake2_alive:
        for pos in snake2_body:
            pygame.draw.rect(game_window, current[3], pygame.Rect(pos[0], pos[1], 10, 10))


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
        score1 += 100
        game_window.fill(current[0])
        pop_spawn = False
        pop_position = random_border_position()
        fruit_count += 1
        
    if two_snakes and snake2_alive:
        if snake2_position[0] == pop_position[0] and snake2_position[1] == pop_position[1]:
            score2 += 100
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
       snake_alive = False # game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        snake_alive = False #game_over()
    # snake 2 game over
    if two_snakes:
        if snake2_position[0] < 0 or snake2_position[0] > window_x-10:
            snake2_alive = False #game_over()
        if snake2_position[1] < 0 or snake2_position[1] > window_y-10:
            snake2_alive = False #game_over()
    
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            snake_alive = False #game_over()
    # snake 2 Touching the snake body
    if two_snakes and snake2_alive:
        for block in snake2_body[1:]:
            if snake2_position == block:
                snake2_alive = False # game_over()
    
    # snake 1 hits snake 2
    if two_snakes and snake_alive and snake2_alive:
        if snake_position == snake2_position:
            snake_alive = False
            snake2_alive = False
    if two_snakes and snake_alive and snake2_alive:
        for block in snake2_body:
            if snake_position == block:
                snake_alive = False
    if two_snakes and snake2_alive and snake_alive:
        for block in snake_body:
            if snake2_position == block:
                snake2_alive = False #game_over()
    if not two_snakes:
        if not snake_alive:  
            game_over()
    else:
        if not snake_alive and not snake2_alive:
            if score1 > score2:
                winner_text = "Player 1 wins!"
            elif score2 > score1:
                winner_text  = "Player 2 wins!"
            else:
                winner_text ="Tie!"
            game_over()
    
    
    # displaying score continuously
    show_score(1, white, current[2], 20)
    
    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
