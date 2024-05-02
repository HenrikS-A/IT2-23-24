import pygame

# 1. Oppsett (init)
BREDDE = 1280
HOYDE = 720

pygame.init()
vindu = pygame.display.set_mode([BREDDE, HOYDE])
klokke = pygame.time.Clock()

dvd_logo = pygame.image.load("dvd-logo.png")
dvd_logo = pygame.transform.scale_by(dvd_logo, 0.15)

x = 0.000000001
y = 0.000000001
x_fart = 10
y_fart = 10

pygame.display.set_caption("DVD")

spiller = True
# Gameloop, skal kjøre 60 ganger i sekundet (60fps):

while spiller:
    # 2. Håndtere input
    hendelser = pygame.event.get()
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            spiller = False

    # 3. Oppdatere spill
    if x >= BREDDE-150 or x <= 0:
        x_fart *= -1
    if y >= HOYDE-90 or y <= 0:
        y_fart *= -1

    x += x_fart
    y += y_fart

    # 4. Tegne (render)
    vindu.fill([255, 255, 255]) # For hver gang loopen kjører, fyller vi skjermen med hvitt.
    # pygame.draw.circle(vindu, [120, 50, 200], [x, y], 25)
    vindu.blit(dvd_logo, [x, y])

    pygame.display.update()

    klokke.tick(60)









    # Smilefjes!
    # pygame.draw.circle(vindu, [120, 50, 200], [260, 200], 25)
    # pygame.draw.circle(vindu, [120, 50, 200], [340, 200], 25)

    # pygame.draw.circle(vindu, [120, 50, 200], [260, 300], 15)
    # pygame.draw.circle(vindu, [120, 50, 200], [340, 300], 15)
    # pygame.draw.circle(vindu, [120, 50, 200], [300, 310], 15)
    # pygame.draw.circle(vindu, [120, 50, 200], [220, 280], 15)
    # pygame.draw.circle(vindu, [120, 50, 200], [380, 280], 15)