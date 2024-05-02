import pygame

# 1. Oppsett
pygame.init()

BREDDE = 1280
HOYDE = 720
vindu = pygame.display.set_mode((BREDDE, HOYDE))

FPS = 60
klokke = pygame.time.Clock()

font = pygame.font.SysFont("Open Sans", 24)

dino_bilde = pygame.image.load("../Dino/bilder/dino1.png").convert_alpha()

while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    # 4. Oppdater spill
    # 5. Tegn
    vindu.fill("white") # Fyller vinduet med hvit bakgrunn, for hver gang loopen kjører.


    # Det norske flagget
    ## VS
    pygame.draw.rect(vindu, "red", (200, 100, 220, 190)) 
    pygame.draw.rect(vindu, "red", (200, 360, 220, 190))
    ## HS
    pygame.draw.rect(vindu, "red", (490, 100, 420, 190))
    pygame.draw.rect(vindu, "red", (490, 360, 420, 190))
    ## Blått
    pygame.draw.rect(vindu, "blue", (440, 100, 30, 450))
    pygame.draw.rect(vindu, "blue", (200, 310, 710, 30))
    

    # Tekst
    tekst_lykke_til = font.render("Lykke til!", True, "black")
    vindu.blit(tekst_lykke_til, (300, 50))

    tekst_hei = font.render("Hei på deg!", True, "blue")
    vindu.blit(tekst_hei, (BREDDE//2 - tekst_hei.get_width()//2, 70))

    # Sirkel
    pygame.draw.circle(vindu, "green", (100, 100), 40)

    # Bilde
    vindu.blit(dino_bilde, (1000, 100))

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
