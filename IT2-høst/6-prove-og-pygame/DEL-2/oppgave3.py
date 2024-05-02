passord = input("Skriv inn passordet ditt\n> ")


# Startverdier for variablene jeg skal sjekke
tall = False
spesialtegn = False
liten_bokstav = False
stor_bokstav = False


# Sjekker kriterier og setter variablene over til True hvis kriteriet stemmer
for i in range(len(passord)):
    if passord[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        tall = True
    
    if passord[i] in ["$", "#", "@", "?", "%", "&", "!"]:
        spesialtegn = True

    if passord[i].islower():
        liten_bokstav = True

    if passord[i].isupper():
        stor_bokstav = True


# Printer ut om passordene er godkjent eller ikke.
if len(passord) < 6:
    print("Ikke godkjent. \nPassordet må ha minimum 6 tegn.")
elif len(passord) > 16:
    print("Ikke godkjent. \nPassordet kan maks ha 16 tegn.")
elif tall == False:
    print("Ikke godkjent. \nPassordet må ha ett tall mellom 1 og 9.")
elif spesialtegn == False:
    print("Ikke godkjent. \nPassordet må ha minst ett spesialtegn ($, #, @, ?, %, &, !).")
elif liten_bokstav == False:
    print("Ikke godkjent. \nPassordet må ha minst én liten bokstav.")
elif stor_bokstav == False:
    print("Ikke godkjent. \nPassordet må ha minst én stor bokstav.")
else:
    print("Passordet er godkjent.")