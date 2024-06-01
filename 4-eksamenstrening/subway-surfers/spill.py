import pygame
import random

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
        super().__init__(KOLONNEBREDDE//2, BREDDE//2, HOYDE - 100, "darkgreen") # Dette er startverdiene til klassen
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

    def kollisjon(self):
        # Jeg lagde en klasse-metode uansett. Mtp. videre utvikling av spillet.
        avslutt_spill()


class Hindring(Spillobjekt):
    def __init__(self):
        posisjon = random.randint(0, 2)
        if posisjon == 0:
            x_pos = BREDDE//2 - KOLONNEBREDDE
        elif posisjon == 1:
            x_pos = BREDDE//2
        elif posisjon == 2:
            x_pos = BREDDE//2 + KOLONNEBREDDE
        
        super().__init__(KOLONNEBREDDE//2, x_pos, 2*MARG + KOLONNEBREDDE//4, "red")
        self.fart = 2

    def beveg(self):
        self.rect.centery += self.fart


class Tekst:
    def __init__(self, tekst: str, font_storrelse: int, farge: str, x: int, y: int):
        self.font = pygame.font.SysFont("Arial", font_storrelse)
        self.farge = farge
        self.surface = self.font.render(tekst, True, self.farge)
        self.rect = self.surface.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)

    def oppdater_tekst(self, tekst):
        self.surface = self.font.render(tekst, True, self.farge)
        self.rect = self.surface.get_rect()
        self.rect.center = (self.x, self.y)

    def tegn(self, surface):
        surface.blit(self.surface, self.rect)



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

hindringer = [Hindring()] # Starter med én hindring i lista

ny_hindring_timer = 90 # 90 frames før ny hindring spawner i spillet
blir_trykket = False

nivaa = 0
nivaatekst = Tekst(f"Nivå: {nivaa}", 38, "black", BREDDE - 100, 100)


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
    for hindring in hindringer:
        hindring.beveg()

    ## Legger til ny hindring hver 90 frame
    ny_hindring_timer -= 1
    if ny_hindring_timer <= 0:
        hindringer.append(Hindring())
        ny_hindring_timer = 90


    ## Kollisjoner:
    if spilleren.rect.collidelist(hindringer) != -1:
        spilleren.kollisjon()



    # Tegn på vinduet
    vindu.fill("white") # Fyller vinduet med en bakgrunnsfarge (fjerner alt fra forrige frame)

    ## Tegner kolonnene til spillet
    for i in range(KOLONNER + 1):
        pygame.draw.line(vindu, "darkgray", (MARG + i * KOLONNEBREDDE, 2*MARG), (MARG + i * KOLONNEBREDDE, HOYDE - MARG), KOLONNELINJEBREDDE)

    spilleren.tegn(vindu)

    for hindring in hindringer:
        hindring.tegn(vindu)

    nivaatekst.tegn(vindu)


    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
