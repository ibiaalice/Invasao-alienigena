import pygame;

class Ship():
	
	def __init__(self, screen):
		self.screen = screen;
		
		self.image = pygame.image.load('images/ship.png');
		self.rect = self.image.get_rect();
		self.screen_rect = screen.get_rect();
		
		self.rect.centerx = self.screen_rect.centerx;
		self.rect.bottom = self.screen_rect.bottom
		
		self.moving_right = False;
	
	def blitme(self):
		self.screen.blit(self.image, self.rect);
	
	def update(self):
		if self.moving)right:
			self.rect.centerx += 1;
			
