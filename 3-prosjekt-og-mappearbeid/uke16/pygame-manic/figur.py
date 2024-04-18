import pygame

class Figur:
    def __init__(self, x: int, y: int, farge: str) -> None:
        # oppretter et pygame Surface med bredde 50 og høyde 50
        self.surface = pygame.Surface((50, 50))
        # oppretter en pygame Rect "rundt" surface-en
        self.rect = self.surface.get_rect()

        # Plasserer figuren i posisjonen (x, y)
        self.rect.center = (x, y)

        # Fyller surface-en til figuren med en farge
        self.surface.fill(farge)

    def tegn(self, surface: pygame.Surface):
        # putter figuren på en annen surface
        surface.blit(self.surface, self.rect)
