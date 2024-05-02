import pygame

# 1. Oppsett
pygame.init()

BREDDE = 1280
HOYDE = 720
vindu = pygame.display.set_mode((BREDDE, HOYDE))

FPS = 60
klokke = pygame.time.Clock()

pygame.display.set_caption("Dinosaur spillet") # Navn på vinduet

font = pygame.font.SysFont("Open Sans", 24) # Skrifttype
font_overskrift = pygame.font.SysFont("Open Sans", 60)

# Bilder
dino_bilde_1 = pygame.image.load("bilder/dino1.png").convert_alpha()
dino_bilde_2 = pygame.image.load("bilder/dino2.png").convert_alpha()
dino_naverende_bilde = 1

bakken = pygame.image.load("bilder/bakgrunn.png").convert_alpha()

# Spiller størrelser
dino_bredde = dino_bilde_1.get_width()
dino_hoyde = dino_bilde_1.get_height()

# Startposisjoner
dino_x = 100
dino_y = 300

bakke_x = 50
bakke_y = 500

# Mekanikk
dino_y_fart = 0
gravitasjon = 0.2


teller = 8 # bruker den til å endre dinosaurbildet hver gang teller er delelig på 8.

while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    taster = pygame.key.get_pressed()
    
    if taster[pygame.K_UP] or taster[pygame.K_w] or taster[pygame.K_SPACE]:
        dino_y_fart -= 1
        dino_y -= 5
    

    # 3. Oppdater spill
    dino_rektangel = pygame.Rect(dino_x, dino_y, dino_bredde, dino_hoyde) # Kollisjonsboks

    if dino_y > HOYDE - 310:
        dino_y_fart = 0
    else:
        dino_y_fart += gravitasjon
    dino_y += dino_y_fart


    # 4. Tegn
    vindu.fill("white") # Fyller vinduet med hvit bakgrunn, for hver gang loopen kjører.

    ## Overskrift
    tekst_overskrift = font_overskrift.render("DINO", True, "black") # Oppretter tekst
    vindu.blit(tekst_overskrift, (BREDDE//2 - tekst_overskrift.get_width()//2, HOYDE * 10/100)) # Tegner teksten i midten av x-posisjon og 10% ned fra toppen

    ## Tegner bakken
    vindu.blit(bakken, (bakke_x, bakke_y))

    ## Tegner dinosaur, endrer bildet for hver gang telleren kan deles på 8
    if teller % 8 == 0:
        if dino_naverende_bilde == 1:
            vindu.blit(dino_bilde_2, (dino_x, dino_y))
            dino_naverende_bilde = 2
        elif dino_naverende_bilde == 2:
            vindu.blit(dino_bilde_1, (dino_x, dino_y))
            dino_naverende_bilde = 1
    else:
        if dino_naverende_bilde == 1:
            vindu.blit(dino_bilde_1, (dino_x, dino_y))
        elif dino_naverende_bilde == 2:
            vindu.blit(dino_bilde_2, (dino_x, dino_y))

    
    
    teller += 1
    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
