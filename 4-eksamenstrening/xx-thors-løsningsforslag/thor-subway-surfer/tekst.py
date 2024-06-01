import pygame

class Tekst:
    def __init__(self, tekst, x, y) -> None:
        self.font = pygame.font.SysFont("Arial", 32)
        self.surface = self.font.render(tekst, True, "white")
        self.rect = self.surface.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)

    def oppdater_tekst(self, tekst):
        self.surface = self.font.render(tekst, True, "white")
        self.rect = self.surface.get_rect()
        self.rect.center = (self.x, self.y)

    def tegn(self, surface):
        surface.blit(self.surface, self.rect)
