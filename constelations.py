import sys

import pygame

from random import randint
from settings import Settings
from star import Star

class Constelation:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Constelations")

        self.stars = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            
    
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_fleet(self):
        """Create the constelation."""
        # Create a star and keep adding stars until there's no room left.
        # Spacing between stars is random.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 2 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_star(current_x+randint(-25,25), current_y+randint(-25,25))
                current_x += randint(5,10) * star_width

            # Finished a row; reset x value, and increment y value.
            current_x = star_width
            current_y += randint(45,50) + star_height
    
    def _create_star(self, x_position, y_position):
            """Create a star and place it in the sky."""
            new_star = Star(self)
            new_star.x = x_position
            new_star.rect.x = x_position
            new_star.rect.y = y_position
            self.stars.add(new_star)
    
    def _update_screen(self):
        """Update changes ont he screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)   
        
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    cons = Constelation()
    cons.run_game()