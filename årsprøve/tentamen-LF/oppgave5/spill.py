import pygame
from spiller import Spiller
from blokk import Blokk
from ball import Ball
 
# Oppsett av pygame
pygame.init()
BREDDE = 600 # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
kjorer = True
font = pygame.font.SysFont("Arial", 50)

# OPPSETT AV SPILL HER:
poeng = 0
nivå = 1
nivåpoeng = 0
ballpoeng = 0
spiller = Spiller(BREDDE / 2, HOYDE - 20)
baller = [Ball(BREDDE / 2, HOYDE / 2)]
blokker = []
for i in range(3):
    for j in range(10):
        blokker.append(Blokk(j * (BREDDE / 10) + ((BREDDE / 10) / 2), i * 30 + 100))
 
while kjorer:
    # fyll skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")
    
    # Hendelser
    for hendelse in pygame.event.get():
        # pygame.QUIT hendelsen skjer når brukeren klikke på X for å lukke vinduet
        if hendelse.type == pygame.QUIT:
            kjorer = False
 
    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        spiller.flytt_venstre()
    if taster[pygame.K_RIGHT]:
        spiller.flytt_høyre()
 
    # Oppdater spill her:
    for ball in baller:
        ball.oppdater_posisjon(BREDDE, HOYDE)
        
        if spiller.rect.colliderect(ball.rect):
            ball.snu_y() 

        for blokk in blokker:
            if ball.rect.colliderect(blokk):
                blokker.remove(blokk)
                ball.snu_y()
                poeng += 1
                nivåpoeng += 1
                ballpoeng += 1
                if ballpoeng == 10:
                    ny_ball = Ball(ball.rect.centerx, ball.rect.centery)
                    ny_ball.rect.center = ball.rect.center
                    ny_ball.x_fart = -ball.x_fart
                    ny_ball.y_fart = -ball.y_fart
                    baller.append(ny_ball)
                    ballpoeng = 0
            
        if ball.rect.top > HOYDE:
            baller.remove(ball)

    if nivåpoeng == 5:
        nivå += 1
        ball.x_fart *= 1.1
        ball.y_fart *= 1.1          
        nivåpoeng = 0
    
    if len(baller) == 0 or len(blokker) == 0:
        pygame.quit()
        raise SystemExit
 
    # Tegn på skjermen her:
    spiller.tegn(vindu)
    for ball in baller:
        ball.tegn(vindu)
    for blokk in blokker:
        blokk.tegn(vindu)
    
    poengtekst = font.render(str(poeng), True, "white")
    vindu.blit(poengtekst, (25, 10))
    nivåtekst = font.render(str(nivå), True, "white")
    vindu.blit(nivåtekst, (BREDDE - 50, 10))

    pygame.display.flip()
    klokke.tick(60) 
 
pygame.quit()