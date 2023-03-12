import pygame
import random

# Initialize Pygame
pygame.init()

FPS = 60
DELAY = 20

# Set up the screen
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define game variables
BALL_SIZE = 20
BALL_COLOR = BLUE
BALL_SPEED = 5
ball_rect = pygame.Rect(WIDTH//2-BALL_SIZE//2, HEIGHT//2-BALL_SIZE//2,
                        BALL_SIZE, BALL_SIZE)
dx = random.choice([-BALL_SPEED, BALL_SPEED])
dy = -BALL_SPEED

PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
PADDLE_COLOR = RED
PADDLE_SPEED = 10
paddle_rect = pygame.Rect(WIDTH//2-PADDLE_WIDTH//2, HEIGHT-PADDLE_HEIGHT-10,
                          PADDLE_WIDTH, PADDLE_HEIGHT)

BLOCK_WIDTH = 50
BLOCK_HEIGHT = 20
BLOCK_COLOR = WHITE
BLOCK_ROWS = 5
BLOCK_COLS = 10
blocks = []
for row in range(BLOCK_ROWS):
    block_row = []
    for col in range(BLOCK_COLS):
        block_rect = pygame.Rect(col*BLOCK_WIDTH, row*BLOCK_HEIGHT+50,
                                 BLOCK_WIDTH, BLOCK_HEIGHT)
        block_row.append(block_rect)
    blocks.append(block_row)


# Define game functions
def draw_ball():
    pygame.draw.ellipse(screen, BALL_COLOR, ball_rect)


def draw_paddle():
    pygame.draw.rect(screen, PADDLE_COLOR, paddle_rect)


def draw_blocks():
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLS):
            block_rect = blocks[row][col]
            if block_rect:
                pygame.draw.rect(screen, BLOCK_COLOR, block_rect)


def move_ball():
    global ball_rect, dx, dy
    ball_rect.x += dx
    ball_rect.y += dy

    # Bounce off walls
    if ball_rect.left < 0 or ball_rect.right > WIDTH:
        dx = -dx
    if ball_rect.top < 0:
        dy = -dy

    # Check for collision with paddle
    if ball_rect.colliderect(paddle_rect):
        dy = -dy

    # Check for collision with blocks
    for row in range(BLOCK_ROWS):
        for col in range(BLOCK_COLS):
            block_rect = blocks[row][col]
            if block_rect and ball_rect.colliderect(block_rect):
                blocks[row][col] = None
                dy = -dy

    # Check if ball goes off screen
    if ball_rect.top > HEIGHT:
        reset_game()


def move_paddle():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_rect.left > 0:
        paddle_rect.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle_rect.right < WIDTH:
        paddle_rect.x += PADDLE_SPEED


def reset_game():
    global ball_rect, dx, dy, blocks
    ball_rect = pygame.Rect(WIDTH//2-BALL_SIZE//2, HEIGHT//2-BALL_SIZE//2,
                            BALL_SIZE, BALL_SIZE)
    dx = random.choice([-BALL_SPEED, BALL_SPEED])
    dy = -BALL_SPEED
    blocks = []
    for row in range(BLOCK_ROWS):
        block_row = []
        for col in range(BLOCK_COLS):
            block_rect = pygame.Rect(col*BLOCK_WIDTH, row*BLOCK_HEIGHT+50,
                                     BLOCK_WIDTH, BLOCK_HEIGHT)
            block_row.append(block_rect)
        blocks.append(block_row)


# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Game logic
    move_ball()
    move_paddle()
    # Draw graphics
    screen.fill(BLACK)
    draw_ball()
    draw_paddle()
    draw_blocks()
    pygame.display.update()
    pygame.time.delay(DELAY)

# Quit Pygame
pygame.quit()
