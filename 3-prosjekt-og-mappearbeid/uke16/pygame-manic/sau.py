import random
from figur import Figur

class Sau(Figur):
    def __init__(self) -> None:
        super().__init__(1230, random.randint(100, 600), "yellow")
