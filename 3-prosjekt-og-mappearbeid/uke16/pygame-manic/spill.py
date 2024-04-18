import pygame
from menneske import Menneske
from sau import Sau

# Oppsett av pygame
pygame.init() 
BREDDE = 1280
HOYDE = 720
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE)) 
klokke = pygame.time.Clock()

# Oppsett av spill, f.eks. opprette spiller, hindere osv.

spiller = Menneske()

sauer: list[Sau] = [Sau() for _ in range(3)] # med type-hints



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
    if taster[pygame.K_UP]:
        spiller.y_fart = -2
        spiller.x_fart = 0
    if taster[pygame.K_DOWN]:
        spiller.y_fart = 2
        spiller.x_fart = 0
    if taster[pygame.K_LEFT]:
        spiller.x_fart = -2
        spiller.y_fart = 0
    if taster[pygame.K_RIGHT]:
        spiller.x_fart = 2
        spiller.y_fart = 0


    ## Input fra mus
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()

    if mus_klikk[0]:
        print(f"Venstreklikk i posisjon {mus_posisjon}")
    if mus_klikk[2]:
        print(f"Høyreklikk i posisjon {mus_posisjon}")
    

    # Oppdater spillogikk her (oppdater fart, sjekk kollisjoner osv.)
    spiller.oppdater_posisjon()


    # Tegn på vinduet
    vindu.fill("white") # Fyller vinduet med en bakgrunnsfarge(fjerner alt fra forrige frame)

    spiller.tegn(vindu)

    for sau in sauer:
        sau.tegn(vindu)


    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
