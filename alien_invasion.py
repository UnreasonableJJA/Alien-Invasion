import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self) -> None:
        """Initialize the game and create the resources""" 
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings() 
        
        dimensions: tuple = (self.settings.screen_width, 
                             self.settings.screen_height)

        self.screen = pygame.display.set_mode(size=dimensions)
        pygame.display.set_caption(title="Alien Invasion")

    def run_game(self) -> None:
       """Start main loop for game"""
       FPS: float = 60
       running = True
       while running:
           # Watch for keyboard and mouse events
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   sys.exit()
           #Redraw the screen
           self.screen.fill(color=self.settings.bg_color)

           #Make the post recently drawn screen visibile
           pygame.display.flip()
           self.clock.tick(FPS)


if __name__ == "__main__":
    ai: AlienInvasion = AlienInvasion()
    ai.run_game()
