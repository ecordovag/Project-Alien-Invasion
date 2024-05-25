import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien_nave.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the right of the screen at different heights.
        self.rect.x = self.settings.screen_width - self.rect.width
        self.rect.y = randint(self.rect.height, self.settings.screen_height - 2 * self.rect.height)

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the alien to the right."""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x