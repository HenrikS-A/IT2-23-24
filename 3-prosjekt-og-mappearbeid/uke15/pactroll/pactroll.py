import pygame
import random

# Klasser
class Objekt:
    def __init__(self, x: int, y: int, tekst: str):
        self.sidelengde = 60
        self.rect = pygame.Rect(self.sidelengde, self.sidelengde, self.sidelengde, self.sidelengde)
        self.rect.centerx = x
        self.rect.centery = y
        self.farge = "yellow"

        # Til teksten:
        self.fonten = pygame.font.SysFont("Open Sans", 50) # Skrift font
        self.tekst = self.fonten.render(tekst, True, "black") # Selve teksten
        self.tekst_ramme = self.tekst.get_rect() # Henter rammen rundt teksten
        self.tekst_ramme.center = self.rect.center # Plasserer sentrum av tekst-rammen på samme pos. som sentrum til rektangelet.

    def oppdater(self):
        self.tekst_ramme.center = self.rect.center

    def tegn(self, vindu):
        pygame.draw.rect(vindu, self.farge, self.rect)
        vindu.blit(self.tekst, (self.tekst_ramme))



class Troll(Objekt):
    def __init__(self, x: int, y: int, tekst: str):
        super().__init__(x, y, tekst)
        self.farge = "green" # Overskriver fargen.
        self.spillerfart = 1 # Konstant fart hele tiden
        self.retning = random.randint(1, 4) # Jeg velger en tilfeldig retning.
        
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
    def __init__(self, x: int, y: int, tekst: str):
        super().__init__(x, y, tekst)


class Hindring(Objekt):
    def __init__(self, x: int, y: int, tekst: str):
        super().__init__(x, y, tekst)
        self.farge = "gray"




# 1. Oppsett
pygame.init()

BREDDE = 1280
HOYDE = 720
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

pygame.display.set_caption("Pactroll") # Navn på vinduet
font = pygame.font.SysFont("Open Sans", 24) # Skrifttype



spiller = Troll(BREDDE//2, HOYDE//2, "T")


matbiter = []
for _ in range(3):
    matbiter.append(Matbit(random.randint(10, BREDDE-10), random.randint(10, HOYDE-10), "M"))


hindringer = []





# For at jeg ikke dør med en gang jeg spiser en matbit
tillatte_hindringer = []



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



    for i in range(len(matbiter)):
        if spiller.rect.colliderect(matbiter[i].rect):
            print("HALLLLLOO")


            ny_hindring = Hindring(matbiter[i].rect.centerx, matbiter[i].rect.centery, "H")

            hindringer.append(ny_hindring)
            tillatte_hindringer.append(ny_hindring)

            # Jeg legger bare en hindring rett over matbiten, jeg fjerner ikke matbit.
        
    if spiller.rect.collidelist([bit.rect for bit in matbiter]):
        print("HADE")
        tillatte_hindringer.clear() # Fjerner alt fra lista!

    for i in range(len(hindringer)):
        if spiller.rect.colliderect(hindringer[i].rect) and hindringer[i] not in tillatte_hindringer:


            

            print("AHAHAHAHAHHAHAHAHAHAHAHAAAAAAA")

            pygame.quit()
            raise SystemExit










    # 4. Tegn

    vindu.fill("black") # Fyller vinduet med sort bakgrunn, for hver gang loopen kjører.

    # tekst_hallo = font.render("Hallo på deg!", True, "black") # Oppretter tekst
    # vindu.blit(tekst_hallo, (BREDDE//2 - tekst_hallo.get_width()//2, HOYDE * 10/100)) # Tegner teksten i midten av x-posisjon og 10% ned fra toppen



    for matbit in matbiter:
        matbit.tegn(vindu)
    
    for hindring in hindringer:
        hindring.tegn(vindu)

    spiller.tegn(vindu)


    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
