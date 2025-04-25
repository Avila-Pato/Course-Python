import random
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 420))
clock = pygame.time.Clock()
running = True

# Coordenadas del cuadrado y velocidad (fuera del loop)
card_y = 130
card_x = 0
card_size = 50
speed_y = 5

coor_list = []

for i in  range(60):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    coor_list.append([x, y])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")


    for coord in coor_list:
        x = coord[0]
        y = coord[1]
        pygame.draw.circle(screen, "white", (x, y), 2)
        coord[1] += 1 ## animación
        if coord[1] > 600: ## bucle de animación
            coord[1] = 0

    # Actualiza la posición vertical
    card_x += speed_y
    if card_x > 720 - card_size or card_x < 0:
        speed_y *= -1

    # Dibuja las filas de cuadrados
    for x in range(0, 750, 100):
        pygame.draw.rect(screen, "green", pygame.Rect(card_x, card_y, card_size, card_size))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
