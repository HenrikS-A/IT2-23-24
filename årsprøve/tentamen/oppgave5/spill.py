import pygame


# Klasser
class Spillobjekt:
    def __init__(self, bredde: int, hoyde: int, x: int, y: int) -> None:
        self.surface = pygame.Surface((bredde, hoyde))
        self.rect = self.surface.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.surface.fill("white")

    def tegn(self, vindu: pygame.Surface):
        vindu.blit(self.surface, self.rect)


class Racket(Spillobjekt):
    def __init__(self) -> None:
        super().__init__(70, 15, BREDDE//2, HOYDE*0.9)
        self.spillerfart = 5
        self.niva = 1
        self.poeng = 0

    def beveg(self, tastaturinput):
        if tastaturinput[pygame.K_d] and self.rect.right < BREDDE:
            self.rect.centerx += self.spillerfart
        if tastaturinput[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= self.spillerfart
    
    def oek_spillerniva(self):
        self.niva += 1

    def oek_poeng(self):
        self.poeng += 1

    def sjekk_oeke_niva(self, murliste):
        if len(murliste) % 5 == 0:
            return True
        return False
    
    def vis_info(self, vindu: pygame.Surface, skjerm_bredde, skjerm_hoyde):
        info_font = pygame.font.SysFont("Open Sans", 60)

        niva_surface = info_font.render(f"{self.niva}", True, "white")
        vindu.blit(niva_surface, (skjerm_bredde * 94/100, skjerm_hoyde * 4/100))

        poeng_surface = info_font.render(f"{self.poeng}", True, "white")
        vindu.blit(poeng_surface, (skjerm_bredde * 6/100, skjerm_hoyde * 4/100))


class Ball(Spillobjekt):
    def __init__(self) -> None:
        super().__init__(10, 10, BREDDE//2 - 100, HOYDE//2)
        self.ballfart = 2
        self.x_fart = self.ballfart
        self.y_fart = self.ballfart
    
    def beveg(self):
        if self.rect.right >= BREDDE:
            self.x_fart = -self.ballfart
        if self.rect.left <= 0:
            self.x_fart = self.ballfart
        if self.rect.top <= 0:
            self.y_fart = self.ballfart

        self.rect.centerx += self.x_fart
        self.rect.centery += self.y_fart

    def spiller_kollisjon(self):
        self.y_fart = -self.ballfart

    def blokk_kollisjon(self, index: int, mur_liste: list):
        if index != -1:
            mur_liste.pop(index)
            self.y_fart = self.ballfart

            return True
        return False
    
    def sjekk_spill_over(self, mur_liste):
        if self.rect.bottom >= HOYDE or len(mur_liste) == 0:
            pygame.quit() # Avslutt spill
            raise SystemExit # Avslutt Python-programmet
        
    def oek_fart(self):
        self.ballfart += 2


class Murblokk(Spillobjekt):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(60, 15, x, y)



# Oppsett av Pygame
pygame.init()
BREDDE = 780
HOYDE = 720
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
pygame.display.set_caption("Breakout") # Navn på vinduet 


## Oppsett av spill
spiller = Racket()
ball = Ball()


murrad1 = []
murrad2 = []
murrad3 = []

for i in range(5):
    venstre = Murblokk(BREDDE//2 - (i*75) - 38, 100)
    hoyre = Murblokk(BREDDE//2 + (i*75) + 38, 100)

    murrad1.append(venstre)
    murrad1.append(hoyre)

for i in range(5):
    venstre = Murblokk(BREDDE//2 - (i*75) - 38, 150)
    hoyre = Murblokk(BREDDE//2 + (i*75) + 38, 150)

    murrad2.append(venstre)
    murrad2.append(hoyre)

for i in range(5):
    venstre = Murblokk(BREDDE//2 - (i*75) - 38, 200)
    hoyre = Murblokk(BREDDE//2 + (i*75) + 38, 200)

    murrad3.append(venstre)
    murrad3.append(hoyre)

# Slår sammen alle mur-rad-listene til én liste med bare Murblokk-objekter
mur = [*murrad1, *murrad2, *murrad3]



while True:
    # Håndter input:
    hendelser = pygame.event.get() 
    for hendelse in hendelser:
        if hendelse.type == pygame.QUIT:
            pygame.quit() # Avslutt spill
            raise SystemExit # Avslutt Python-programmet
        
    ## Input fra tastatur:
    taster = pygame.key.get_pressed()

    # Oppdater spill
    spiller.beveg(taster)
    ball.beveg()
    ball.sjekk_spill_over(mur)
    

    ## Kollisjoner
    if ball.rect.colliderect(spiller.rect):
        ball.spiller_kollisjon()

    mur_kollisjon_index = ball.rect.collidelist([blokk.rect for blokk in mur])
    kollisjon = ball.blokk_kollisjon(mur_kollisjon_index, mur)
    
    if kollisjon:
        spiller.oek_poeng()

        oeke_niva = spiller.sjekk_oeke_niva(mur)
        if oeke_niva:
            spiller.oek_spillerniva()
            ball.oek_fart()


    # Tegn
    vindu.fill("black")

    spiller.vis_info(vindu, BREDDE, HOYDE)

    spiller.tegn(vindu)
    ball.tegn(vindu)

    for murblokk in mur:
        murblokk.tegn(vindu)

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
