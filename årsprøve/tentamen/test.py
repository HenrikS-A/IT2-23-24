# tall = 8

# if tall < 4:
#     if tall > 7:
#         print("linje 5 kjører")
# elif tall < 10:
#     print("linje 7 kjører")
# elif tall > 100:
#     print("Linje 9 kjører")
# else:
#     print("linje 11 kjører")


class Info:
    def __init__(self, fornavn, etternavn) -> None:
        self.navn = f"{fornavn} {etternavn}"


helt = Info("Espen", "Askeladd")

print("Test")
