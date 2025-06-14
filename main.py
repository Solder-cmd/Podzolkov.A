import pygame
from platform import *
from ball import *
from enemy import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

FPS = 60

coins = []
enemies = list()
for x in range(45, screen.get_width() - 50, 55):
    for y in range(50, 151, 50):
        enemies.append(Enemy(x, y))

platform = Platform(1280/2, 720 - 100)
ball = Ball((1280/2, 500))

font = pygame.font.SysFont(None, 48)
big_font = pygame.font.SysFont(None, 72)

# 🆕 ДОБАВЛЕНЫ НОВЫЕ ПЕРЕМЕННЫЕ
score = 0
lives = 3
game_over = False
win = False
ball_lost = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    if not game_over:
        platform.move(screen)
        platform.draw(screen)

        for enemy in enemies[:]:
            enemy.draw(screen)
            if enemy.check_collision(ball):
                ball.reflect(enemy)
                if enemy.health <= 0:
                    coins.append(Coin(enemy.rect.centerx, enemy.rect.centery))
                    enemies.remove(enemy)
                    score += 100  # 🆕 очки за врага

        for coin in coins[:]:
            coin.update()
            coin.draw(screen)
            # 🆕 Сбор монет
            if coin.rect.colliderect(platform.rect):
                score += 10
                coins.remove(coin)

        ball.draw(screen)

        if not ball_lost:
            ball.move(screen, platform)

        # 🆕 Проверка на потерю мяча
        if ball.rect.bottom > screen.get_height():
            lives -= 1
            if lives > 0:
                # сброс мяча
                ball = Ball((1280/2, 500))
                ball_lost = True
            else:
                game_over = True
                win = False

        # Перезапуск мяча, если он был потерян, и кликнули мышкой
        if ball_lost and pygame.mouse.get_pressed()[0]:
            ball_lost = False

        # Победа
        if not enemies:
            game_over = True
            win = True

        # 🆕 Отображение счёта и жизней
        score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
        lives_text = font.render(f"Жизни: {lives}", True, (255, 255, 255))
        screen.blit(score_text, (20, 10))
        screen.blit(lives_text, (20, 50))

    else:
        # Сообщение о победе/поражении
        if win:
            text = big_font.render("Виграв!", True, (255, 255, 255))
        else:
            text = big_font.render("Програв!", True, (255, 0, 0))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2,
                           screen.get_height() // 2 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
