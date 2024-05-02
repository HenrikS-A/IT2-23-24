import pygame


class Figur:
    def __init__(self, bildesti: str) -> None:
        self.bilde = pygame.image.load(bildesti).convert_alpha()
        self.ramme = self.bilde.get_rect()

    def tegn(self):
        vindu.blit(self.bilde, self.ramme)


