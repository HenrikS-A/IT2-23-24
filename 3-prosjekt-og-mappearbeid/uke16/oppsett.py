import pygame


# Oppsett av pygame:

pygame.init() # Laster inn alle spesielle variabler fra pygame
## Bredde og høyde til spill-vinduet
## STORE bokstaver betyr konstanter (endres ikke)
BREDDE = 1280
HOYDE = 720
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE)) # Slik vi oppretter et vindu
klokke = pygame.time.Clock()

# Oppsett av spill, f.eks. opprette spiller, hindere osv.



# Gameloop-en
while True:

    # Hendelser:
    hendelser = pygame.event.get() # En liste med alle hendelser som har skjedd (siden forrige frame?)
    for hendelse in hendelser:
        # Hvis brukeren trykker på X på spill-vinduet, så avslutter jeg
        if hendelse.type == pygame.QUIT:
            pygame.quit() # Avslutt spill
            raise SystemExit # Avslutt Python-programmet
        
    
    ## Input fra tastatur:

    # (Hvis jeg bare skal registrere ett trykk, 
    # kan jeg hente tastetrykk som en event i hendelser over!)

    # Jeg bruker ikke "elif" fordi da kan jeg ikke trykke på 2 knapper samtidig.
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        print("Du trykker på 'Pil opp'.")
    if taster[pygame.K_s]:
        print("Du trykker på 's'.")


    ## Input fra mus
    mus_posisjon = pygame.mouse.get_pos()
    mus_klikk = pygame.mouse.get_pressed()

    if mus_klikk[0]:
        print(f"Venstreklikk i posisjon {mus_posisjon}")
    if mus_klikk[2]:
        print(f"Høyreklikk i posisjon {mus_posisjon}")
    

    # Oppdater spillogikk her (oppdater fart, sjekk kollisjoner osv.)



    # Tegn på vinduet
    vindu.fill("white") # Fyller vinduet med en bakgrunnsfarge(fjerner alt fra forrige frame)

    pygame.display.flip() # Oppdaterer skjermen
    klokke.tick(FPS)
