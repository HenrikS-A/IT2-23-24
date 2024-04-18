import pygame
import random

# Klasser
class Objekt:
    def __init__(self, x: int, y: int, tekst: str, farge: str):
        self.sidelengde = 60
        self.surface = pygame.Surface((self.sidelengde, self.sidelengde))
        self.rect = self.surface.get_rect()
        
        # self.rect = pygame.Rect(self.sidelengde, self.sidelengde, self.sidelengde, self.sidelengde)
        self.rect.centerx = x
        self.rect.centery = y
        self.surface.fill(farge)

        # Til bokstav tekst:
        self.fonten = pygame.font.SysFont("Open Sans", 50) # Skrift font
        self.tekst = self.fonten.render(tekst, True, "black") # Selve teksten
        self.tekst_ramme = self.tekst.get_rect() # Henter rammen rundt teksten
        self.tekst_ramme.center = self.rect.center # Plasserer sentrum av tekst-rammen på samme pos. som sentrum til rektangelet.

    def oppdater(self):
        self.tekst_ramme.center = self.rect.center

    def tegn(self, vindu):
        # pygame.draw.rect(vindu, self.farge, self.rect)
        vindu.blit(self.surface, self.rect)
        vindu.blit(self.tekst, (self.tekst_ramme))


class Troll(Objekt):
    def __init__(self):
        super().__init__(BREDDE//2, HOYDE//2, "T", "green") # Alle spillere skal ha disse verdiene
        self.spillerfart = 5 # Konstant fart hele tiden
        self.retning = random.randint(1, 4) # Jeg velger en tilfeldig start-retning for spilleren.
        
    def beveg(self):

        # Retninger:
        # 1 = Høyre
        # 2 = Ned
        # 3 = Venstre
        # 4 = Opp

        if self.retning == 1:
            self.rect.centerx += self.spillerfart
        elif self.retning == 2:
            self.rect.centery += self.spillerfart
        elif self.retning == 3:
            self.rect.centerx -= self.spillerfart
        elif self.retning == 4:
            self.rect.centery -= self.spillerfart


class Matbit(Objekt):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "M", "yellow") # Alle matbiter skal ha disse verdiene

class Hindring(Objekt):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "H", "gray") # Standardverdier




# 1. Oppsett
pygame.init()

BREDDE = 1280
HOYDE = 720
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

pygame.display.set_caption("Pactroll") # Navn på vinduet
font = pygame.font.SysFont("Open Sans", 24) # Skrifttype



spiller = Troll()


matbiter = []
for _ in range(3):

    # Her må jeg legge inn kode for å forsikre meg om at matbitene ikke spawner oppå hverandre.

    matbiter.append(Matbit(random.randint(10, BREDDE-10), random.randint(10, HOYDE-10)))


hindringer = []

# For at jeg ikke dør med en gang jeg spiser en matbit
tillatte_hindringer = []

kollisjon = False



while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                spiller.retning = 1
            if event.key == pygame.K_DOWN:
                spiller.retning = 2
            if event.key == pygame.K_LEFT:
                spiller.retning = 3
            if event.key == pygame.K_UP:
                spiller.retning = 4
            
    
    # 3. Oppdater spill
    spiller.beveg()
    spiller.oppdater()


    ## Kollisjoner:
    kollisjoner_liste = spiller.rect.collidelistall([matbit.rect for matbit in matbiter])
    if len(kollisjoner_liste) > 0:
        for i in kollisjoner_liste: # Det er en liste med indeks-er

            if not kollisjon: 
                kollisjon = True

                # Spawner en ny matbit på spillebrettet ved en kollisjon
                matbiter.append(Matbit(random.randint(10, BREDDE-10), random.randint(10, HOYDE-10)))

                # Jeg legger en hindring rett over matbiten, jeg fjerner ikke matbit.
                ny_hindring = Hindring(matbiter[i].rect.centerx, matbiter[i].rect.centery)

                hindringer.append(ny_hindring)
                tillatte_hindringer.append(ny_hindring) # For at spilleren ikke dør med en gang
    else:
        kollisjon = False # Når spiller ikke kolliderer lengre


    # For hver frame, sjekker jeg om spilleren kolliderer med noen av de tillatte hindringene 
    # (sjekker alle fra lista), Hvis spilleren ikke gjør det (lenger), 
    # fjerner jeg alt fra tillatte hindringer.
    kollisjonsindeks = spiller.rect.collidelist([hindring.rect for hindring in hindringer])    
    if kollisjonsindeks == -1:
        tillatte_hindringer.clear() # Fjerner alt fra lista!
        pass


    # Hvis spiller kolliderer med hindring (som ikke er tillatt), avslutt spillet
    for i in range(len(hindringer)):
        if spiller.rect.colliderect(hindringer[i].rect) and hindringer[i] not in tillatte_hindringer:
            pygame.quit()
            raise SystemExit


    # 4. Tegn

    vindu.fill("black") # Fyller vinduet med sort bakgrunn, for hver gang loopen kjører.

    for matbit in matbiter:
        matbit.tegn(vindu)
    
    for hindring in hindringer:
        hindring.tegn(vindu)

    spiller.tegn(vindu)


    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)

