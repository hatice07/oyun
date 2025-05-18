import pygame
import random
import sys

WIDTH = 500
HEIGHT = 600

WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
ROAD_BORDER = (30, 30, 30)
LINE_COLOR = (200, 200, 200)
RED = (200, 50, 50)
BLUE = (50, 100, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 100, 0)
BROWN = (139, 69, 19)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Araba Yarisi")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24)
big_font = pygame.font.SysFont("arial", 48, bold=True)

center_lines = [i for i in range(-100, HEIGHT, 100)]
tree_positions = [i for i in range(0, HEIGHT, 120)]

def draw_car(color1, color2):
    car = pygame.Surface((60, 120), pygame.SRCALPHA)
    pygame.draw.rect(car, color1, (0, 0, 60, 120), border_radius=15)
    pygame.draw.rect(car, color2, (15, 20, 30, 70), border_radius=10)
    pygame.draw.circle(car, BLACK, (15, 110), 8)
    pygame.draw.circle(car, BLACK, (45, 110), 8)
    pygame.draw.rect(car, WHITE, (10, 5, 15, 10)) 
    pygame.draw.rect(car, WHITE, (35, 5, 15, 10))
    return car

def draw_hearts(surface, x, y, hearts):
    for i in range(hearts):
        heart_x = x + i * 35
        pygame.draw.circle(surface, RED, (heart_x + 5, y + 5), 6)
        pygame.draw.circle(surface, RED, (heart_x + 15, y + 5), 6)
        pygame.draw.polygon(surface, RED, [(heart_x, y + 8), (heart_x + 10, y + 20), (heart_x + 20, y + 8)])


player_img = draw_car(BLUE, WHITE)
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT - 140))

enemy_colors = [(RED, YELLOW), (GREEN, WHITE), (YELLOW, BLACK), (WHITE, RED)]
enemy_imgs = [draw_car(body, stripe) for body, stripe in enemy_colors]
enemy_list = []

score = 0
level = 1
enemy_speed = 6
spawn_timer = 0
game_over = False
health = 3
level_up_timer = 0
level_up_display = False

def spawn_enemy():
    x_positions = [90, 190, 290, 390]
    x = random.choice(x_positions)
    img = random.choice(enemy_imgs)
    rect = img.get_rect(topleft=(x, -120))
    enemy_list.append((img, rect))

running = True
while running:
    clock.tick(60)
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 60:
            player_rect.x -= 6
        if keys[pygame.K_RIGHT] and player_rect.right < WIDTH - 60:
            player_rect.x += 6

        for i in range(len(center_lines)):
            center_lines[i] += enemy_speed
            pygame.draw.rect(screen, LINE_COLOR, (WIDTH // 2 - 5, center_lines[i], 10, 50), border_radius=3)
            if center_lines[i] > HEIGHT:
                center_lines[i] = -100

        for i in range(len(tree_positions)):
            tree_positions[i] += enemy_speed
            
            pygame.draw.rect(screen, BROWN, (20, tree_positions[i], 10, 20))
            pygame.draw.circle(screen, DARK_GREEN, (25, tree_positions[i] - 10), 15)
           
            pygame.draw.rect(screen, BROWN, (WIDTH - 30, tree_positions[i], 10, 20))
            pygame.draw.circle(screen, DARK_GREEN, (WIDTH - 25, tree_positions[i] - 10), 15)
            if tree_positions[i] > HEIGHT:
                tree_positions[i] = -60

        pygame.draw.rect(screen, ROAD_BORDER, (50, 0, 10, HEIGHT))
        pygame.draw.rect(screen, ROAD_BORDER, (WIDTH - 60, 0, 10, HEIGHT))

        spawn_timer += 1
        if spawn_timer > 50:
            spawn_enemy()
            spawn_timer = 0

        for enemy_img, enemy_rect in enemy_list[:]:
            enemy_rect.y += enemy_speed
            screen.blit(enemy_img, enemy_rect)

            if enemy_rect.colliderect(player_rect):
                enemy_list.remove((enemy_img, enemy_rect))
                health -= 1
                if health <= 0:
                    game_over = True
                    game_over_level = level

            if enemy_rect.top > HEIGHT:
                enemy_list.remove((enemy_img, enemy_rect))
                score += 1

                if score % 10 == 0:
                    level += 1
                    enemy_speed += 1
                    level_up_display = True
                    level_up_timer = pygame.time.get_ticks()

        screen.blit(player_img, player_rect)

        score_text = font.render(f"Skor: {score}", True, WHITE)
        level_text = font.render(f"Seviye: {level}", True, YELLOW)
        screen.blit(score_text, (WIDTH - 150, 10))
        screen.blit(level_text, (WIDTH - 150, 40))
        draw_hearts(screen, 20, 10, health)

        if level_up_display:
            elapsed = pygame.time.get_ticks() - level_up_timer
            if elapsed < 2000:
                level_announce = big_font.render(f"SEVİYE {level}", True, YELLOW)
                screen.blit(level_announce, (WIDTH // 2 - level_announce.get_width() // 2, HEIGHT // 2 - 100))
            else:
                level_up_display = False

    else:
        over_text = big_font.render("OYUN BİTTİ!", True, RED)
        score_text = font.render(f"Skorun: {score}", True, WHITE)
        level_text = font.render(f"Seviye: {game_over_level}", True, YELLOW)
        info_text = font.render("Çıkmak için ESC'ye bas", True, WHITE)

        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 100))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 40))
        screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, HEIGHT // 2))
        screen.blit(info_text, (WIDTH // 2 - info_text.get_width() // 2, HEIGHT // 2 + 50))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()