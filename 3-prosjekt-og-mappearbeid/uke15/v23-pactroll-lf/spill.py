import pygame

from hinder import Hinder
from matbit import Matbit
from troll import Troll
from hjelpefunksjoner import finn_unik_pos
 
# Oppsett av pygame
pygame.init()
BREDDE = 600 # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
poeng_font = pygame.freetype.SysFont("Arial", 50)
 
# OPPSETT AV SPILL HER:
poeng = 0
troll = Troll(BREDDE/2, HOYDE/2)
matbiter = []
hindere = []
for i in range(3):
    # bruker hjelpefunksjonen finn_unik_pos (se hjelpefunksjoner.py)
    # for å finne en posisjon som ikke er tatt:
    x, y = finn_unik_pos(BREDDE, HOYDE, matbiter, hindere, troll)
    matbiter.append(Matbit(x, y))

# hvis trollet spiser en matbit da gjøres matbiten om til et hinder
# for at trollet ikke sakl dø med en gang, så får trollet 2 sekunder
# fri før det dør hvis det overlapper med et hinder
fritid = 0 # trollet har ingen "fritid" i starten

while True:
    # fyll skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")
    
    # Hendelser
    for hendelse in pygame.event.get():
        # pygame.QUIT hendelsen skjer når brukeren klikke på X for å lukke vinduet
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
 
 
    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        troll.retning = (0, -1)
    if taster[pygame.K_DOWN]:
        troll.retning = (0, 1)
    if taster[pygame.K_LEFT]:
        troll.retning = (-1, 0)
    if taster[pygame.K_RIGHT]:
        troll.retning = (1, 0)
 
    # Oppdater spill:
    troll.oppdater_posisjon()

    # Sjekker om troll spiser en av matbitene:
    for matbit in matbiter:
        if troll.rect.colliderect(matbit.rect): # hvis troll og matbit overlapper:
            center_x = matbit.rect.centerx # hent x-koordinatet til matbiten
            center_y = matbit.rect.centery # hent y-koordinatet til matbiten
            hindere.append(Hinder(center_x, center_y)) # lag et nytt Hinder på samme sted
            matbiter.remove(matbit) # fjern matbiten
            x, y = finn_unik_pos(BREDDE, HOYDE, matbiter, hindere, troll)
            matbiter.append(Matbit(x, y)) # lag en ny matbit et annet sted
            troll.fart *= 1.1 # øker farten til trollet med 10%
            poeng += 1
            fritid = 120 # trollet får 2 sekunder fri

    fritid -= 1
    # Sjekker om troll er utenfor banen:
    if troll.rect.left < 0 or troll.rect.right > BREDDE or troll.rect.top < 0 or troll.rect.bottom > HOYDE:
        pygame.quit()
        raise SystemExit
    
    # Sjekker om troll kolliderer med et hinder:
    # skal bare sjekke hvis trollet ikke har "fritid":
    if fritid < 0:
        for hinder in hindere:
            if troll.rect.colliderect(hinder.rect):
                pygame.quit()
                raise SystemExit

    # Tegning:
    troll.tegn(vindu)
    for matbit in matbiter:
        matbit.tegn(vindu)
    for hinder in hindere:
        hinder.tegn(vindu)

    # Tegner tekst på skjermen:
    poeng_font.render_to(vindu, (10, 10), f'Poeng: {poeng}', "white")

    pygame.display.flip()
    klokke.tick(60) 
