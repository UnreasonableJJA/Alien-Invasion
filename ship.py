import pygame


class Ship:
    """A class to hold the assets of the ship"""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and its location"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and get its rect
        self.image = pygame.image.load('space_ships_sprites/ship.bmp')
        self.rect = self.image.get_rect()
        self.center_ship()

        """Movement flags for the ship"""
        self.moving_right: bool = False
        self.moving_left: bool = False

    def update(self) -> None:
        """Update the ship's position absed on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        """Update rect object from self.x, removes decimal part when draw"""
        self.rect.x = int(self.x)

    def center_ship(self) -> None:
        """Center the player on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self) -> None:
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
