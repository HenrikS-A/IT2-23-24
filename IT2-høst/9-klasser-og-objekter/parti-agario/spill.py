import pygame, random

# Klasser
class Matbit:
    def __init__(self):
        self.bilde = pygame.image.load("bilder/stemme.png").convert_alpha()
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = random.randint(0, BREDDE)
        self.ramme.centery = random.randint(0, HOYDE)

    def tegn(self, vindu):
        vindu.blit(self.bilde, self.ramme)

class Celle:
    def __init__(self, navn: str, radius: int, bildeurl: str, x: int, y: int, farge: str):
        self.navn = navn
        self.radius = radius
        self.bilde_original = pygame.image.load(bildeurl).convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde_original, (2 * self.radius, 2 * self.radius))
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = x
        self.ramme.centery = y
        self.farge = farge

    def beveg(self, mus_x: int, mus_y: int):
        if mus_x > self.ramme.centerx:
            self.ramme.centerx += 1
        elif mus_x < self.ramme.centerx:
            self.ramme.centerx -= 1

        if mus_y > self.ramme.centery:
            self.ramme.centery += 1
        elif mus_y < self.ramme.centery:
            self.ramme.centery -= 1
    
    def spis(self, motspiller=None):
        print("SPIS!")

        if motspiller:
            self.radius += motspiller.radius
        else:
            self.radius += 1
        
        self.oppdater_bilde()

    def bli_spist(self):
        self.radius = 10
        self.oppdater_bilde()

    def oppdater_bilde(self):
        self.bilde = pygame.transform.scale(self.bilde_original, (2 * self.radius, 2 * self.radius))
        gammel_x = self.ramme.centerx
        gammel_y = self.ramme.centery
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = gammel_x
        self.ramme.centery = gammel_y

    def tegn(self, vindu):
        pygame.draw.circle(vindu, self.farge, (self.ramme.centerx, self.ramme.centery), self.radius + 4)
        vindu.blit(self.bilde, self.ramme)



# 1. Oppsett
pygame.init()

BREDDE = 1280
HOYDE = 720
FPS = 60

vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
pygame.display.set_caption("Parti Agario") # Navn på vinduet



spiller = Celle("AP", 50, "bilder/jonas.png", 100, 200, "red")

motspillere = [
    Celle("SV", 25, "bilder/kirsti.png", 500, 400, "purple"),
    Celle("Høyre", 100, "bilder/erna.png", 50, 400, "blue"),
    Celle("FrP", 75, "bilder/sylvi.png", 400, 300, "darkblue")
]

matbiter = []
for _ in range(10):
    matbiter.append(Matbit())



while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    mus_x, mus_y = pygame.mouse.get_pos()

    # 3. Oppdater spill
    spiller.beveg(mus_x, mus_y)

    for i in range(len(motspillere) - 1, -1, -1):
        if spiller.ramme.colliderect(motspillere[i].ramme):
            if spiller.radius > motspillere[i].radius:
                print("SPIS motspiller!!")
                spiller.spis(motspillere[i])
                motspillere.pop(i) 

            elif spiller.radius < motspillere[i].radius:
                print("Bli spist")
                spiller.bli_spist()

    for i in range(len(matbiter) - 1, -1, -1):
        if spiller.ramme.colliderect(matbiter[i].ramme):
            spiller.spis()
            matbiter.pop(i)
    

    # 4. Tegn
    vindu.fill("white") # Fyller vinduet med hvit bakgrunn, for hver gang loopen kjører.

    spiller.tegn(vindu)
    
    for motspiller in motspillere:
        motspiller.tegn(vindu)

    for matbit in matbiter:
        matbit.tegn(vindu)



    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
