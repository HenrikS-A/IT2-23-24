def partall(tall: int):
    # En funksjon som tar in et heltall (int)
    # og returnerer True hvis tallet er et partall
    # og False hvis tallet er et oddetall
    return True


# Testcaser som skal gi resultatene:
#print(partall(2))  -> True
#print(partall(3))  -> False


assert partall(2) == True

# Denne gir en AssertionError. Koden gjør ikke det jeg vil. Programmet avslutter som en 'forsikring'
assert partall(3) == False, "3 er ikke et partall"

print("Alle tester: OK!")
