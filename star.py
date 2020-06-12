# zchisholm
# Star file for the background of alien_invasion

# zchisholm
import pygame

class Star():

	def __init__(self, ai_settings, screen):
		""" Initialize the ship and set its start position."""
		self.screen = screen
		self.ai_settings = ai_settings

		#load the ship image and get its rect.
		self.image = pygame.image.load('images/star.png')
		self.image = pygame.transform.scale(self.image, (64, 64))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's center
		self.center = float(self.rect.centerx)

		# Movement Flags
		self.moving_right = False
		self.moving_left = False

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)