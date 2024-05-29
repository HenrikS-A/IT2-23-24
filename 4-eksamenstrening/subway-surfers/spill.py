import pygame

# Klasser
class Spillobjekt:
    def __init__(self, sidelengde: int, x: int, y: int, farge: str):
        self.surface = pygame.Surface((sidelengde, sidelengde))
        self.rect = self.surface.get_rect()
        self.rect.center = (x, y)
        self.surface.fill(farge)

    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)

class Spiller(Spillobjekt):
    def __init__(self):
        self.x = BREDDE//2 # Dette er startverdien til x-posisjonen
        super().__init__(KOLONNEBREDDE//2, self.x, HOYDE - 100, "darkgreen")
        self.posisjon = 1
    
    def beveg(self, tastaturinput: int):
            if self.posisjon == 0:
                if tastaturinput == pygame.K_RIGHT:
                    self.rect.centerx += KOLONNEBREDDE
                    self.posisjon = 1
            elif self.posisjon == 1:
                if tastaturinput == pygame.K_LEFT:
                    self.rect.centerx -= KOLONNEBREDDE
                    self.posisjon = 0
                if tastaturinput == pygame.K_RIGHT:
                    self.rect.centerx += KOLONNEBREDDE
                    self.posisjon = 2
            elif self.posisjon == 2:
                if tastaturinput == pygame.K_LEFT:
                    self.rect.centerx -= KOLONNEBREDDE
                    self.posisjon = 1



# Funksjoner
def avslutt_spill():
    """ Avslutter spillet """
    pygame.quit()
    raise SystemExit


# Konstanter
BREDDE = 500
HOYDE = 720
FPS = 60
KOLONNER = 3
MARG = 50
KOLONNELINJEBREDDE = 5
KOLONNEBREDDE = (BREDDE - 2*MARG) // KOLONNER


# Oppsett av pygame
pygame.init()
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
pygame.display.set_caption("Subway Surfers") # Navn på vinduet


# Oppsett av spill
spilleren = Spiller()

blir_trykket = False


# Gameloop
while True:
    # Hendelser:
    hendelser = pygame.event.get() 
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            avslutt_spill()

        # Input fra tastatur
        if hendelse.type == pygame.KEYDOWN:
            spilleren.beveg(hendelse.key)

    
    

    # Input fra mus
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()
    if mus_klikk[0]:
        print(f"Venstreklikk i posisjon {mus_posisjon}")
    if mus_klikk[2]:
        print(f"Høyreklikk i posisjon {mus_posisjon}")
    

    # Oppdater spill




    # Tegn på vinduet
    vindu.fill("white") # Fyller vinduet med en bakgrunnsfarge (fjerner alt fra forrige frame)

    ## Tegner kolonnene til spillet
    for i in range(KOLONNER + 1):
        pygame.draw.line(vindu, "darkgray", (MARG + i * KOLONNEBREDDE, 2*MARG), (MARG + i * KOLONNEBREDDE, HOYDE - MARG), KOLONNELINJEBREDDE)

    spilleren.tegn(vindu)

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
