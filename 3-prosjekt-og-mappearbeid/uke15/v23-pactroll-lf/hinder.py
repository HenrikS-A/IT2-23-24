from figur import Figur

class Hinder(Figur):
    def __init__(self, x:int, y:int):
        super().__init__(x, y, "gray")