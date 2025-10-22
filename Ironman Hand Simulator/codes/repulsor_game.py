import pygame, random, math, os

pygame.init()
W, H = 1000, 650
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Iron Man Repulsor — Targets")
clock = pygame.time.Clock()

# Colors
BG = (8, 10, 18)
TARGET_COLOR = (130, 200, 255)
LASER = (255, 100, 100)
WHITE = (240, 240, 250)

# Sounds
assets = os.path.join(os.path.dirname(__file__), "assets")
pop_path = os.path.join(assets, "pop.wav")
charge_path = os.path.join(assets, "charge.wav")
if os.path.exists(pop_path):
    pop_snd = pygame.mixer.Sound(pop_path)
else:
    pop_snd = None
if os.path.exists(charge_path):
    charge_snd = pygame.mixer.Sound(charge_path)
else:
    charge_snd = None

font = pygame.font.SysFont("arial", 28)

class Target:
    def __init__(self):
        self.r = random.randint(18, 30)
        self.x = random.randint(self.r, W-self.r)
        self.y = random.randint(self.r, H//2)
        self.dy = random.uniform(0.6, 1.6)
        self.ttl = 255

    def update(self):
        self.y += self.dy
        if self.y > H - 80:
            self.y = random.randint(self.r, H//2)
        self.ttl = min(255, self.ttl + 1)

    def draw(self, surf):
        pygame.draw.circle(surf, TARGET_COLOR, (int(self.x), int(self.y)), self.r)

    def hit(self, x, y):
        return (self.x - x)**2 + (self.y - y)**2 <= (self.r+18)**2

targets = [Target() for _ in range(10)]
score = 0
charging = False
beam_timer = 0  # frames beam is visible

def draw_beam(px, py):
    pygame.draw.circle(screen, (40,40,80), (px, py), 60)
    pygame.draw.circle(screen, (255,120,120), (px, py), 22)
    pygame.draw.circle(screen, (255,230,230), (px, py), 10)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
        elif e.type == pygame.MOUSEBUTTONDOWN:
            charging = True
            if charge_snd: charge_snd.play()
        elif e.type == pygame.MOUSEBUTTONUP:
            charging = False
            beam_timer = 6  # show beam briefly
            # detect hits
            px, py = pygame.mouse.get_pos()
            popped = 0
            for t in targets[:]:
                if t.hit(px, py):
                    targets.remove(t)
                    targets.append(Target())
                    popped += 1
            if popped and pop_snd: pop_snd.play()
            score += popped

    screen.fill(BG)

    # draw targets
    for t in targets:
        t.update()
        t.draw(screen)

    # repulsor
    mx, my = pygame.mouse.get_pos()
    if charging or beam_timer > 0:
        draw_beam(mx, my)
        if beam_timer > 0:
            beam_timer -= 1

    # UI
    hud = font.render(f"Score: {score}   Targets: {len(targets)}   Press ESC to quit", True, WHITE)
    screen.blit(hud, (20, H-40))

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
