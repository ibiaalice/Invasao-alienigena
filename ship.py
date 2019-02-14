import pygame;

class Ship():
	
	def __init__(self, screen):
		self.screen = screen;
		self.ai_settings = ai_settings;
		self.image = pygame.image.load('images/ship.png');
		self.rect = self.image.get_rect();
		self.screen_rect = screen.get_rect();
		
		self.rect.centerx = self.screen_rect.centerx;
		self.rect.bottom = self.screen_rect.bottom
		self.center = float(self.rect.centerx);
		
		#flags de movimento
		self.moving_right = False;
		self.moving_left = False;
		
	
	def blitme(self):
		self.screen.blit(self.image, self.rect);
	
	def update(self):
		if self.moving_right:
			self.center += self.ai_settings.ship_speed_factor;
		if self.moving_left:
			self.center -= self.ai_settings.ship_speed_factor;
		
		#atualiza o rect de acordo com o center
		self.rect.centerx = self.center;
