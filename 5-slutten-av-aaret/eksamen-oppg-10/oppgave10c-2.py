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
        self.skal_endre_livsstatus = False
        self.naboer = []

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
        if self.lever:
            self.surface.fill("black")
        else:
            self.surface.fill("white")

    def drep(self):
        self.lever = False

    def endre_livsstatus(self):
        """ En metode som endrer livsstatusen fra levende til død, og motsatt """
        if not self.lever:
            self.lever = True
        else:
            self.lever = False

    def trykk(self, muspos: tuple[int, int]):
        """ En metode som sjekker om den blir trykket på. Da skal den endre livsstatus """
        if self.rect.collidepoint(muspos):
            self.endre_livsstatus()

    def finn_naboer(self, celleliste: list[list], rad: int, kolonne: int):
        # Muligens noe feil her.
        naboer = []
        rader, kolonner = len(celleliste), len(celleliste[0]) # Maks-lengdene

        for i in range(rad-1, rad+2):
            for j in range(kolonne-1, kolonne+2):
                # Her sjekker jeg at jeg holder meg innenfor celle-koordinatsystemet 
                # og at egen plassering ikke registres som en naboplassering - da må altså 
                # maks én av koordinatene være lik input koordinatene
                if i >= 0 and i < rader and j >= 0 and j < kolonner and (i != rad or j != kolonne):
                    naboer.append(celleliste[i][j])

        self.naboer = naboer

    def ny_generasjon(self):
        # Muligens noe feil her.
        naboer_som_lever = []
        for nabo in self.naboer:
            if nabo.lever == True:
                naboer_som_lever.append(nabo)

        if self.lever == True and len(naboer_som_lever) < 2:
            self.skal_endre_livsstatus = True
        elif self.lever == True and len(naboer_som_lever) > 3:
            self.skal_endre_livsstatus = True
        elif self.lever == False and len(naboer_som_lever) == 3:
            self.skal_endre_livsstatus = True


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
antall_horisontalt = (BREDDE-MARG)//(CELLE_BREDDE+CELLE_AVSTAND)
antall_vertikalt = (HOYDE-MARG)//(CELLE_BREDDE+CELLE_AVSTAND)

## Oppretter cellene i riktig posisjon og legger dem til i en nøstet liste
for i in range(antall_vertikalt):
    liste = []
    for j in range(antall_horisontalt):
        liste.append(Celle(MARG + (CELLE_BREDDE+CELLE_AVSTAND)*j, MARG + (CELLE_BREDDE+CELLE_AVSTAND)*i))
    celler.append(liste)

## Finner naboene til hver celle (kanskje er det noe feil her.)
for i, nostet_liste in enumerate(celler):
    rad = i
    for j, celle in enumerate(nostet_liste):
        kolonne = j
        celle.finn_naboer(celler, rad, kolonne)
        pass
    pass
pass

## Legger alle cellene i en flat celle-liste
# celler = []
# for liste in nostet_celleliste:
#     celler.extend(liste)


ny_generasjon_teller = 60 # Jeg har 60fps, så hvert sekund er en ny generasjon.

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
            for celleliste in celler:
                for celle in celleliste:
                    celle.trykk(mus_posisjon)

    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_SPACE]:
        for celleliste in celler:
            for celle in celleliste:
        
                celle.drep()
                ny_generasjon_teller = 300 # Du har 5 sekunder på å plassere ut ting etter å ha drept alle.


    # Oppdater spill
    for celleliste in celler:
        for celle in celleliste:
            celle.oppdater_celle()
    ny_generasjon_teller -= 1




    ## Finner naboene til hver celle (kanskje er det noe feil her.)
    for i, nostet_liste in enumerate(celler):
        rad = i
        for j, celle in enumerate(nostet_liste):
            kolonne = j
            celle.finn_naboer(celler, rad, kolonne)
            pass





    if ny_generasjon_teller <= 0:
        for celleliste in celler:
            for celle in celleliste:
                celle.ny_generasjon()
    
        ny_generasjon_teller = 60 # Resetter nedtellingen til neste generasjon

        # Her fungerer ikke ting.
        for celleliste in celler:
            for celle in celleliste:
                if celle.skal_endre_livsstatus:
                    celle.endre_livsstatus()

    

    # Tegn på vinduet
    vindu.fill("gray") # Fyller vinduet med en bakgrunnsfarge (fjerner alt fra forrige frame)

    for celleliste in celler:
        for celle in celleliste:
            celle.tegn(vindu)

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
