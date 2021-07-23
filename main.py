import pygame, random


# General setup
pygame.init()
pygame.font.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Title and Icon
pygame.display.set_caption("Snake")
snake_icon = pygame.image.load('snake.png')
pygame.display.set_icon(snake_icon)

#Background music
#music by Eugenio Mininni from https://mixkit.co/free-stock-music/
music = pygame.mixer.music.load('backgroundmusic.mp3')
pygame.mixer.music.play(-1)

# Create the screen
size_x = 400
size_y = 400
screen = pygame.display.set_mode((size_x, size_y))



#constants
FPS = 8
blue = (0, 0, 255)
red = (255, 0, 0)
pinkish = (210, 0, 80)
square_size = 20


# creating a grid
def draw_grid():
    size = 400
    RECTSIZE = 20
    row = col = RECTSIZE
    row_width = size // row
    col_width = size // col

    x = y = 0
    for i in range(row):
        x += row_width
        pygame.draw.line(screen, (112,128,144), (x, 0), (x, size))

    for i in range(col):
        y += col_width
        pygame.draw.line(screen, (112,128,144), (0, y), (size, y))

#Restart message
font = pygame.font.SysFont("arial", 15)

def snake(square_size, snake_list):
    for XnY in snake_list:
        pygame.draw.rect(screen, blue, [XnY[0], XnY[1], square_size, square_size])

def restart(text, color, size):
    mytext = font.render(text, True, color)
    screen.blit(mytext, size)


#Game loop
def game_loop():
    go_x = int(size_y / 2)
    go_y = int(size_y / 2)
    lead_x = 0
    lead_y = 0
    change_x = 20
    change_y = 20

    # Apple
    apple_x = round(random.randint(0, size_x - square_size) / 20) * 20
    apple_y = round(random.randint(0, size_y - square_size) / 20) * 20

    snake_list = []
    snake_length = 1

    gameExit = False
    snake_dead = False

    while not gameExit:
        while snake_dead == True:
            screen.fill((244, 213, 246))
            restart("Your score is {}. Press \'R\' to restart or \'Q\' to quit".format(snake_length), pinkish,(85, 150))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    snake_dead = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        snake_dead = False
                    if event.key == pygame.K_r:
                        snake_dead = False
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x = -change_x
                    lead_y = 0
                if event.key == pygame.K_RIGHT:
                    lead_x = change_x
                    lead_y = 0
                if event.key == pygame.K_UP:
                    lead_y = -change_y
                    lead_x = 0
                if event.key == pygame.K_DOWN:
                    lead_y = change_y
                    lead_x = 0

        go_x += lead_x
        go_y += lead_y
        if go_x >= size_x + 2 or go_x <= -2 or go_y >= size_y + 2 or go_y <= -2:
            snake_dead = True

        screen.fill((0, 0, 0))
        draw_grid()


        snake_head = []
        snake_head.append(go_x)
        snake_head.append(go_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for snake_part in snake_list[:-1]:
            if snake_part == snake_head:
                snake_dead = True

        snake(square_size, snake_list)

        apple_img = pygame.image.load("apple.png")
        apple_img.convert()
        screen.blit(apple_img, (apple_x, apple_y))
        #pygame.draw.rect(screen, red, [apple_x, apple_y, square_size, square_size])
        pygame.display.update()
        if go_x == apple_x and go_y == apple_y:
            eating = pygame.mixer.Sound("eatingsound.ogg")
            eating.play()
            apple_x = round(random.randint(0, size_x-square_size) / 20) * 20
            apple_y = round(random.randint(0, size_y-square_size) / 20) * 20
            snake_length += 1

        clock.tick(FPS)



    pygame.quit()
    quit()

game_loop()















