from ship import Ship
from settings import Settings
import sys
import pygame

"""This project is from Python Crash Course 2nd Edition by Eric Matthes"""


class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """initialize the game, and create the game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """starts the main loop for the game."""
        while True:
            # Watch for the keyboard and mouse events.
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        """Responds to keypresses and mouse events."""
        # Watch for the keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False

    def _update_screen(self):
        """Update image on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the ame.
    ai = AlienInvasion()
    ai.run_game()
