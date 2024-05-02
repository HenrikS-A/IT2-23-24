print("Hallo, verden!") # print er en innebygd funksjon i python, "Hallo, verden!" er ... 
# ... et argument som forteller datamaskinen hva vi vil printe

navn = input("Hva heter du? ") # input funksjonen returnerer det brukeren skriver i terminalen
print(f"Hei, {navn}")

# print-funksjonen kan ta inn uendelig mange argumenter, og den kan ta inn nøkkelordargumenter som sep og end.
print("Hei", navn, sep="???", end="Heisann\n") 
# Noen interessante greier, end er til vanlig \n, for å få ny linje må vi legge det inn manuelt
print("test")

