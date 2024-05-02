elever = ["Harry", "Hermine", "Ronny", "Draco"]
hus = ["Griffing", "Griffing", "Griffing", "Smygard"]

# for elev in elever:
#     print(elev)
# for h in hus:
#     print(h)

for i in range(len(elever)):
    # i -> 0, 1, 2, 3
    print(f"{i + 1}: {elever[i]}, {hus[i]}")