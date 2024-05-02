fullt_navn = input("Skriv inn navnet ditt\n> ")

navn = fullt_navn.split()

for i in range(len(navn)):
    print(navn[i][0].upper(), end="")
print("") # For å fjerne % som betyr at jeg ikke har new-line på slutten. Gjør det bare finere.