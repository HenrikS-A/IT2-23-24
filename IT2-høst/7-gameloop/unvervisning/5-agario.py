import pygame
import random
import math


# 1. Oppsett
pygame.init()

BREDDE = 1280
HOYDE = 720
vindu = pygame.display.set_mode((BREDDE, HOYDE))

FPS = 60
klokke = pygame.time.Clock()

pygame.display.set_caption("AGARIO") # Navn på vinduet

font = pygame.font.SysFont("Open Sans", 24) # Skrifttype
font_overskrift = pygame.font.SysFont("Open Sans", 60)

## Startverdier
spiller_x = 300
spiller_y = 600
spiller_radius = 40

matbit1_x = 200
matbit1_y = 200
matbit1_radius = 10

matbit2_x = 600
matbit2_y = 300
matbit2_radius = 10

matbit3_x = 850
matbit3_y = 450
matbit3_radius = 10


while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    mus_x, mus_y = pygame.mouse.get_pos()

    # 3. Oppdater spill
    spiller_rektangel = pygame.Rect(spiller_x - spiller_radius, spiller_y - spiller_radius, spiller_radius*2, spiller_radius*2)
    
    matbit1_rektangel = pygame.Rect(matbit1_x - matbit1_radius, matbit1_y - matbit1_radius, matbit1_radius*2, matbit1_radius*2)
    if spiller_rektangel.colliderect(matbit1_rektangel):
        matbit1_x = random.randint(0, BREDDE)
        matbit1_y = random.randint(0, HOYDE)

        spiller_radius += 5
    
    matbit2_rektangel = pygame.Rect(matbit2_x - matbit2_radius, matbit2_y - matbit2_radius, matbit2_radius*2, matbit2_radius*2)
    if spiller_rektangel.colliderect(matbit2_rektangel):
        matbit2_x = random.randint(0, BREDDE)
        matbit2_y = random.randint(0, HOYDE)

        spiller_radius += 5

    matbit3_rektangel = pygame.Rect(matbit3_x - matbit3_radius, matbit3_y - matbit3_radius, matbit3_radius*2, matbit3_radius*2)
    if spiller_rektangel.colliderect(matbit3_rektangel):
        matbit3_x = random.randint(0, BREDDE)
        matbit3_y = random.randint(0, HOYDE)

        spiller_radius += 5


    # pygame.sprite.collide_circle()
    # pygame.



    ## Bevegelsesmekanikk
    dx = mus_x-spiller_x
    dy = mus_y-spiller_y

    vinkel = math.atan(dy/dx)   # finner vinkel med den inverse av tangens

    # Enhetssirkelen
    x_vekst = math.cos(vinkel)
    y_vekst = math.sin(vinkel)

    # gjør at spilleren beveger seg raskere når musen er lengre unna
    vektorlengde = math.sqrt(dx**2 + dy**2)

    if 100 < vektorlengde < 300:
        x_vekst *= vektorlengde * 0.01
        y_vekst *= vektorlengde * 0.01
    elif vektorlengde > 300:
        x_vekst *= 3    # Makshastighet er 3 ganger vanlig fart
        y_vekst *= 3


    if dx != 0 and dy != 0:
        if dx < -1:
            spiller_x -= x_vekst
            spiller_y -= y_vekst
        elif dx > 1:
            spiller_x += x_vekst
            spiller_y += y_vekst



    # 4. Tegn
    vindu.fill("white") # Fyller vinduet med hvit bakgrunn, for hver gang loopen kjører.

    ## Spiller
    pygame.draw.circle(vindu, "red", (spiller_x, spiller_y), spiller_radius)
    pygame.draw.circle(vindu, "red3", (spiller_x, spiller_y), spiller_radius, 5) # Dette lager en border rundt sirkelen

    ## Mat
    pygame.draw.circle(vindu, "green", (matbit1_x, matbit1_y), matbit1_radius)
    pygame.draw.circle(vindu, "green3", (matbit1_x, matbit1_y), matbit1_radius, 3)

    pygame.draw.circle(vindu, "green", (matbit2_x, matbit2_y), matbit2_radius)
    pygame.draw.circle(vindu, "green3", (matbit2_x, matbit2_y), matbit2_radius, 3)

    pygame.draw.circle(vindu, "green", (matbit3_x, matbit3_y), matbit3_radius)
    pygame.draw.circle(vindu, "green3", (matbit3_x, matbit3_y), matbit3_radius, 3)


    ## Overskrift
    tekst_overskrift = font_overskrift.render("AGARIO", True, "black") # Oppretter tekst
    vindu.blit(tekst_overskrift, (BREDDE//2 - tekst_overskrift.get_width()//2, HOYDE * 10/100)) # Tegner teksten i midten av x-posisjon og 10% ned fra toppen


    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
