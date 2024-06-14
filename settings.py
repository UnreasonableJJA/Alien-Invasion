class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self) -> None:
        self.screen_width: int = 1200
        self.screen_height: int = 800
        self.bg_color: tuple = (230, 230, 230)
        # Ship settings
        self.ship_speed: float = 3.5
        self.ship_limit: int = 3

        # Bullet settings
        self.bullet_speed: float = 5
        self.bullet_width: int = 3
        self.bullet_height: int = 15
        self.bullet_color: tuple[int, int, int] = (60, 60, 60)
        self.bullets_allowed: int = 3

        # Alien settings
        self.alien_speed: float = 1.0
        self.alien_drop_speed: float = 50
        self.fleet_direction = 1  # 1 for right, -1 for left
