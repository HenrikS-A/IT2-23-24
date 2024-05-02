from figur import Figur

class Spiller(Figur):
    def __init__(self, x: int, y: int):
        super().__init__(100, 10, x, y)

    def flytt_venstre(self):
        self.rect.left -= 5
    
    def flytt_høyre(self):
        self.rect.left += 5
    