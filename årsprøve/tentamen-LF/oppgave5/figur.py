import pygame

class Figur:
    def __init__(self, bredde: int, høyde: int, x: int, y: int):
        self.surface = pygame.Surface((bredde, høyde))
        self.rect = self.surface.get_rect()

        self.rect.center = (x,y)
        self.surface.fill("white")
    
    def tegn(self, surface: pygame.Surface):
        surface.blit(self.surface, self.rect)