import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Subway Surfers")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 155, 255)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Fonts
font = pygame.font.SysFont("Arial", 40)

# Player
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 10

# Obstacles
obstacle_size = 50
obstacle_speed = 10
obstacles = []

# Score
score = 0


def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_size, player_size))


def draw_obstacles(obstacles):
    for obs in obstacles:
        pygame.draw.rect(screen, RED, (obs[0], obs[1], obstacle_size, obstacle_size))


def update_obstacles(obstacles):
    global score
    for obs in obstacles:
        obs[1] += obstacle_speed
        if obs[1] > HEIGHT:
            obstacles.remove(obs)
            score += 1


def detect_collision(player_x, player_y, obstacles):
    for obs in obstacles:
        if (
            player_x < obs[0] + obstacle_size
            and player_x + player_size > obs[0]
            and player_y < obs[1] + obstacle_size
            and player_y + player_size > obs[1]
        ):
            return True
    return False


# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Generate obstacles
    if random.randint(1, 20) == 1:
        obstacle_x = random.randint(0, WIDTH - obstacle_size)
        obstacles.append([obstacle_x, 0])

    # Update and draw
    draw_player(player_x, player_y)
    draw_obstacles(obstacles)
    update_obstacles(obstacles)

    # Collision detection
    if detect_collision(player_x, player_y, obstacles):
        text = font.render("Game Over!", True, RED)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()










