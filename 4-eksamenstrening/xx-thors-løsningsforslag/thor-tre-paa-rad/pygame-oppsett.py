import pygame

# Oppsett av pygame
pygame.init()
BREDDE = 600  # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

# OPPSETT AV SPILL HER:

while True:
    # fyll skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")

    # Hendelser
    for hendelse in pygame.event.get():
        # pygame.QUIT hendelsen skjer når brukeren klikke på X for å lukke vinduet
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        print("pil opp")
    if taster[pygame.K_s]:
        print("s")

    # Input fra mus:
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()
    if mus_klikk[0]:
        print(f"Venstre klikk i posisjon {mus_posisjon}")
    if mus_klikk[1]:
        print(f"Hjul-klikk i posisjon {mus_posisjon}")
    if mus_klikk[2]:
        print(f"Høyreklikk i posisjon {mus_posisjon}")

    # Oppdater spill her:

    # Tegn på skjermen her:

    # flip() oppdater vinduet med alle endringer
    pygame.display.flip()

    # klokke.tick(60) begrenser spillet til 60 FPS (frames per second)
    klokke.tick(60)
