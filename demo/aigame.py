import pgzrun
import random

# Constants
WIDTH = 800
HEIGHT = 400
ALIEN_Y = HEIGHT - 80

# Actors
alien = Actor('p3_stand', (100, ALIEN_Y))
cactus = Actor('cactus', (WIDTH, HEIGHT - 80))

# Variables
alien.gravity = 1
alien.jump_strength = -15
alien.vy = 0
game_over = False
score = 0

def update():
    global game_over, score

    if not game_over:
        update_alien()
        update_cactus()
        check_collision()

def update_alien():
    alien.vy += alien.gravity
    alien.y += alien.vy

    if alien.y > ALIEN_Y:
        alien.y = ALIEN_Y
        alien.vy = 0

def update_cactus():
    global score
    cactus.x -= 4

    if cactus.x < 0:
        cactus.x = WIDTH
        score += 1

def check_collision():
    global game_over
    if alien.colliderect(cactus):
        game_over = True

def on_key_down(key):
    if key == keys.SPACE and alien.y == ALIEN_Y:
        alien.vy = alien.jump_strength

def draw():
    screen.clear()
    screen.draw.text(f'Score: {score}', (10, 10), fontsize=30, color="white")
    alien.draw()
    cactus.draw()

    if game_over:
        screen.draw.text('GAME OVER', (WIDTH // 2 - 100, HEIGHT // 2), fontsize=60, color="red")

pgzrun.go()
