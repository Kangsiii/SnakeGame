import pygame
import random

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("뱀 게임")

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
fruit_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
fruit_spawn = True

direction = "RIGHT"
change_to = direction

score = 0

clock = pygame.time.Clock()

def game_over():
    font = pygame.font.SysFont("Arial", 30)
    screen.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    global running
    running = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = "LEFT"
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = "DOWN"

    if change_to == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if change_to == "UP" and not direction == "DOWN":
        direction = "UP"
    if change_to == "DOWN" and not direction == "UP":
        direction = "DOWN"

    if direction == "RIGHT":
        snake_pos[0] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
    fruit_spawn = True
    screen.fill((0, 0, 0))

    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > width - 10 or snake_pos[1] < 0 or snake_pos[1] > height - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
