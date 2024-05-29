import pygame

# Klasser
class Spillobjekt:
    def __init__(self, sidelengde: int, farge: str, x: int, y: int):
        self.surface = pygame.Surface((sidelengde, sidelengde))
        self.rect = self.surface.get_rect()
        self.rect.center = (x, y)
        self.surface.fill(farge)

    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)


# Funksjoner
def avslutt_spill():
    """ Avslutter spillet """
    pygame.quit()
    raise SystemExit


# Konstanter
BREDDE = 720
HOYDE = 720
FPS = 60
KOLONNER = 3
KOLONNEBREDDE = 50
MARG = 50


# Oppsett av pygame
pygame.init()
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
pygame.display.set_caption("Subway Surfers") # Navn på vinduet


# Oppsett av spill
objekt = Spillobjekt(100, "green", 100, 100)


# Gameloop
while True:
    # Hendelser:
    hendelser = pygame.event.get() 
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            avslutt_spill()
        
    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        print("Du trykker på 'Pil opp'.")
    if taster[pygame.K_s]:
        print("Du trykker på 's'.")

    # Input fra mus
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()
    if mus_klikk[0]:
        print(f"Venstreklikk i posisjon {mus_posisjon}")
    if mus_klikk[2]:
        print(f"Høyreklikk i posisjon {mus_posisjon}")
    

    # Oppdater spill

    # Spillogikk (oppdater fart, sjekk kollisjoner osv.)


    # Tegn på vinduet
    vindu.fill("white") # Fyller vinduet med en bakgrunnsfarge (fjerner alt fra forrige frame)
    
    for i in range(KOLONNER + 1):
        pygame.draw.line(vindu, "red", (100, 100), (100, 150))

    # MARG + i * KOLONNEBREDDE, MARG
    # MARG + i * KOLONNEBREDDE, HOYDE - MARG

    

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
