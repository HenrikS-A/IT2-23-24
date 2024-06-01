import pygame
from konstanter import *

class Brikke:
    def __init__(self, x: int, y: int, farge: str) -> None:
        self.x = x
        self.y = y
        self.farge = farge
        self.surface = pygame.Surface((CELLEBREDDE, CELLEBREDDE))
        self.rect = self.surface.get_rect()
        self.rect.left = self.x * (CELLEBREDDE + MARG)
        self.rect.top = self.y * (CELLEBREDDE + MARG)
        self.surface.fill(farge)

    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)
    
    def bytt_farge(self, ny_farge: str):
        self.farge = ny_farge
        self.surface.fill(self.farge)
    
    def mus_klikket(self, mus_x: int, mus_y: int):
        return self.rect.collidepoint(mus_x, mus_y)
    
    