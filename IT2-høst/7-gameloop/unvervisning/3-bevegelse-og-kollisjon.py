import pygame

# 1. Oppsett
pygame.init()

BREDDE = 1280
HOYDE = 720
vindu = pygame.display.set_mode((BREDDE, HOYDE))

FPS = 60
klokke = pygame.time.Clock()

font = pygame.font.SysFont("Open Sans", 24)
font_overskrift = pygame.font.SysFont("Open Sans", 60)

dino_bilde_1 = pygame.image.load("../Dino/bilder/dino1.png").convert_alpha()
dino_bilde_2 = pygame.image.load("../Dino/bilder/dino2.png").convert_alpha()
dino_naverende_bilde = 1

kaboom_bilde = pygame.image.load("kaboom-comic-sticker-31219-550x550.png").convert_alpha()
kaboom_bilde = pygame.transform.scale_by(kaboom_bilde, 0.5)


# Startposisjoner
spiller1_x = 900
spiller1_y = 200

spiller2_x = 300
spiller2_y = 400

spiller_dino_x = BREDDE//2
spiller_dino_y = HOYDE//2

# Spillerstørrelser
spiller1_bredde = 100
spiller1_hoyde = 100

spiller2_bredde = 100
spiller2_hoyde = 100



teller = 5 # bruker den til å endre dinosaurbildet hver 5 teller.

while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        

    taster = pygame.key.get_pressed()

    # Spiller 1 kontroll:
    if taster[pygame.K_UP]:
        spiller1_y -= 1
    if taster[pygame.K_DOWN]:
        spiller1_y += 1
    if taster[pygame.K_LEFT]:
        spiller1_x -= 1
    if taster[pygame.K_RIGHT]:
        spiller1_x += 1

    # Spiller 2 kontroll:
    if taster[pygame.K_w]:
        spiller2_y -= 1
    if taster[pygame.K_s]:
        spiller2_y += 1
    if taster[pygame.K_a]:
        spiller2_x -= 1
    if taster[pygame.K_d]:
        spiller2_x += 1

    # Spiller dinosaur kontroll:
    if taster[pygame.K_u]:
        spiller_dino_y -= 1
    if taster[pygame.K_j]:
        spiller_dino_y += 1
    if taster[pygame.K_h]:
        spiller_dino_x -= 1
    if taster[pygame.K_k]:
        spiller_dino_x += 1
    
    
    # 3. Oppdater spill
    spiller1_rektangel = pygame.Rect(spiller1_x, spiller1_y, spiller1_bredde, spiller1_hoyde)
    spiller2_rektangel = pygame.Rect(spiller2_x, spiller2_y, spiller2_bredde, spiller2_hoyde)

    

    # 4. Tegn
    vindu.fill("white") # Fyller vinduet med hvit bakgrunn, for hver gang loopen kjører.

    if spiller1_rektangel.colliderect(spiller2_rektangel):
        print("KOLLLLLLLISSSSSJON!!!!!!")

        tekst_kollisjon = font.render("BOOOOOOM!", True, "black")
        vindu.blit(tekst_kollisjon, (BREDDE//2 - tekst_kollisjon.get_width()//2, HOYDE * 50/100))

        vindu.blit(kaboom_bilde, ( (spiller2_x + spiller2_bredde//2) - kaboom_bilde.get_width()//2 , ((spiller2_y + spiller2_hoyde//2) - kaboom_bilde.get_width()//2) - spiller2_hoyde * 1.5))




    # Overskrift
    tekst_overskrift = font_overskrift.render("DINO", True, "black")
    vindu.blit(tekst_overskrift, (BREDDE//2 - tekst_overskrift.get_width()//2, HOYDE * 10/100))

    # Spillere
    ## Spiller 1:
    pygame.draw.rect(vindu, "blue", (spiller1_x, spiller1_y, spiller1_bredde, spiller1_hoyde))
    ## Spiller 2:
    pygame.draw.rect(vindu, "red", (spiller2_x, spiller2_y, spiller2_bredde, spiller2_hoyde))

    ## Dinosaur, endrer bildet for hver gang telleren kan deles på 5
    if teller % 5 == 0:
        if dino_naverende_bilde == 1:
            vindu.blit(dino_bilde_2, (spiller_dino_x, spiller_dino_y))
            dino_naverende_bilde = 2
        elif dino_naverende_bilde == 2:
            vindu.blit(dino_bilde_1, (spiller_dino_x, spiller_dino_y))
            dino_naverende_bilde = 1
    else:
        if dino_naverende_bilde == 1:
            vindu.blit(dino_bilde_1, (spiller_dino_x, spiller_dino_y))
        elif dino_naverende_bilde == 2:
            vindu.blit(dino_bilde_2, (spiller_dino_x, spiller_dino_y))


    teller += 1

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
