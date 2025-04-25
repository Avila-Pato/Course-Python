import pygame

pygame.init()
screen = pygame.display.set_mode((720, 420))
clock = pygame.time.Clock()
running = True

# pygame.mouse.set_visible(False)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


mouse_pos = pygame.mouse.get_pos()
x = mouse_pos[0]
y = mouse_pos[1]


pygame.draw.circle(screen, "white", (x, y, 100, 100))


screen.fill("black")

pygame.display.flip()
clock.tick(60)

pygame.quit()