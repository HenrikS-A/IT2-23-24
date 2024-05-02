def hallo(til): # definerer funksjonen hallo, med "til" som et parameter
    print("Hallo", til)

hallo("Henrik") # Funksjonskall, "Henrik" er et argument
hallo("Martin")


def heisann(*navn, avslutning): # definerer funksjonen heisann, med *navn som parameter 
    # (* betyr at den kan ta inn uendelig mange) og avslutning som "vanlig" parameter
    print("Hei", ", ".join(navn), avslutning)

heisann("Thor", "Henrik", "Martin", avslutning="og hele resten av verden!")