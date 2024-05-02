temp = float(input("Skriv inn kroppstemperaturen din her (punktum som komma): "))

if temp < 36.5:
    print("Du har kald temp.")
elif temp >= 36.5 and temp <= 37.5:
    print("Du har normal temperatur")
elif temp >= 37.5:
    print("Du har varm temp. Feber :(")
else:
    print("ERROR")