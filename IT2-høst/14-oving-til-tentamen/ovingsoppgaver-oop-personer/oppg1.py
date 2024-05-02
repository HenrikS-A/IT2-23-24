
class Person:
    def __init__(self, navn: str, etternavn: str, fodselsaar: int):
        self.fornavn = navn
        self.etternavn = etternavn
        self.fodselsaar = fodselsaar

    def beregn_alder(self):
        return 2023 - self.fodselsaar
    
    def vis_info(self):
        print(f"Navn: {self.fornavn} {self.etternavn} \nAlder: {self.beregn_alder()}")


if __name__ == "__main__":
    # Denne koden kjører kun hvis vi trykker play på denne fila
    henrik = Person("Henrik", "Strøm-Andersen", 2005)
    henrik.vis_info()
    martin = Person("Martin", "Kaminski", 2005)
    martin.vis_info()
    person = Person("Hei", "På deg", 1492)
    person.vis_info()

