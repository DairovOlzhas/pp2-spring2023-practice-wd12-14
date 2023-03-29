import pygame

pygame.init()

screen_width = 600
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong")

#Define Game Variables
margin = 50
cpu_score = 0
player_score = 0
fps = 60
winner = 0 #winner is 1 if the player scores a point, -1 if the CPU does
live_ball=False
speed_increase = 0

# Define Colors
bg = (50, 25, 50)
white = (255, 255, 255)
orange = (220, 80, 20)
yellow = (240, 240, 0)


def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen, white, (0, margin), (screen_width, margin))

# PADDLE Class
class Paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 20, 100)
        self.speed = 5

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.speed) #move in place
        if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed) #move in place

    def ai(self):
        #ai to move the paddle automatically
        #move down
        if self.rect.centery < pong_ball.rect.top and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.speed)
        #move up
        if self.rect.centery > pong_ball.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.speed)


    def draw(self, color=white):
        pygame.draw.rect(screen, color, self.rect)


#BALL Class
class Ball():
    def __init__(self, x, y):
        self.reset(x,y)

    def move(self):

        #add collision detection
        #check top margin
        if self.rect.top < margin:
            self.speed_y *= -1
        #check bottom screen
        if self.rect.bottom > screen_height:
            self.speed_y *= -1
        #check collisions with paddles
        if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpu_paddle):
            self.speed_x *= -1
        #check for out of bounds
        if self.rect.left < 0:
            self.winner = 1
        if self.rect.right > screen_width:
            self.winner = -1

        #update ball position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.winner


    def draw(self):
        pygame.draw.circle(screen, orange, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.ball_rad = 10
        self.rect = pygame.Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = -4
        self.speed_y = 4
        self.winner = 0


#Create Paddles
player_paddle = Paddle(screen_width - 40, screen_height // 2)
cpu_paddle = Paddle(20, screen_height // 2)

cpu_paddle2 = Paddle(screen_width - 40, screen_height // 2)


#Create Pong Ball
pong_ball = Ball(screen_width - 60, screen_height // 2 +50)

#Game Loop
run = True

while run:
    draw_board()

    #Draw Paddles
    player_paddle.draw()
    cpu_paddle.draw()
    
    # TODO

    # END_TODO


    if speed_increase > 500:
        speed_increase = 0
        if pong_ball.speed_x < 0:
            pong_ball.speed_x -= 1
        if pong_ball.speed_x > 0:
            pong_ball.speed_x += 1
        if pong_ball.speed_y < 0:
            pong_ball.speed_y -= 1
        if pong_ball.speed_y > 0:
            pong_ball.speed_y += 1
    


    pygame.display.update()


pygame.quit()