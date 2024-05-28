class Bruker:
    def __init__(self, fornavn: str, etternavn: str) -> None:
        self.fornavn = fornavn
        self.etternavn = etternavn
    def formelt(self):
        # Metode som retunerer etternavn, fornavn: eks: Coward, Thor Christian
        return f"{self.etternavn}, {self.fornavn}"
    def brukernavn(self):
        # metode som returnerer brukernavn, første del av fornavn pluss første
        # bokstav i etternavnet: eks: thorc
        return self.fornavn.lower() + self.etternavn.lower()[0]
    def mail(self, fylke: str):
        # metode som returnerer mail: brukernavn@fylke.no:
        # eks: thorc@akershus.no
        return f"{self.brukernavn()}@{fylke.lower()}.no"       # Her gjorde jeg endringer: lower fylke, endret til .no fra .com

class TestBruker:
    def __init__(self) -> None:
        self.bruker = Bruker("Henrik", "Strøm-Andersen")
    def test_formelt(self):
        assert self.bruker.formelt() == "Strøm-Andersen, Henrik", "Forventet resultat her er: 'Strøm-Andersen, Henrik'."
        print("Formelt metoden OK.")
    def test_brukernavn(self):
        assert self.bruker.brukernavn() == "henriks", "Forventet resultat her er: 'henriks'."
        print("Brukernavn metoden OK.")
    def test_mail(self):
        assert self.bruker.mail("Akershus") == "henriks@akershus.no", "Forventet resultat her er: 'henriks@akershus.no'."
        print("Mail metoden OK.")
    def kjor(self):
        print("-- Tester Bruker-klassen --")
        self.test_formelt()
        self.test_brukernavn()
        self.test_mail()
        print("-- Test fullført --")

brukertest = TestBruker()
brukertest.kjor()
