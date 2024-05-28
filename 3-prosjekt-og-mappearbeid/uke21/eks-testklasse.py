class Rektangel:
    def __init__(self, bredde: int, høyde: int) -> None:
        self.bredde = bredde
        self.høyde = høyde
    def areal(self):
        return self.bredde * self.høyde
    def omkrets(self):
        return 2 * self.bredde + 2 * self.høyde

class TestRektangel:
    def __init__(self) -> None:
        self.kvadrat = Rektangel(10, 10)
        self.vanlig = Rektangel(10, 5)
    def test_areal(self):
        assert self.kvadrat.areal() == 100, "Areal skal være 100"
        assert self.vanlig.areal() == 50, "Areal skal være 50"
        print("Areal OK!")
    def test_omkrets(self):
        assert self.kvadrat.omkrets() == 40, "Omkrets skal være 40"
        assert self.vanlig.omkrets() == 30, "Omkrets skal være 30"
        print("Omkrets OK!")
    def kjør(self):
        print("-- tester Rektangel --")
        self.test_areal()
        self.test_omkrets()
        print("-- test ferdig --")
test = TestRektangel()
test.kjør()
