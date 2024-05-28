import pygame

class Figur:
    def __init__(self, bredde: int, hoyde: int, x: int, y: int, farge: str) -> None:
        self.surface = pygame.Surface((bredde, hoyde))
        self.rect = self.surface.get_rect()
        self.rect.center = (x, y)
        self.surface.fill(farge)

    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)

