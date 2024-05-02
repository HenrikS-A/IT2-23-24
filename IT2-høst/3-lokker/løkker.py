# Den naive (dumme) metoden
print("Mjau")
print("Mjau")
print("Mjau")


# While-løkke "klassikeren"
i = 0
while i <= 3:
    print("Mjau")
    i += 1


# For-løkke
for i in range(4):       # Se eks nedenfor!
    print("Mjau")

for _ in range(4):       # OBS!!!!! Hvis det er en variabel jeg ikke trenger så er det vanlig å skrive en understrek!!!
    print("Mjau")

for i in range(10):
    print("Mjau", "u" * i, "!", sep="")


# The pythonic way
print("hei\n" * 3, end="")



print("Hei", end="")
print("på deg!")