import pygame

# 1. Oppsett
pygame.init()

BREDDE = 1280
HOYDE = 720
vindu = pygame.display.set_mode((BREDDE, HOYDE))

FPS = 60
klokke = pygame.time.Clock()

# Norsk flagg - riktig forholdstall
def norges_flagg(x_koordinat, y_koordinat, flagg_storrelse):
    # Rød bakgrunn:
    pygame.draw.rect(vindu, (206, 0, 0), (x_koordinat, y_koordinat, 22*flagg_storrelse, 16*flagg_storrelse))
    # Hvitt kors:
    pygame.draw.rect(vindu, "white", (x_koordinat + 6*flagg_storrelse, y_koordinat, 4*flagg_storrelse, 16*flagg_storrelse))
    pygame.draw.rect(vindu, "white", (x_koordinat, y_koordinat + 6*flagg_storrelse, 22*flagg_storrelse, 4*flagg_storrelse))
    # Blått kors:
    pygame.draw.rect(vindu, (0, 31, 100), (x_koordinat + 7*flagg_storrelse, y_koordinat, 2*flagg_storrelse, 16*flagg_storrelse))
    pygame.draw.rect(vindu, (0, 31, 100), (x_koordinat, y_koordinat + 7*flagg_storrelse, 22*flagg_storrelse, 2*flagg_storrelse))


while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    # 4. Oppdater spill
    # 5. Tegn
    vindu.fill((240, 240, 240)) # Fyller vinduet med hvit bakgrunn, for hver gang loopen kjører.


    norges_flagg(300, 150, 30)


    """
    # Det norske flagget
    # VS
    pygame.draw.rect(vindu, "red", (200, 100, 220, 190)) 
    pygame.draw.rect(vindu, "red", (200, 360, 220, 190))

    # HS
    pygame.draw.rect(vindu, "red", (490, 100, 420, 200))
    pygame.draw.rect(vindu, "red", (490, 360, 430, 200))

    # Blått
    pygame.draw.rect(vindu, "blue", (440, 100, 30, 450))
    pygame.draw.rect(vindu, "blue", (200, 310, 710, 30))
    """


    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
