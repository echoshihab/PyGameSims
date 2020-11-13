from ship import Ship
from settings import Settings
import sys
iimport pygame

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the ame.
    ai = AlienInvasion()
    ai.run_game()
