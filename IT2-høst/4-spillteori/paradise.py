import random

def main():
    print("Velkommen til Troskapstesten!")

    spiller_1_gevinst = 0
    spiller_2_gevinst = 0

    for i in range(1000):   # spiller 1000 troskapstester
        spiller_1_rundegevinst, spiller_2_rundegevinst = spill(spiller_tilfeldig, spiller_halvveis)
        spiller_1_gevinst += spiller_1_rundegevinst
        spiller_2_gevinst += spiller_2_rundegevinst

    print(f"\nSpiller 1: {spiller_1_gevinst /1000}")
    print(f"Spiller 2: {spiller_2_gevinst /1000}")
        



def spiller_snill(belop: int) -> str:
    return "behold"

def spiller_slem(belop):
    return "kast"

def spiller_halvveis(belop):
    if belop >= 150_000:
        return "kast"
    else:
        return "behold"

def spiller_tilfeldig(belop):
    tilfeldig_tall = random.randint(1, 100)
    if tilfeldig_tall <= 50:
        return "kast"
    else:
        return "behold"


def spill(spiller_1_strategi, spiller_2_strategi) -> list[int]:
    pengepott = 0

    for i in range(30):
        pengepott += 10_000
        print(f"\nRunde {i + 1}: {pengepott},-")

        valg_spiller_1 = spiller_1_strategi(pengepott)
        print(f"Spiller 1: {valg_spiller_1}")

        valg_spiller_2 = spiller_2_strategi(pengepott)
        print(f"Spiller 2: {valg_spiller_2}")


        if valg_spiller_1 == "kast" and valg_spiller_2 == "kast":
            return [pengepott / 2, pengepott / 2]

        if valg_spiller_1 == "kast":
            print(f"\nSpiller 1 vant! Gevinsten ble: {pengepott},-")
            print("- Spillet er over -")
            return [pengepott, 0]
        elif valg_spiller_2 == "kast":
            print(f"\nSpiller 2 vant! Gevinsten ble: {pengepott},-")
            print("- Spillet er over -")
            return [0, pengepott]


main()
