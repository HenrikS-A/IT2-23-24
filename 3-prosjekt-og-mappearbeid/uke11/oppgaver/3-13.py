
while True:                                             # infinite while-loop starter (helt til den brytes ut)
    try:                                                # Først skal jeg prøve det som står innenfor "try"
        alder = int(input("Hvor gammel er du? "))           # Alder tar inn et input som bare kan være datatypen int.
        break                                               # Hvis linjen over skjer uten feilmelding, 
                                                            # så bryter vi ut av while-loopen og vi fortsetter på linje 8
    except:                                             # Hvis "try" gir en feil-melding, så skal det innenfor "except" kjøre
        print("Ugyldig input. Alder må være et tall.")      # Her printes det ut en melding og while-loopen begynner på start.
år = 2024                                               # År settes til 2024
fødselsår = år - alder                                  # Fødselsår beregnes
print(f"Du er født i {fødselsår}")                      # Det printes ut en melding som sier fødselsåret du er født i.
