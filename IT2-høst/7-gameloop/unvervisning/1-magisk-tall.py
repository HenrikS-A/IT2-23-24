import random
# Magisk tall - et spill hvor brukeren skal gjette hvilket tall datamaskinen tenker på

# 1. Oppsett
magisk_tall = random.randint(1, 10)
antall_forsok = 0

while True:
    # 2. Håndter input
    brukerinput = input("Hva er det magiske tallet?\n > ")
    if brukerinput == "avslutt":
        break
    
    tall = int(brukerinput)

    # 3. Oppdater spill
    antall_forsok += 1

    # 4. Tegn (print)
    if tall > magisk_tall:
        print("For høyt")
    elif tall < magisk_tall:
        print("For lavt")
    else: 
        print(f"Riktig! Du brukte {antall_forsok} forsøk.")
        break
