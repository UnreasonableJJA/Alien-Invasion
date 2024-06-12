import pygame

class Ship:
    """A class to hold the assets of the ship"""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and its location"""
        self.screen: pygame.Surface  = ai_game.screen
        self.screen_rect: pygame.Rect = ai_game.screen.get_rect()
       
        # Load the ship and get its rect
        self.image: pygame.Surface = pygame.image.load('space_ships_sprites/ship.bmp')
        self.rect = self.image.get_rect()

        


