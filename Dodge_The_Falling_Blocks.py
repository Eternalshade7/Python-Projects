import pygame
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

import random

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Enemy Block
block_size = 50
block_x = random.randint(0, WIDTH - block_size)
block_y = -block_size
block_speed = 5

# Power-up
powerup_size = 30
powerup_x = random.randint(0, WIDTH - powerup_size)
powerup_y = -300  # starts off-screen
powerup_speed = 3
powerup_active = True

# Score
score = 0
font = pygame.font.SysFont("comicsans", 30)

# Sounds
try:
    hit_sound = pygame.mixer.Sound("hit.wav")
    powerup_sound = pygame.mixer.Sound("powerup.wav")
except:
    print("⚠️ Sound files missing. Sounds will not play.")
    hit_sound = powerup_sound = None

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Enemy movement
    block_y += block_speed
    if block_y > HEIGHT:
        block_y = -block_size
        block_x = random.randint(0, WIDTH - block_size)
        score += 1
        block_speed += 0.2

    # Power-up movement
    powerup_y += powerup_speed
    if powerup_y > HEIGHT:
        powerup_y = -random.randint(500, 1000)  # re-spawn at random height
        powerup_x = random.randint(0, WIDTH - powerup_size)

    # Collision with block
    if (player_x < block_x + block_size and
        player_x + player_size > block_x and
        player_y < block_y + block_size and
        player_y + player_size > block_y):
        if hit_sound:
            hit_sound.play()
        print("Game Over! Final Score:", score)
        running = False

    # Collision with power-up
    if (player_x < powerup_x + powerup_size and
        player_x + player_size > powerup_x and
        player_y < powerup_y + powerup_size and
        player_y + player_size > powerup_y):
        if powerup_sound:
            powerup_sound.play()
        block_speed = max(block_speed - 2, 2)  # slow down block
        powerup_y = -random.randint(500, 1000)
        powerup_x = random.randint(0, WIDTH - powerup_size)

    # Draw
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (block_x, block_y, block_size, block_size))
    pygame.draw.rect(screen, GREEN, (powerup_x, powerup_y, powerup_size, powerup_size))

    # Score
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()
# This code implements a simple game where the player controls a block that must dodge falling blocks.
# The player can move left and right using the arrow keys, and the objective is to avoid the falling blocks.        
