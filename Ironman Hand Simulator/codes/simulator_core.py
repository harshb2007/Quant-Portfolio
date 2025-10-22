import pygame

pygame.init()
W, H = 960, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.display.set_caption("Iron Man Repulsor — Core Demo")

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill((6, 6, 12))
    x, y = pygame.mouse.get_pos()
    # glow
    pygame.draw.circle(screen, (40, 40, 80), (x, y), 50)
    # repulsor
    pygame.draw.circle(screen, (255, 80, 80), (x, y), 24)
    pygame.draw.circle(screen, (255, 200, 200), (x, y), 12)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
