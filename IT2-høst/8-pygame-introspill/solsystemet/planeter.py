import pygame

class Planet:
    def __init__(self, x, y, r, planet_navn):
        self.x = x
        self.y = y
        self.radius = r
        self.surface = pygame.image.load(f"bilder/{planet_navn}.png").convert_alpha()
        self.surface = pygame.transform.scale(self.surface, ((self.radius*2, self.radius*2)))

    def tegn(self, vindu):
        # pygame.draw.circle(vindu, farge, (self.x, self.y), self.radius)
        vindu.blit(self.surface, (self.x, self.y))
        
    

# 1. Oppsett
pygame.init()

BREDDE = 1280
HOYDE = 720
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
pygame.display.set_caption("Solsystemet") # Navn på vinduet
klokke = pygame.time.Clock()

planeter = [
    Planet(100, 400, 2.4397, "mercury"),
    Planet(700, 400, 60.518, "venus"),
    Planet(200, 400, 63.71, "earth"),
    Planet(140, 400, 33.895, "mars"),
    Planet(500, 400, 69.911, "jupiter"),
    Planet(350, 400, 58.232, "saturn"),
    Planet(400, 400, 25.362, "uranus"),
    Planet(238, 400, 24.622, "neptune"),

    Planet(50, 400, 6963.40*0.01, "sun")
]


while True:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    # 3. Oppdater spill
    # 4. Tegn

    for planet in planeter:
        planet.tegn(vindu)



    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
