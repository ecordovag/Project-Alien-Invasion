import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    """A class to represent a single drop in the raindrops."""

    def __init__(self, ai_game):
        """Initialize the drop and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the drop image and set its rect attribute.
        self.image = pygame.image.load('images/drop.bmp')
        self.rect = self.image.get_rect()

        # Start each new drop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if drop is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.bottom >= screen_rect.bottom
    
    def update(self):
        """Move a grid of drops down."""
        self.y += self.settings.drop_speed
        self.rect.y = self.y
    
  