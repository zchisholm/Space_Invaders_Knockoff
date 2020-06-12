# zchisholm

class Settings():
	""" A class to store all settings for the Alien Invasion Game."""

	def __init__(self):
		""" Initialize the game's settigns."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 53, 89)

		# Ship Settings
		self.ship_speed_factor = 1.5
		self.ship_limit = 3

		#Bullet Settings
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 250, 250, 250
		self.bullets_allowed = 5

		# Alien Settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction of 1 represetns right: -1 represents left.
		self.fleet_direction = 1

		# Game speed up
		self.speedup_scale = 1.1
		# How quickly the alien point values increase
		self.score_scale = 1.5
		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		self.fleet_direction = 1

		# Scoring 
		self.alien_points = 50


	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		print(self.alien_points)