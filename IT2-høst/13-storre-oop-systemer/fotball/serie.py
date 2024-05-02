from lag import Lag

class Serie():
    def __init__(self, navn: str) -> None:
        self.navn = navn
        self.lag: list[Lag] = []

    def hent_navn(self) -> str:
        return self.navn
    
    def hent_lagliste(self):
        return self.lag
    
    def legg_til_lag(self, lag):
        self.lag.append(lag)

    def spill_kamp(self, hjemmelag, bortelag, bortemål, hjemmemål):
        if hjemmemål > bortemål:
            return hjemmelag
        elif hjemmemål < bortemål:
            return bortelag
        elif hjemmemål == bortemål:
            return "uavgjort!"
        
    def finn_spiller(self, navn: str):
        for lag in self.lag:
            for spiller in lag.spillere:
                if navn in spiller.navn:
                    return spiller.navn
                return None
