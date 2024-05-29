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
    """ Representerer et troll-objekt i spillet.

    Arver fra Spillobjekt og definerer troll-spesifikke egenskaper her.
    Da legger jeg ikke inn parametere når jeg oppretter objektet, men
    den får ulike standardverdier her.

    Attributter:
        spillerfart (int): Farten til troll-objektet.
        retning (int): Retningen troll-objektet beveger seg i. \
            Mulige verdier: 1 (høyre), 2 (ned), 3 (venstre), 4 (opp).
        poeng (int): Antall poeng troll-objektet har oppnådd.

    Metoder:
        beveg(tastaturinput: pygame.key.ScancodeWrapper): Endrer retningen \
            på trollpbjektet basert på tastaturinput.
        sjekk_posisjon(skjerm_bredde: int, skjerm_hoyde: int): Sjekker om trollobjektet \
            er utenfor spillvinduet og avslutter hvis det er tilfellet.
        oek_fart_og_poeng(): Øker farten og poengsummen til troll-objektet.
        vis_poeng(vindu: pygame.Surface, skjerm_bredde: int, skjerm_hoyde: int): Viser \
            poengsummen til trollobjektet på spillviduet. 

    """
    def __init__(self):
        super().__init__(BREDDE//2, HOYDE//2, "green", "T")
        """ Initialiserer et nytt Troll-objekt med standardverdier. 
        
        Jeg slipper å velge parametere når jeg oppretter de ulike objektene.
        Her velger jeg posisjon, farge og bokstav som troll-objekter skal ha.
        """

        self.spillerfart = 1
        self.retning = random.randint(1, 4) # Jeg velger en tilfeldig start-retning for spilleren.
        self.poeng = 0

    def beveg(self, tastaturinput: pygame.key.ScancodeWrapper):
        """ Endrer retningen til troll-objektet basert på tastaturinput. 

        Retning har de mulige verdiene: 1 (høyre), 2 (ned), 3 (venstre), 4 (opp).
        
        Argumenter: 
            tastaturinput (pygame.key.ScancodeWrapper): Tastaturinput som styrer trollet.
        """

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

        if self.retning == 1:
            self.rect.centerx += self.spillerfart
        elif self.retning == 2:
            self.rect.centery += self.spillerfart
        elif self.retning == 3:
            self.rect.centerx -= self.spillerfart
        elif self.retning == 4:
            self.rect.centery -= self.spillerfart

    def sjekk_posisjon(self, skjerm_bredde: int, skjerm_hoyde: int):
        """ Sjekker om troll_objektet er utenfor spillvinduet og avslutter om det er tilfellet. """
        if (self.rect.left <= 0
            or self.rect.right >= skjerm_bredde
            or self.rect.top <= 0
            or self.rect.bottom >= skjerm_hoyde):
            pygame.quit()
            raise SystemExit

    def oek_fart_og_poeng(self):
        """ Øker farten og poengsummen til troll-objektet. """
        self.poeng += 1
        self.spillerfart += 1

    def vis_poeng(self, vindu: pygame.Surface, skjerm_bredde: int, skjerm_hoyde: int):
        """ Viser poengsummen til troll-objektet på spillvinduet. 
        
        Argumenter:
            vindu (pygame.Surface): Overflaten hvor poengsummen skal vises.
            skjerm_bredde (int): Bredde på spillvinduet
            skjerm_hoyde (int): Høyde på spillvinduet.
        """

        poeng_font = pygame.font.SysFont("Open Sans", 60)
        poeng_surface = poeng_font.render(f"{self.poeng}", True, "white")
        vindu.blit(poeng_surface, (skjerm_bredde * 0.94, skjerm_hoyde * 0.10))


class Matbit(Spillobjekt):
    """ Representerer en matbit i spillet.
    
    Arver fra Spillobjekt og definerer matbit-spesifikke egenskaper.
    """
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "yellow", "M") # Matbiter skal ha bokstav "M" og fargen gul
        """ Initialiserer en ny Matbit med standardverdier. """

    

    
    @classmethod # Gjør at man kan kalle funksjoner uten å initiere en matbit først.
    def opprett_nytt_koordinat(cls, koordinatliste: list[tuple]) -> list[int]:
        x = random.randint(30, BREDDE-30)
        y = random.randint(30, HOYDE-30)

        sjekk = True
        while sjekk:
            # While-loopen kjører igjen bare hvis jeg må endre et koordinat i løpet av koden under.
            # Hvis ikke, kjører while-loopen bare én gang
            sjekk = False 

            for koord in koordinatliste:
                while abs(koord[0] - x) <= 60:
                    x = random.randint(30, BREDDE-30)
                    sjekk = True
                while abs(koord[1] - y) <= 60:
                    y = random.randint(30, HOYDE-30)
                    sjekk = True
        return [x, y]





class Hindring(Spillobjekt):
    """ Representerer en hindring i spillet.
    
    Arver fra Spillobjekt og definerer hindring-spesifikke egenskaper.
    """
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "gray", "H") # Hindringer skal ha bokstav "H" og fargen grå
        """ Initialiserer en ny Hindring med standardverdier. """



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
# matbiter = [Matbit(random.randint(30, BREDDE-30), random.randint(30, HOYDE-30)) for _ in range(3)]


matbitkoordinater: list[(int, int)] = []
matbiter: list[Matbit] = []
for _ in range(3):
    ny_x, ny_y = Matbit.opprett_nytt_koordinat(matbitkoordinater)
    matbiter.append(Matbit(ny_x, ny_y))
    matbitkoordinater.append((ny_x, ny_y))

print("Hei")


hindringer: list[Hindring] = []
tillatte_hindringer: list[Hindring] = [] # For at jeg ikke dør med en gang jeg spiser en matbit

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

    # spiller.oppdater()
    spiller.tekst_ramme.center = spiller.rect.center # Dette oppdaterer...

    spiller.sjekk_posisjon(BREDDE, HOYDE)

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
                # matbiter.append(Matbit(random.randint(30, BREDDE-30), random.randint(30, HOYDE-30)))
                ny_x, ny_y = Matbit.opprett_nytt_koordinat(matbitkoordinater)
                matbiter.append(Matbit(ny_x, ny_y))
                matbitkoordinater.append((ny_x, ny_y))

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
