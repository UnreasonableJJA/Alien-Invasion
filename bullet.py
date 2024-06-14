import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game) -> None:
        """Create a bullet object where the ship is"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet at (0, 0) and move it to the the ship's position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's y position as a float.
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the bullet up the screen"""
        # Update the position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y: int = self.y

    def draw_bullet(self) -> None:
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
