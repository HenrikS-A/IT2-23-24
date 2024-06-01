import pygame
from konstanter import * # importerer alle konstantene
from brikke import Brikke

def sjekk_vinner(brikker: list[Brikke]):
    # en funksjon som retunerer en farge hvis spillet har en vinner
    for i in range(3):
        if brikker[i*3].farge != "white" and brikker[i*3].farge == brikker[i*3+1].farge == brikker[i*3+2].farge:
            return brikker[i*3].farge
        if brikker[i].farge != "white" and brikker[i].farge == brikker[i+3].farge == brikker[i+6].farge:
            return brikker[i].farge
    if brikker[0].farge != "white" and brikker[0].farge == brikker[4].farge == brikker[8].farge:
        return brikker[0].farge
    if brikker[2].farge != "white" and brikker[2].farge == brikker[4].farge == brikker[6].farge:
        return brikker[2].farge
    return ""

# Oppsett av pygame
pygame.init()
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

# OPPSETT AV SPILL HER:
brikker = []
rundenummer = 0
timer = 0

for y in range(3):
    for x in range(3):
        brikker.append(Brikke(x, y, "white"))


while True:
    # fyll skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")

    # Hendelser
    for hendelse in pygame.event.get():
        # pygame.QUIT hendelsen skjer når brukeren klikke på X for å lukke vinduet
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Input fra mus:
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()
    if mus_klikk[0] and timer < 0:
        print(f"Venstre klikk i posisjon {mus_posisjon}")
        mus_x = mus_posisjon[0]
        mus_y = mus_posisjon[1]
        for brikke in brikker:
            if brikke.mus_klikket(mus_x, mus_y):
                if rundenummer % 2 == 0:
                    # partall
                    brikke.bytt_farge("green")
                else:
                    # oddetall
                    brikke.bytt_farge("red")
        rundenummer += 1
        timer = 60

    # Oppdater spill her:
    timer -= 1
    vinner = sjekk_vinner(brikker)
    if vinner == "red" or vinner == "green":
        print(f"{vinner} vant!")
        pygame.quit()
        raise SystemExit

    # Tegn på skjermen her:
    for brikke in brikker:
        brikke.tegn(vindu)


    # flip() oppdater vinduet med alle endringer
    pygame.display.flip()

    # klokke.tick(60) begrenser spillet til 60 FPS (frames per second)
    klokke.tick(60)
