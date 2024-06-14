import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent an alien in a fleet"""

    def __init__(self, ai_game) -> None:
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        """Load the alien and get its rect attribute"""
        self.image = pygame.image.load('space_ships_sprites/alien.bmp')
        self.rect: tuple[int, int] = self.image.get_rect()
        # Start each new alien at the top left of the screen + offset of height
        # & width
        # rect.x and rect.y start at top left initially?
        self.rect.x: int = self.rect.width
        self.rect.y: int = self.rect.height
        # Store the alien's horizontal position
        self.x = float(self.rect.x)

    def check_edges(self) -> bool:
        """Return true if alien hits the edge"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self) -> None:
        """Move the alien left or right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
