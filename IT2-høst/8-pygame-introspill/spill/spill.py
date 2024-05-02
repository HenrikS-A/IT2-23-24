import pygame

# 1. Oppsett
pygame.init()

BREDDE = 1280
HOYDE = 720
vindu = pygame.display.set_mode((BREDDE, HOYDE))

FPS = 60
klokke = pygame.time.Clock()

pygame.display.set_caption("Breaking Bad") # Navn på vinduet

overskrift_font = pygame.font.SysFont("Open Sans", 32) # Skrifttype
overskfrift_surface = overskrift_font.render("Breaking Bad", True, "black")

liv_font = pygame.font.SysFont("Open Sans", 28)

liv = 10
fiende_farge_endrer = 0
kollisjon = False

spiller_surface = pygame.image.load("bilder/walter-white.png").convert_alpha()
spiller_surface = pygame.transform.scale_by(spiller_surface, 0.2)
spiller_rect = spiller_surface.get_rect()
spiller_rect.top = 100
spiller_rect.centerx = BREDDE // 2
spiller_fart = 0

fiende_surface = pygame.image.load("bilder/gustavo-fring.png").convert_alpha()
fiende_surface = pygame.transform.scale_by(fiende_surface, 0.23)
fiende_rect = fiende_surface.get_rect()
fiende_rect.bottom = HOYDE - 10
fiende_rect.centerx = BREDDE // 2

meth_surface = pygame.image.load("bilder/crystal-meth.png").convert_alpha()
meth_surface = pygame.transform.scale_by(meth_surface, 0.2)
meth_rect = meth_surface.get_rect()
meth_rect.top = spiller_rect.bottom - 25
meth_rect.centerx = spiller_rect.centerx
meth_fart = 2


while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   # avslutter pygame
            raise SystemExit    # Avslutter løkka uten feilmelding
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spiller_fart = -5
            if event.key == pygame.K_RIGHT:
                spiller_fart = 5

        if event.type == pygame.KEYUP:
            spiller_fart = 0

    # 3. Oppdater spill
    fiende_rect.x -= 5
    if fiende_rect.right < 0:
        fiende_rect.left = BREDDE

    if spiller_rect.right < 0:
        spiller_rect.left = BREDDE
    elif spiller_rect.left > BREDDE:
        spiller_rect.right = 0

    spiller_rect.x += spiller_fart
    meth_rect.y += meth_fart

    if meth_rect.top > HOYDE:
        meth_rect.top = spiller_rect.bottom - 25
        meth_rect.centerx = spiller_rect.centerx
        meth_fart += 0.5
        kollisjon = False


    if fiende_rect.colliderect(meth_rect):
        if liv <= 0:
            pygame.quit()
            raise SystemExit
        else:
            fiende_farge_endrer = pygame.BLEND_RGB_SUB
        
        if not kollisjon:
            kollisjon = True # Setter verdien med en gang tilbake til True etter første gang den registrerer en kollisjon
            liv -= 1    # Da vil bare ett og ett liv fjernes om gangen

    else:
        fiende_farge_endrer = 0


    # 4. Tegn
    vindu.fill("white") # Fyller vinduet med hvit bakgrunn, for hver gang loopen kjører.
    vindu.blit(overskfrift_surface, (BREDDE//2 - overskfrift_surface.get_width()//2, HOYDE * 5/100)) # Tegner teksten i midten av x-posisjon og 10% ned fra toppen


    liv_surface = liv_font.render(f"Liv: {liv}", True, "black") # Jeg må lage surface-en her fordi jeg oppdaterer livene
    vindu.blit(liv_surface, (BREDDE - liv_surface.get_width() - 20, HOYDE * 5/100))

    ## Tegner spiller
    vindu.blit(spiller_surface, spiller_rect)

    ## Tegner fiende
    vindu.blit(fiende_surface, fiende_rect, None, fiende_farge_endrer)

    ## Tegner meth
    vindu.blit(meth_surface, meth_rect)     # , None, pygame.BLEND_RGB_SUB


    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
