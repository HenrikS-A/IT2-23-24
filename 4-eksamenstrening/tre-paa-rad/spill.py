import pygame

# Klasser
class Spillobjekt:
    def __init__(self, bredde, farge, x, y):
        self.surface = pygame.Surface((bredde, bredde))
        self.rect = self.surface.get_rect()
        self.rect.center = (x, y)
        self.surface.fill(farge)

    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)

class Celle(Spillobjekt):
    def __init__(self, x, y):
        super().__init__(180, "white", x, y)
        self.eier = None



# Oppsett av pygame
pygame.init() 
BREDDE = 720
HOYDE = 720
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE)) 
klokke = pygame.time.Clock()
pygame.display.set_caption("Tre på rad") # Navn på vinduet



## Oppsett av spill
brett = Spillobjekt(620, "black", BREDDE//2, HOYDE//2)

celler = []
for i in range(3):
    for j in range(3):
        celler.append(Celle(110 + 200*j, 110 + 200*i))


# Gameloop
while True:
    # Håndter input:
    hendelser = pygame.event.get() 
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            pygame.quit() # Avslutt spill
            raise SystemExit # Avslutt Python-programmet
    



    ## Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        print("Du trykker på 'Pil opp'.")
    if taster[pygame.K_s]:
        print("Du trykker på 's'.")

    ## Input fra mus
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()

    if mus_klikk[0]:
        print(f"Venstreklikk i posisjon {mus_posisjon}")
    if mus_klikk[2]:
        print(f"Høyreklikk i posisjon {mus_posisjon}")
    
    # Oppdater spill
    # Oppdater spillogikk her (oppdater fart, sjekk kollisjoner osv.)


    # Tegn
    vindu.fill("white") # Fyller vinduet med en bakgrunnsfarge (fjerner alt fra forrige frame)

    brett.tegn(vindu)
    for celle in celler:
        celle.tegn(brett.surface)

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
