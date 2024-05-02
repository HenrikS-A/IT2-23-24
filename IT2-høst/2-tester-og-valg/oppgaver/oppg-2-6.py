# d1 = input("Skriv inn dag: ")
# m1 = input("Skriv inn måned: ")
# print(f"Første datoen er: {d1}.{m1}")

# d2 = input("Skriv inn dag: ")
# m2 = input("Skriv inn måned: ")
# print(f"Andre datoen er: {d2}.{m2}")

# if m1 < m2:
#     print("Riktig rekkefølge!")
# elif m1 > m2:
#     print("Feil rekkefølge")
# elif m1 == m2:
#     if d1 < d2:
#         print("Riktig rekkefølge")
#     elif d1 > d2:
#         print("Feil rekkefølge")
#     elif d1 == d2:
#         print("Samme dato!")


print("Skriv inn dato slik: dd/mm, eks: 1/9")

dato_1 = input("Dato 1: ")
d1, m1 = dato_1.split("/")

print(f"Første datoen er: {d1}.{m1}\n")

dato_2 = input("Dato 2: ")
d2, m2 = dato_2.split("/")

print(f"Andre datoen er: {d2}.{m2}\n")


if m1 < m2:
    print("Riktig rekkefølge!")
elif m1 > m2:
    print("Feil rekkefølge")
elif m1 == m2:
    if d1 < d2:
        print("Riktig rekkefølge")
    elif d1 > d2:
        print("Feil rekkefølge")
    elif d1 == d2:
        print("Samme dato!")
