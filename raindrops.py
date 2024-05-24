import sys

import pygame

from settings import Settings
from drop import Drop

class Raindrops:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrops")

        self.drops = pygame.sprite.Group()
        self.row_drops = pygame.sprite.Group()

        self._create_raindrops()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_drops()         
            self._update_screen()
            self.clock.tick(60)
    

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    

    def _create_raindrops(self):
        """Create raindrops."""
        # Create a drop and keep adding drops until there's no room left.
        # Spacing between drops is one drop width and one drop height.
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size

        current_x, current_y = drop_width, drop_height
        while current_x < (self.settings.screen_width - 1.5 * drop_width):
            self._create_drop(current_x, current_y)
            current_x += 2 * drop_width
     

    def _create_drop(self, x_position, y_position):
            """Create a drop and place it in the raindrops."""
            new_drop = Drop(self)
            new_drop.y = y_position
            new_drop.rect.y = y_position
            new_drop.rect.x = x_position
            self.drops.add(new_drop)


    def _check_fleet_edges(self):
        """Respond appropriately if any drops have reached an edge."""
        for drop in self.drops.sprites():
            if drop.check_edges():
                self._create_raindrops()
                break
      

    def _update_drops(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
         # Get rid of drops that have disappeared.
        for drop in self.drops.copy():
            if drop.rect.bottom >= self.settings.screen_height:
                self.drops.remove(drop)
        self.drops.update()


    def _update_screen(self):
        """Update changes on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
            
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Raindrops()
    ai.run_game()