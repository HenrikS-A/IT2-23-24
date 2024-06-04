import pygame
import random

# Klasser
class Celle:
    def __init__(self, x: int, y: int):
        self.sidelengde = 25
        self.surface = pygame.Surface((self.sidelengde, self.sidelengde))
        self.rect = self.surface.get_rect()
        self.rect.center = (x, y)
        self.lever = None
        tall = random.randint(1, 3)
        if tall == 1:
            self.lever = True
        else:
            self.lever = False

        self.oppdater_celle()
            
    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)
    
    def oppdater_celle(self):
        """ En metode som oppdaterer fargen på cellen ut i fra om den lever eller ikke """
        if self.lever == True:
            self.surface.fill("green")
        elif self.lever == False:
            self.surface.fill("red")

    def drep(self):
        self.lever = False

    def endre_livsstatus(self):
        """ En metode som endrer livsstatusen fra levende til død, og motsatt """
        if self.lever == False:
            self.lever = True
        else:
            self.lever = False
    
    def trykk(self, muspos: tuple[int, int]):
        """ En metode som sjekker om den blir trykket på. Da skal den endre livsstatus """
        if self.rect.collidepoint(muspos):
            self.endre_livsstatus()


# Funksjoner
def avslutt_spill():
    """ Avslutter spillet """
    pygame.quit()
    raise SystemExit


# Konstanter
BREDDE = 720
HOYDE = 720
FPS = 60
MARG = 50
CELLE_AVSTAND = 3
CELLE_BREDDE = 25


# Oppsett av pygame
pygame.init()
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
pygame.display.set_caption("Livets spill") # Navn på vinduet


# Oppsett av spill
celler: list[Celle] = []
for i in range((HOYDE-MARG)//(CELLE_BREDDE+CELLE_AVSTAND)):
    for j in range((BREDDE-MARG)//(CELLE_BREDDE+CELLE_AVSTAND)):
        celler.append(Celle(MARG + (CELLE_BREDDE+CELLE_AVSTAND)*j, MARG + (CELLE_BREDDE+CELLE_AVSTAND)*i))


# Gameloop
while True:
    # Hendelser:
    hendelser = pygame.event.get() 
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            avslutt_spill()

        # Mus-klikk
        if hendelse.type == pygame.MOUSEBUTTONDOWN: # Sjekker bare én gang når musen klikkes NED
            mus_posisjon = pygame.mouse.get_pos()
            for celle in celler:
                celle.trykk(mus_posisjon)

    # Oppdater spill
    for celle in celler:
        celle.oppdater_celle()
        # celle.drep()

    # Tegn på vinduet
    vindu.fill("gray") # Fyller vinduet med en bakgrunnsfarge (fjerner alt fra forrige frame)

    for celle in celler:
        celle.tegn(vindu)

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
