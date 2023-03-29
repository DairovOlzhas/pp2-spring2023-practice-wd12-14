import pygame
from random import randrange

RES = 800
SIZE = 50

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 60
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
score = 0
speed_count, snake_speed = 0, 10

pygame.init()
window = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()


# TODO add fonts here


def close_game():
    # TODO render game over title
    exit()


while True:
    window.fill(WHITE)
    # drawing snake, apple
    for i, j in snake:
        pygame.draw.rect(window, GREEN, (i, j, SIZE - 1, SIZE - 1))
    pygame.draw.rect(window, RED, (*apple, SIZE, SIZE))

    # show score
    # TODO render score title with score of player

    # snake movement
    speed_count += 1
    if not speed_count % snake_speed:
        x += dx * SIZE
        y += dy * SIZE
        snake.append((x, y))
        snake = snake[-length:]

    # eating food
    if snake[-1] == apple:
        # TODO add eating apple stuff
        pass

    # game over
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        close_game()

    pygame.display.flip()
    clock.tick(fps)

    # controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True}
