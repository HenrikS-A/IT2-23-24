import random

def finn_unik_pos(bredde, hoyde, matbiter, hindere, troll):
    # en funksjon som returnerer en posisjon som ikke allerede er tatt
    unik = False
    while not unik:
        unik = True
        x = random.randint(0, bredde)
        y = random.randint(0, hoyde)
        for matbit in matbiter:
            if matbit.rect.collidepoint(x, y):
                unik = False
        for hinder in hindere:
            if hinder.rect.collidepoint(x, y):
                unik = False
        if troll.rect.collidepoint(x, y):
            unik = False
    return x, y