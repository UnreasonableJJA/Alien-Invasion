import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(size=(1200,800))
        pygame.display.set_caption(title="Alien Invasion")
   

    def run_game(self) -> None:
       """Start main loop for game"""
       running = True
       while running:
           # Watch for keyboard and mouse events
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   sys.exit()

           pygame.display.flip()

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

