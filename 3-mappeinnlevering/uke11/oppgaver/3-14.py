
while True:
    navn = input("Skriv inn navnet ditt her: \n > ").lower()
    navn_liste = navn.split()
    if len(navn_liste) > 1:
        break
    print("Skriv minst to navn (fornavn + etternavn). Prøv på nytt")

mailadresse = navn_liste[0] + navn_liste [-1][0] + "@afk.no"
print(mailadresse)
