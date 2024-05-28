import pygame
from ballong import Ballong
from spiller import Spiller

BREDDE = 1280
HOYDE = 720
FPS = 60
ANTALL_BALLONGER_X = 15
ANTALL_BALLONGER_Y = 5

# Oppsett av pygame
pygame.init() 
vindu = pygame.display.set_mode((BREDDE, HOYDE)) 
klokke = pygame.time.Clock()

# Oppsett av spill
ny_ballong = Ballong(BREDDE//2, HOYDE - 50)
spiller = Spiller(BREDDE//2, HOYDE-100)

ballonger = []
for i in range(ANTALL_BALLONGER_Y):
    for j in range(ANTALL_BALLONGER_X):
        print(i, j)
        # Jeg bruker tall som gjør at det ser fint ut på min pc.
        ballonger.append(Ballong(j* ((BREDDE-50)//ANTALL_BALLONGER_X) + 66, 65 + i*75)) 

# Gameloop-en
while True:
    # Hendelser:
    hendelser = pygame.event.get() 
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            pygame.quit() # Avslutt spill
            raise SystemExit # Avslutt Python-programmet
        
    ## Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        spiller.flytt_venstre()
    if taster[pygame.K_RIGHT]:
        spiller.flytt_hoyre()
    if taster[pygame.K_SPACE]:
        ny_ballong.skyt()

    ny_ballong.oppdater_posisjon()
    for ballong in ballonger:
        if ny_ballong.rect.colliderect(ballong.rect):
            ny_ballong.stopp()
            ballonger.append(ny_ballong)
            ny_ballong = Ballong(BREDDE//2, HOYDE - 50)

    ## Input fra mus
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()

    if mus_klikk[0]:
        print(f"Venstreklikk i posisjon {mus_posisjon}")
    if mus_klikk[2]:
        print(f"Høyreklikk i posisjon {mus_posisjon}")
    

    # Oppdater spillogikk her (oppdater fart, sjekk kollisjoner osv.)


    # Tegn på vinduet
    vindu.fill("black") # Fyller vinduet med en bakgrunnsfarge(fjerner alt fra forrige frame)

    spiller.tegn(vindu)
    ny_ballong.tegn(vindu)
    for ballong in ballonger:
        ballong.tegn(vindu)

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
