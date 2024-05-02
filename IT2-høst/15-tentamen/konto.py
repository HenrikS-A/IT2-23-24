class Konto:
    def __init__(self, kontonr: int, rente: float):
        self.kontonummer = kontonr
        self.saldo = 0.0
        self.rente = rente
    
    def print_info(self):
        print(f"Kontonr.: {self.kontonummer}, saldo: {self.saldo}, rente: {self.rente}.")
    
    def sett_inn(self, beløp):
        self.saldo += beløp

    def ta_ut(self, beløp):
        if self.saldo >= beløp:
            self.saldo -= beløp
        else:
            print("Feilmelding. Det er ikke nok penger på kontoen")
    
    def renteoppgjør(self):
        self.saldo += self.saldo * self.rente
    
    def overfør(self, beløp, annen_konto):
        if self.saldo >= beløp:
            self.saldo -= beløp
            annen_konto.saldo += beløp
        else:
            print("Feilmelding. Det er ikke nok penger på kontoen")

class Lønnskonto(Konto):
    def __init__(self, kontonr: int, rente=0.01):
        super().__init__(kontonr, rente)
        self.rente = 0.01
    
    def få_lønn(self):
        self.saldo += 30_000

class Sparekonto(Konto):
    def __init__(self, kontonr: int, rente=0.045):
        super().__init__(kontonr, rente)
        self.rente = 0.045
        self.antall_uttak = 0
    
    def ta_ut(self, beløp):
        if self.antall_uttak < 10:
            if self.saldo >= beløp:
                self.saldo -= beløp
                self.antall_uttak += 1
            else:
                print("Feilmelding. Det er ikke nok penger på kontoen")
        else:
            print("Du har tatt for mange uttak av sparekontoen. Du kan ikke ta ut mer penger.")

    def overfør(self, beløp, annen_konto):
        if self.antall_uttak < 10:
            super().overfør(beløp, annen_konto)
            self.antall_uttak += 1
        else:
            print("Du har overført for mange ganger fra sparekontoen. Du kan overføre mer penger.")



# Under har jeg gjort litt testing:

henriks_konto = Konto(930012340, 0.024)
henriks_lønnskonto = Lønnskonto(930012341)
henriks_sparekonto = Sparekonto(930012342)

henriks_konto.print_info()
henriks_lønnskonto.print_info()
henriks_sparekonto.print_info()

henriks_konto.sett_inn(1000)
henriks_lønnskonto.sett_inn(1000)
henriks_sparekonto.sett_inn(1000)

# henriks_konto.ta_ut(1001)
# henriks_lønnskonto.ta_ut(1000)
# henriks_sparekonto.ta_ut(500)

# henriks_konto.renteoppgjør()
# henriks_lønnskonto.renteoppgjør()
# henriks_sparekonto.renteoppgjør()

# henriks_konto.overfør(50, henriks_lønnskonto)
# henriks_lønnskonto.overfør(500000000, henriks_konto)
# henriks_sparekonto.overfør(300, henriks_konto)

henriks_lønnskonto.få_lønn()

for _ in range(9):
    henriks_sparekonto.overfør(25, henriks_konto)

for _ in range(2):
    henriks_sparekonto.ta_ut(25)

henriks_konto.print_info()
henriks_lønnskonto.print_info()
henriks_sparekonto.print_info()
