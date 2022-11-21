import pygame
import os

WIDTH, HEIGHT = 900, 500
BALL_SIZE = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
VEL = 15  # Velocity
STRIKER_VEL = 2

BORDER = pygame.Rect(WIDTH / 2 - 2, 0, 4, HEIGHT)
LEFT_GOAL = pygame.Rect(0, HEIGHT // 2 - 60, 20, 120)
RIGHT_GOAL = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 60, 20, 120)

BALL_IMG = pygame.image.load(os.path.join('Assets', 'Ball.png'))
BALL = pygame.transform.scale(BALL_IMG, (30, 30))

SLIDER_IMG = pygame.image.load(os.path.join('Assets', 'Slider.png'))
SLIDER = pygame.transform.scale(SLIDER_IMG, (15, 90))


def draw_window():
    WIN.fill(WHITE)
    # pygame.draw.rect(WIN, BLACK, BORDER)
    # pygame.draw.rect(WIN, BLACK, LEFT_GOAL)
    # pygame.draw.rect(WIN, BLACK, RIGHT_GOAL)
    # WIN.blit(BALL, (ball.x, ball.y))
    WIN.blit(SLIDER, (100, 15))
    WIN.blit(SLIDER, (800, 15))
    pygame.display.update()

#
# def left_movement(keys_pressed, right):
#     if keys_pressed[pygame.K_w] and right.y - VEL > 0:  # up
#         right.y -= VEL
#     if keys_pressed[pygame.K_s] and right.y + VEL + right.height < HEIGHT - 70:  # down
#         right.y += VEL
#     if keys_pressed[pygame.K_a] and right.x - VEL > 0:  # left
#         right.x -= VEL
#     if keys_pressed[pygame.K_d] and right.x + VEL + right.height < BORDER.x:  # right
#         right.x += VEL
#
#
# def right_movement(keys_pressed, left):
#     if keys_pressed[pygame.K_UP] and left.y - VEL > 0:  # up
#         left.y -= VEL
#     if keys_pressed[pygame.K_DOWN] and left.y + VEL + left.height < HEIGHT - 70:  # down
#         left.y += VEL
#     if keys_pressed[pygame.K_LEFT] and left.x - VEL > BORDER.x + BORDER.width:  # left
#         left.x -= VEL
#     if keys_pressed[pygame.K_RIGHT] and left.x + VEL + left.height < WIDTH:  # right
#         left.x += VEL

#
# def moveBall(ball):
#     ball.x += STRIKER_VEL
#     # ball.y += STRIKER_VEL
#
# def stopBall(ball):
#     ball.x -= STRIKER_VEL
# def hit():
#     print("hit")

def main():
    # For movement
    # right = pygame.Rect(800, HEIGHT // 2 - 45 , 90, 15)
    # left = pygame.Rect(100, HEIGHT // 2 - 45, 90, 15)
    # ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30, )

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # keys_pressed = pygame.key.get_pressed()
        # right_movement(keys_pressed, right)
        # left_movement(keys_pressed, left)

        # BR_Up = ball.y
        # BR_Down = ball.y + ball.height
        # R_Up = right.y
        # R_Left = right.x
        # R_Down = right.x + right.height
        # print(R_Up, R_Left, R_Down)
        # if BR_Up > R_Up and BR_Down < R_Down :
        #     print('hit')
        #     stopBall(ball)
        # else :
        #     moveBall(ball)

        # print(right.x,x1)
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
