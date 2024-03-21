# For å fikse opp:

def partall(tall: int):
    # En funksjon som tar in et heltall (int)
    # og returnerer True hvis tallet er et partall
    # og False hvis tallet er et oddetall
    if tall % 2 == 0:
        return True
    else:
        return False


# Testcaser som skal gi resultatene:
#print(partall(2))  -> True
#print(partall(3))  -> False


assert partall(2) == True
assert partall(3) == False
assert partall(-5) == False
assert partall(-2) == True

print("Alle tester: OK!")
