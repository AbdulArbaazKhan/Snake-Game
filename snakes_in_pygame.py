import os
import random
import pygame

pygame.init()
font = pygame.font.SysFont(None, 55)


def screen_text(text, color, x, y):
    text_display = font.render(text, True, color)
    window.blit(text_display, [x, y])


def plot(area, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(area, color, [x, y, snake_size, snake_size])


window_width = 900
window_height = 600
# creating window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("SnakesWithArbaz")
# game specific variables
# game colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
pygame.mixer.init()
pygame.mixer_music.load("resources/So_Long_Analog.mp3")


def home_screen():
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer_music.play()
                    gameLoop()

                if event.key == pygame.K_ESCAPE:
                    game_over = True
        window.fill((30, 67, 82))
        screen_text("Welcome To Snakes", (34, 83, 86), 270, 250)
        screen_text("Press Spacebar To Play", (34, 83, 86), 270, 300)
        pygame.display.update()


def gameLoop():
    snake_x = 40
    snake_y = 50
    size = 10
    block_size = 8
    velocity_x = 0
    velocity_y = 0
    snake_initial_velcity = 4
    foodx = random.randint(20, window_width / 2)
    foody = random.randint(20, window_height / 2)
    score = 0
    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as create:
            create.write("30")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    # creating snakr update after eating food
    snk_length = 1
    snk_list = []
    game_over = False
    clock = pygame.time.Clock()
    fps = 60
    game_exit = False
    # creating game loop
    colors = ((108, 214, 255), (230, 255, 101), (143, 72, 189), (72, 199, 67), (255, 171, 98), green, white)
    random_colors = random.choice(colors)
    random_colors2 = random.choice(colors)
    if random_colors == random_colors2:
        for i in range(0, 1):
            random_colors2 = random.choice(colors)
            i += 1
    if random_colors2 == random_colors:
        for i in range(0, 1):
            random_colors = random.choice(colors)
            i += 1
    while not game_exit:
        if game_over:
            window.fill(random_colors2)
            screen_text("Game Over Press Enter to Continue", (23, 67, 200), 150, 270)
            screen_text(f"Score: {score}", (23, 67, 200), 150, 306)
            pygame.mixer_music.stop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_exit = True
                        home_screen()
                    if event.key == pygame.K_ESCAPE:
                        game_exit = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_exit = True
                    if event.key == pygame.K_RIGHT:
                        velocity_x = snake_initial_velcity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -snake_initial_velcity
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = snake_initial_velcity
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -snake_initial_velcity
                        velocity_x = 0
                    if event.key == pygame.K_EQUALS:
                        snake_initial_velcity += 2
                    if event.key == pygame.K_MINUS:
                        snake_initial_velcity-=2
            snake_x += velocity_x
            snake_y += velocity_y
            window.fill(random_colors)
            # pygame.draw.rect(window, green, [snake_x, snake_y, size, size])
            plot(window, random_colors2, snk_list, size)
            pygame.draw.rect(window, black, [foodx, foody, block_size, block_size])
            if abs(snake_x - foodx) < 6 and abs(snake_y - foody) < 6:
                score += 10
                foodx = random.randint(20, window_width / 2)
                foody = random.randint(20, window_height / 2)
                snk_length += 5
                if score > int(hiscore):
                    with open("hiscore.txt", "w") as f:
                        hiscore = f.write(str(score))
                    hiscore = score
            screen_text(
                'Score: ' + str(score) + "                                                  Hiscore: " + str(hiscore),
                random_colors2, 5, 5)
            head = [snake_x, snake_y]
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]
            if snake_x < 0 or snake_x > 900 or snake_y < 0 or snake_y > 600:
                game_over = True
            if head in snk_list[:-1]:
                game_over = True
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


home_screen()
