import pygame 
import random

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atack")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("tank.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0

	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

class tank_evils(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("tank_green.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 22 :
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)



class atack(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("misilespecial.png")
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()




background = pygame.image.load("fondo-negro.jpg").convert()


all_sprites = pygame.sprite.Group()
tanks_list = pygame.sprite.Group()
atacks = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
	tanques = tank_evils()
	all_sprites.add(tanques)
	tanks_list.add(tanques)


#running = True
#while running:
	#clock.tick(60)

	#for event in pygame.event.get():
		#if event.type == pygame.QUIT:
			#running = False
		

	#all_sprites.update()

	#screen.blit(background, [0, 0])
	#all_sprites.draw(screen)
	#pygame.display.flip()

#pygame.quit()


running = True
while running:

	clock.tick(50)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False
		
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()


	all_sprites.update()

	hits = pygame.sprite.groupcollide(tanks_list, atacks, True, True)
	for hit in hits:
		tanque = tanks_evil()
		all_sprites.add(tanque)
		tanks_list.add(tanque)
		
	hits = pygame.sprite.spritecollide(player, tanks_list, False)
	if hits:
		running = False

	screen.blit(background, [0, 0])
	all_sprites.draw(screen)
	pygame.display.flip()

pygame.quit()
