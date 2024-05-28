import pygame
import time

# Klasser
class Spillobjekt:
    def __init__(self, bredde: int, farge: str, x: int, y: int):
        self.surface = pygame.Surface((bredde, bredde))
        self.rect = self.surface.get_rect()
        self.rect.center = (x, y)
        self.surface.fill(farge)

    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)

class Celle(Spillobjekt):
    def __init__(self, x: int, y: int):
        super().__init__(180, "white", x, y)
        self.ingen_eier = True

    def trykk(self, muspos: tuple[int, int], tur: int) -> int:
        if self.ingen_eier and self.rect.collidepoint(muspos):
                self.ingen_eier = False
                if tur == 0:
                    self.surface.fill("green")
                    return 1, True  # Endrer tur-en når det skjer en endring
                else:
                    self.surface.fill("red")
                    return 0, True # Endrer tur-en når det skjer en endring

        return tur, False # Returnerer tilbake tur hvis det ikke skjer et trykk


# Oppsett av pygame
pygame.init() 
BREDDE = 720
HOYDE = 720
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE)) 
klokke = pygame.time.Clock()
pygame.display.set_caption("Tre på rad") # Navn på vinduet

font = pygame.font.SysFont("Open Sans", 38) # Skrifttype



## Oppsett av spill
brett = Spillobjekt(620, "black", BREDDE//2, HOYDE//2)

celler = []
for i in range(3):
    for j in range(3):
        celler.append(Celle(160 + 200*j, 160 + 200*i))

spiller1_celler = []
spiller2_celler = []

tur = 0
mulige_seire = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
game_over = False
vinner = 0

# Gameloop
while True:
    # Håndter input:
    hendelser = pygame.event.get() 
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            pygame.quit() 
            raise SystemExit

        # NOTAT:
        if hendelse.type == pygame.MOUSEBUTTONDOWN: # Sjekker bare én gang når musen klikkes NED
            mus_posisjon = pygame.mouse.get_pos()
        # -----

    ## Input fra mus
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()
    if mus_klikk[0] and not game_over: # Sjekker etter venstreklikk, så lenge ingen har vunnet
        for i, celle in enumerate(celler):
            tur, endring = celle.trykk(mus_posisjon, tur)

            if endring and tur == 1: # Her må jeg tenke motsatt mtp. tur.
                spiller1_celler.append(i)
            elif endring and tur == 0: # Her må jeg tenke motsatt mtp. tur.
                spiller2_celler.append(i)


    # Oppdater spill
    
    ## Spillogikk
    if len(spiller1_celler) >= 3:
        for mulighet in mulige_seire:
            if all(nr in spiller1_celler for nr in mulighet): # Her sjekker jeg om ALLE tallene i hver mulighet også er i spillerens nummererte celler
                vinner = 1
                game_over = True
            elif all(nr in spiller2_celler for nr in mulighet):
                vinner = 2
                game_over = True


    # Tegn
    vindu.fill("white") # Fyller vinduet med en bakgrunnsfarge (fjerner alt fra forrige frame)

    brett.tegn(vindu)
    for celle in celler:
        celle.tegn(vindu)

    if tur == 0:
        farge = "grønn"
    else:
        farge = "rød"
    venter_tekst = font.render(f"Venter på {farge}", True, "black") # Oppretter tekst
    vindu.blit(venter_tekst, (BREDDE//2 - venter_tekst.get_width()//2, 10)) # Tegner teksten i midten av x-posisjon og 10% ned fra toppen

    if vinner > 0:
        pygame.draw.rect(vindu, "gray", (BREDDE//2 - 120, HOYDE//2 - 60, 240, 130)) # Tegner et rektangel
        vinner_tekst = font.render(f"Spiller {vinner} vant!", True, "black") # Oppretter tekst
        vindu.blit(vinner_tekst, (BREDDE//2 - vinner_tekst.get_width()//2, HOYDE//2 - vinner_tekst.get_height()//2)) # Tegner teksten i midten av x-posisjon og 10% ned fra toppen

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
