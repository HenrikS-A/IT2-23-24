
# Type hinting er spesielle kommentarer som sier hvilken 
# datatype parametere skal ha og hvilken datatype funksjoner returnerer

# Fahrenheit :int sier at parameteren fahrenheit skal være et int
# -> float sier at funksjonen returnerer et float

def fahrenheit_til_celsius(fahrenheit: int) -> float:
    return (fahrenheit - 32) * (5/9)

print(fahrenheit_til_celsius(60))



# Docstrings er spesielle kommentarer som breskriver 
# en klasse, en funksjon eller et program. De skrives 
# mellom tre anførselstegn øvsert i klassen/funksjonen/programmet.

def celsius_til_fahrenheit(celsius: float) -> float:
    """
        En funksjon som konverterer celsius til fahrenheit.

        parametere
            celsius (float): antall grader i celsius
    """
    return (9/5) * (celsius + 32)

print(celsius_til_fahrenheit(2))


# Docstrings til en klasse
class Elev:
    """
    Klasse for en elev på VGS

    attributter
        navn (string): Navnet på eleven
        trinn (int): Klassetrinnet til eleven (eks: 3)
        klasse (string): Bokstavklassen til eleven (eks: STF)
        fag (list[str]): En liste med fag eleven tar

    metoder
        meld_opp_til_fag(fagnavn: str): Melder eleven opp til et fag
        dropp_ut_av_fag(fagnavn: str): Fjerner et fag fra elevens fagliste
    """
    def __init__(self, navn: str, trinn: int, klasse: str):
        self.navn = navn
        self.trinn = trinn
        self.klasse = klasse
        self.fag = []

    def meld_opp_til_fag(self, fagnavn: str):
        self.fag.append(fagnavn)

    def dropp_ut_av_fag(self, fagnavn: str):
        self.fag.remove(fagnavn)

henrik = Elev("Henrik", 3, "STF")
martin = Elev("Martin", 3, "STE")
