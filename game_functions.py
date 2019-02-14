import sys;
import pygame;

def check_events():
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(); 
		
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets);
				
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship);
			
				
def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True;
		
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True;
		
def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False;
			
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False;
		
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets);
		
		if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings, screen, ship);
			bullets.add(new_bullet);
	
	elif event.key == pygame.K_q:
		sys.exit();

def fire_bullet(ai_settings, screen, ship, bullets):
	 #cria um novo projetil e adiciona no gp de projeteis
	 if(len(bullets) < ai_settings.bullets_allowed):
		 new_bullet = Bullet(ai_settings, screen, ship);
		 bullets.add(new_bullet);
	
def update_screen(ai_settings, screen, ship):
	
	screen.fill(ai_settings.bg_collor);
	ship.blitme();
	pygame.display.flip();

def update_bullets(bullets):
	
	#atualiza as posições dos projeteis
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet);
	
