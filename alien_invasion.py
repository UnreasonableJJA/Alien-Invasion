import sys
from time import sleep

import pygame

from settings import Settings
from gamestats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

"""
! TODO: Add a single alien to the top left of the screen w/ spacing [x]
! TODO: Fill the top portion of the screen with aliens [x]
! TODO: Make the fleet move sideways and down. If all shot down,
        make a new fleet. If fleet reaches ground, destroy ship and
        generate new fleet [x]
! TODO: Create a life system based on # of ships []
"""


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self) -> None:
        """Initialize the game and create the resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # run game at 1200x800
        dimensions: tuple = (self.settings.screen_width,
                              self.settings.screen_height)
        self.screen = pygame.display.set_mode(size=dimensions)
        """Run game in fullscreen"""
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(title="Alien Invasion")
        # Create an instance to store game statistics
        self.stats = GameStats(self)
        # Create instances to store the player ship, bullets, and aliens
        self.ship = Ship(ai_game=self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        
        self.game_active = True

    def run_game(self) -> None:
        """Start main loop for game"""
        FPS: float = 60
        running = True
        while running:
            self._check_events()
            self.ship.update()
            if self.game_active:
                self._update_bullets()
                self._update_aliens()
                self._update_screen()
            self.clock.tick(FPS)

    def _check_events(self) -> None:
        """Check for any new events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event) -> None:
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False

    def _fire_bullet(self) -> None:
        """Create a new bullet and add it to the self.bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self) -> None:
        """Update position of bullets, remove old bullets"""
        # Update bullet positions
        self.bullets.update()
        # Get rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        self._check_bullet_collisions()

    def _check_bullet_collisions(self) -> None:
        """Check for bullets colliding with aliens and delete both"""
        collisions: dict = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Delete bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self) -> None:
        """Create the fleet of aliens."""
        # Make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_increment_width: float = 2.5 * alien_width
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 4 * alien_height):
            while current_x < (self.settings.screen_width - alien_increment_width):
                self._create_alien(current_x, current_y)
                current_x += alien_increment_width
            # Finished a row; reset x, increment y
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position: int, y_position: int) -> None:
        """Create an alien and place it in the row at its x_position"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _change_fleet_direction(self) -> None:
        """Drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.fleet_direction *= -1

    def _update_fleet_edges(self) -> None:
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _ship_hit(self) -> None:
        """Decrement the ship counter, remove bullets and aliens, generate new
        fleet, and recenter ship"""
        # Decrement ship counter
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            # Remove bullets and aliens
            self.aliens.empty()
            self.bullets.empty()
            # Generate new fleet and recenter ship
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self) -> None:
        for alien in self.aliens.sprites():
            # NOTE: Height is counted from the top
            if alien.rect.bottom >= self.settings.screen_height: 
                self._ship_hit()
                break

    def _update_aliens(self) -> None:
        """Update the positions of all aliens in the fleet."""
        self._update_fleet_edges()
        self.aliens.update()
        # Look for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _update_screen(self) -> None:
        """Update the screen and flip to the the new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
