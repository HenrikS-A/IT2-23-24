import pygame
from konstanter import *
from spiller import Spiller
from fiende import Fiende
from skudd import Skudd
from tekst import Tekst

pygame.init()
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

overskrift = Tekst("Subway surfer", BREDDE / 2, 20)
spiller = Spiller()
fiender = []
skuddliste: list[Skudd] = []
nivå = 0
timer_spiller = 0
timer_fiender = 1 * FPS * (1 - (nivå / 10))
timer_nivå = SEKUND_PER_NIVA * FPS
nivåtekst = Tekst(f"nivå: {nivå}", BREDDE - 70, 75)

while True:
    # fyller skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")

    # hendelser
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_LEFT]:
        if timer_spiller < 0:
            spiller.venstre()
            timer_spiller = 20
    if taster[pygame.K_RIGHT]:
        if timer_spiller < 0:
            spiller.høyre()
            timer_spiller = 20
    if taster[pygame.K_SPACE]:
        if timer_spiller < 0:
            skuddliste.append(Skudd(spiller.x, spiller.rect.top))
            timer_spiller = 20

    # oppdater spill:
    timer_spiller -= 1
    timer_fiender -= 1
    timer_nivå -= 1

    if timer_fiender < 0:
        fiender.append(Fiende())
        timer_fiender = 1 * FPS * (1 - (nivå / 10))

    if timer_nivå < 0:
        nivå += 1
        print(f"nytt nivå: {nivå}")
        timer_nivå = SEKUND_PER_NIVA * FPS
        nivåtekst.oppdater_tekst(f"nivå: {nivå}")

    for fiende in fiender:
        fiende.flytt()

    for skudd in skuddliste:
        skudd.flytt()

    if spiller.sjekk_kollisjon(fiender):
        pygame.quit()
        raise SystemExit

    skuddtreff = []
    for skudd in skuddliste:
        treff = skudd.sjekk_kollisjon(fiender)
        if treff:
            fiender.remove(treff)
            skuddtreff.append(skudd)

    for skudd in skuddtreff:
        skuddliste.remove(skudd)

    # tegning:
    for i in range(ANTALL_KOLONNER + 1):
        pygame.draw.line(vindu, "white", (MARG_VENSTRE + i * CELLEBREDDE,
                         MARG_TOPP), (MARG_VENSTRE + i * CELLEBREDDE, HOYDE))

    spiller.tegn(vindu)
    for fiende in fiender:
        fiende.tegn(vindu)

    for skudd in skuddliste:
        skudd.tegn(vindu)


    nivåtekst.tegn(vindu)

       

    pygame.display.flip()
    klokke.tick(FPS)
