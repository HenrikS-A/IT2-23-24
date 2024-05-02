# antall = int(input("Hvor mange katter har du?"))


while True:
    antall = input("Hvor mange katter har du?")
    er_tall = antall.isnumeric()
    antall = int(antall)
    
    if not er_tall and antall < 0:
        continue
    else:
        break


for _ in range(antall):
    print("Mjau!")