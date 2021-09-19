import pygame

pygame.init()

WHITE = pygame.color.Color("white")

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.display.update()
    clock.tick(60)
