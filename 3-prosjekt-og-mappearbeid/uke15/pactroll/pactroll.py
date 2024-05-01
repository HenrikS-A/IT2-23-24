import pygame
import random


# Klasser
class Spillobjekt:
    """ Representerer et spillobjekt.

    Argumenter:
        x (int): x-koordinatet til spillobjektet.
        y (int): y-koordinatet til spillobjektet.
        farge (str): Fargen til spillobjektet, eks. "red".
        tekst (str): Teksten som skal vises på spillobjektet.
    
    Attributter:
        sidelengde (int): Sidelengden til spillobjektets overflate.
        surface (pygame.Surface): Pygame-overflate for spillobjektet.
        rect (pygame.Rect): Rektangel som definerer spillobjektets posisjon og størrelse.
        font (pygame.font.Font): Skriftfont for teksten.
        tekst (pygame.Surface): Overflate som inneholder teksten som skal vises på spillobjektet.
        tekst_ramme (pygame.Rect): Rektangel som definerer området for teksten på spillobjektet.

    Metoder:
        oppdater(): Oppdaterer posisjonen til teksten på spillobjektet
        tegn(vindu: pygame.Surface): Tegner spillobjektet på angitt pygame-vindu.
    """

    def __init__(self, x: int, y: int, farge: str, tekst: str):
        """ Initialiserer et nytt Spillobjekt med angitt posisjon (x, y), farge og tekst. """
        self.sidelengde = 60
        self.surface = pygame.Surface((self.sidelengde, self.sidelengde))
        self.rect = self.surface.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.surface.fill(farge)

        # Til bokstav-tekst:
        self.font = pygame.font.SysFont("Open Sans", 50) # Skrift font
        self.tekst = self.font.render(tekst, True, "black") # Selve teksten
        self.tekst_ramme = self.tekst.get_rect() # Henter rammen rundt teksten
        self.tekst_ramme.center = self.rect.center # Plasserer sentrum av teksten i sentrum av spillobjektet

    def oppdater(self):
        """ Oppdaterer posisjonen til teksten på spillobjektet. 

        Dette må gjøres for hver frame slik at tekst og figur hele 
        tiden ligger over hverandre.
        """

        self.tekst_ramme.center = self.rect.center

    def tegn(self, vindu: pygame.Surface):
        """ Tegner spillobjektet på angitt pygame-vindu.

        Argumenter:
            vindu (pygame.Surface): Overflaten som objektet skal tegnes på.
        """

        vindu.blit(self.surface, self.rect)
        vindu.blit(self.tekst, self.tekst_ramme)


class Troll(Spillobjekt):
    def __init__(self):
        # I stedet for å velge parametere når jeg oppretter de ulike obketene,
        # velger jeg her hvilken posisjon, bokstav og farge troll-objekter skal ha
        super().__init__(BREDDE//2, HOYDE//2, "green", "T")
        self.spillerfart = 1
        self.retning = random.randint(1, 4) # Jeg velger en tilfeldig start-retning for spilleren.
        self.poeng = 0

    def beveg(self, tastaturinput: pygame.key.ScancodeWrapper):
        # Her endrer jeg bare retningen og ikke faktisk bevegelse
        # for at trollet ikke skal stoppe hvis spilleren slipper opp tasten
        
        taster = tastaturinput
        if taster[pygame.K_RIGHT] or taster[pygame.K_d]:
            self.retning = 1
        if taster[pygame.K_DOWN] or taster[pygame.K_s]:
            self.retning = 2
        if taster[pygame.K_LEFT] or taster[pygame.K_a]:
            self.retning = 3
        if taster[pygame.K_UP] or taster[pygame.K_w]:
            self.retning = 4
        
        # Retninger:
        # 1 -> Høyre
        # 2 -> Ned
        # 3 -> Venstre
        # 4 -> Opp

        if self.retning == 1:
            self.rect.centerx += self.spillerfart
        elif self.retning == 2:
            self.rect.centery += self.spillerfart
        elif self.retning == 3:
            self.rect.centerx -= self.spillerfart
        elif self.retning == 4:
            self.rect.centery -= self.spillerfart

    def sjekk_posisjon(self):
        if (self.rect.left <= 0
            or self.rect.right >= BREDDE
            or self.rect.top <= 0
            or self.rect.bottom >= HOYDE):
            pygame.quit()
            raise SystemExit

    def oek_fart_og_poeng(self):
        self.poeng += 1
        self.spillerfart += 1

    def vis_poeng(self, vindu: pygame.Surface, skjerm_bredde: int, skjerm_hoyde: int):
        poeng_font = pygame.font.SysFont("Open Sans", 60)
        poeng_surface = poeng_font.render(f"{self.poeng}", True, "white")
        vindu.blit(poeng_surface, (skjerm_bredde * 0.94, skjerm_hoyde * 0.10))


class Matbit(Spillobjekt):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "yellow", "M") # Matbiter skal ha bokstav "M" og fargen gul


class Hindring(Spillobjekt):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "gray", "H") # Hindringer skal ha bokstav "H" og fargen grå


# 1. Oppsett
pygame.init()
BREDDE = 1280
HOYDE = 720
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
pygame.display.set_caption("Pactroll") # Navn på vinduet

## Oppsett av spill
spiller = Troll()
matbiter = [Matbit(random.randint(30, BREDDE-30), random.randint(30, HOYDE-30)) for _ in range(3)]

hindringer: list[Hindring] = []
tillatte_hindringer = [] # For at jeg ikke dør med en gang jeg spiser en matbit

kollisjon = False

while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    ## Input fra tastatur:
    taster = pygame.key.get_pressed()


    # 3. Oppdater spill
    spiller.beveg(taster)
    spiller.oppdater()
    spiller.sjekk_posisjon()

    ## Kollisjoner:

    # collidelisteall() sjekker hvilke rects som kolliderer og returnerer en liste med indeks-er
    kollisjoner_liste = spiller.rect.collidelistall([matbit.rect for matbit in matbiter])
    if len(kollisjoner_liste) > 0:
        for i in kollisjoner_liste:
            # Jeg skal bare kjøre denne én gang og ikke hver eneste frame,
            # så denne kjører bare akkurat i det den oppdager en ny kollisjon
            if not kollisjon:
                kollisjon = True

                # Spawner en ny matbit på spillebrettet ved en kollisjon
                matbiter.append(Matbit(random.randint(30, BREDDE-30), random.randint(30, HOYDE-30)))

                # Jeg oppretter en hindring rett over matbiten
                ny_hindring = Hindring(matbiter[i].rect.centerx, matbiter[i].rect.centery)

                hindringer.append(ny_hindring)
                tillatte_hindringer.append(ny_hindring) # For at spilleren ikke dør med en gang

                spiller.oek_fart_og_poeng()
    else:
        kollisjon = False # Når spiller ikke kolliderer lengre

    # For hver frame, sjekker jeg om spilleren kolliderer med noen av de tillatte hindringene 
    # (sjekker alle fra lista). Hvis spilleren ikke kolliderer med noen hindringer, 
    # så fjerner jeg alt fra tillatte hindringer
    kollisjonsindeks = spiller.rect.collidelist([hindring.rect for hindring in hindringer])    
    if kollisjonsindeks == -1:
        tillatte_hindringer.clear() # Fjerner alt fra lista

    # Hvis spiller kolliderer med hindring (som ikke er tillatt) -> avslutt spillet
    for hindring in hindringer:
        if spiller.rect.colliderect(hindring) and hindring not in tillatte_hindringer:
            pygame.quit()
            raise SystemExit


    # 4. Tegn
    vindu.fill("black") # Fyller vinduet med sort bakgrunn for hver gang loopen kjører

    spiller.vis_poeng(vindu, BREDDE, HOYDE)

    # Slår listene (og spiller objektet) sammen til én liste med enkelt-objekter, 
    # så tegner jeg hvert objekt i lista
    for objekt in [*matbiter, *hindringer, spiller]:
        objekt.tegn(vindu)

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
