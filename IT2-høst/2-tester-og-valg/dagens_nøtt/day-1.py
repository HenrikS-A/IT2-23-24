fil = open("day-1-input.txt", "r") # Leser input filen
data = fil.read()

alvene = data.split("\n\n") # splitter opp alvene

# Lager liste i liste med bare kalorier
alvene_kalorier = []
for alv in alvene:
    alv = alv.split("\n")

    alvene_kalorier.append(alv)

# Legger inn i ny liste der alt er integers
int_alvene_kalorier = []
for alv in alvene_kalorier:
    alv = [int(kalori) for kalori in alv] # gjør om alt om til int, går gjennom én og én alv av gangen
    int_alvene_kalorier.append(alv)

# går gjennom listen og lagrer den høyeste summen i en variabel, den blir oppdatert

hoeyeste_kaloritall = 0
for i in range(len(int_alvene_kalorier)):
    kalori_sum = sum(int_alvene_kalorier[i])
    if kalori_sum > hoeyeste_kaloritall:
        hoeyeste_kaloritall = kalori_sum

print(hoeyeste_kaloritall)





# lager ny liste med bare alle summene

alver_totalkalorier_summert = []
for i in range(len(int_alvene_kalorier)):
    kalori_sum = sum(int_alvene_kalorier[i])
    alver_totalkalorier_summert.append(kalori_sum)


tre_hoyeste_kalorisummer = []

while len(tre_hoyeste_kalorisummer) < 3:
    hoeyeste_kaloritall = 0

    for kalori_sum in alver_totalkalorier_summert:
        if kalori_sum > hoeyeste_kaloritall:
            hoeyeste_kaloritall = kalori_sum

    tre_hoyeste_kalorisummer.append(hoeyeste_kaloritall)

    alver_totalkalorier_summert.remove(hoeyeste_kaloritall)


print(tre_hoyeste_kalorisummer)
print(sum(tre_hoyeste_kalorisummer))




