import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
f = True
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos3 = pygame.Vector2(screen.get_width() / 2 + 30, screen.get_height() / 2 - 30)
player_pos4 = pygame.Vector2(screen.get_width() / 2 - 30, screen.get_height() / 2 - 30)
hight = screen.get_height()
width = screen.get_width()
while running:
    screen.fill("#09182b")
    for i in range(100):
        screen.fill(pygame.Color('white'),
                    (random.random() * width, random.random() * hight, 1, 150))
    pygame.draw.circle(screen, "#ddeeff", player_pos, 120)
    pygame.draw.circle(screen, "#8db3d9", player_pos2, 100)
    if f:
        pygame.draw.circle(screen, "#002238", player_pos3, 20)
        pygame.draw.circle(screen, "#002238", player_pos4, 20)
    elif not f:
        pygame.draw.rect(screen, "#002238", (player_pos4.x + 43, player_pos4.y - 10, 20 + 20, 20), 0)
        pygame.draw.rect(screen, "#002238", (player_pos4.x - 23, player_pos4.y - 10, 20 + 20, 20), 0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        f = True
        if player_pos.x < 1155:
            player_pos2.x += 290 * dt
            player_pos3.x += 280 * dt
            player_pos4.x += 280 * dt
            player_pos.x += 300 * dt
    if keys[pygame.K_a]:
        f = True
        if player_pos.x > 125:
            player_pos2.x -= 290 * dt
            player_pos3.x -= 280 * dt
            player_pos4.x -= 280 * dt
            player_pos.x -= 300 * dt
    if keys[pygame.K_w]:
        f = False
        if player_pos.y < 600:
            player_pos2.y -= 290 * dt
            player_pos3.y -= 280 * dt
            player_pos4.y -= 280 * dt
            player_pos.y -= 300 * dt
            # player_pos5.y -= 280 * dt
    if keys[pygame.K_s]:
        f = False
        if player_pos.y > 20:
            player_pos2.y += 290 * dt
            player_pos3.y += 280 * dt
            player_pos4.y += 280 * dt
            player_pos.y += 300 * dt
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            py_x = pygame.mouse.get_pos()
            if py_x[0] > (player_pos.x - 30 and py_x[0] < (player_pos.x + 30)):
                print('peijfpwief')


    # fill the screen with a color to wipe away anything from last frame

    pygame.time.delay(20)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(120) / 1000