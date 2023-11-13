import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("블록 깨기 게임")

# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# 패들 설정
paddle_width, paddle_height = 400, 10
paddle_x = (width - paddle_width) // 2
paddle_y = height - paddle_height - 10
paddle_speed = 10

# 공 설정
ball_size = 20
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 5 * random.choice([1, -1])
ball_speed_y = 5

# 블록 설정
block_width, block_height = 80, 30
block_rows = 5
block_cols = 10
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * (block_width + 5), row * (block_height + 5), block_width, block_height)
        blocks.append(block)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 충돌 체크
    if ball_x <= 0 or ball_x >= width - ball_size:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # 패들과 충돌 체크
    if (
        paddle_x < ball_x < paddle_x + paddle_width
        and paddle_y < ball_y < paddle_y + paddle_height
    ):
        ball_speed_y = -ball_speed_y

    # 블록과 충돌 체크
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # 그리기
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, red, (ball_x, ball_y, ball_size, ball_size))

    for block in blocks:
        pygame.draw.rect(screen, blue, block)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
