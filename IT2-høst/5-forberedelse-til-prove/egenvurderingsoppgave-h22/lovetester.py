match = 0

# Alder beregning
navn_person1 = input("Skriv inn navnet på person 1: ").lower()
navn_person2 = input("Skriv inn navnet på person 2: ").lower()

if len(navn_person1) == len(navn_person2):
    match = 0.6
elif navn_person1[0] == navn_person2[0]:
    match = 0.4
else:
    match = 0.15


# Bosted beregning
bosted_person1 = input("Skriv inn bosted til person 1: ").lower()
bosted_person2 = input("Skriv inn bosted til person 2: ").lower()

if bosted_person1 == bosted_person2:
    match *= 1.5


# Alder beregning
alder_person1 = int(input("Skriv inn alder til person 1: "))
alder_person2 = int(input("Skriv inn alder til person 2: "))

if alder_person1 == (alder_person2 / 2) + 7 or alder_person2 == (alder_person1 / 2) + 7:
    match /= 2


# Hemmelige faktorer
if "a" in navn_person1 or "t" in navn_person1 or "a" in navn_person2 or "t" in navn_person2:
    match += 0.02

elif ("s" in navn_person1 and "e" in navn_person1 and "e" not in navn_person2) or ("s" in navn_person2 and "e" in navn_person2 and "e" not in navn_person1):
    match += 0.15

elif navn_person1[0] not in navn_person2:
    match -= 0.2

elif ( navn_person1[-1] == navn_person2[0] ) or ( navn_person2[-1] == navn_person1[0] ):
    match += 0.3


# Siste detaljer
if len(navn_person1) == 1 or len(navn_person2) == 1:
    match = 0

if match > 1:
    match = 1
elif match < 0:
    match = 0

# Printer ut match-prosenten
print(f"{navn_person1.capitalize()} og {navn_person2.capitalize()} har en match-prosent på: {round(match*100, 1)}%")