elever = ["Harry", "Hermine", "Ronny"]

for elev in elever:
    print(elev)


# print(elever[0])
# print(elever[1])
# print(elever[2])

for i in range(len(elever)):
    # print(i + 1, elever[i], sep=": ")
    print(f"{i + 1}: {elever[i]}")

