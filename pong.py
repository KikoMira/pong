import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [5, 5]
left_paddle_pos = [10, HEIGHT // 2 - PADDLE_HEIGHT // 2]
right_paddle_pos = [WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2]
paddle_vel = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_pos[1] > 0:
        left_paddle_pos[1] -= paddle_vel
    if keys[pygame.K_s] and left_paddle_pos[1] < HEIGHT - PADDLE_HEIGHT:
        left_paddle_pos[1] += paddle_vel
    if keys[pygame.K_UP] and right_paddle_pos[1] > 0:
        right_paddle_pos[1] -= paddle_vel
    if keys[pygame.K_DOWN] and right_paddle_pos[1] < HEIGHT - PADDLE_HEIGHT:
        right_paddle_pos[1] += paddle_vel

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if (
        ball_pos[0] <= left_paddle_pos[0] + PADDLE_WIDTH
        and left_paddle_pos[1] < ball_pos[1] < left_paddle_pos[1] + PADDLE_HEIGHT
    ) or (
        ball_pos[0] >= right_paddle_pos[0] - BALL_SIZE
        and right_paddle_pos[1] < ball_pos[1] < right_paddle_pos[1] + PADDLE_HEIGHT
    ):
        ball_vel[0] = -ball_vel[0]

    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - BALL_SIZE:
        ball_vel[1] = -ball_vel[1]

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, WHITE, pygame.Rect(left_paddle_pos, (PADDLE_WIDTH, PADDLE_HEIGHT)))
    pygame.draw.rect(screen, WHITE, pygame.Rect(right_paddle_pos, (PADDLE_WIDTH, PADDLE_HEIGHT)))
    pygame.draw.ellipse(screen, WHITE, pygame.Rect(ball_pos, (BALL_SIZE, BALL_SIZE)))

    pygame.display.flip()

    clock.tick(FPS)
