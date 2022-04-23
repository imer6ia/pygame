import sys
import random
import pygame

pygame.init()

width = 1000
height = 600

size = (width, height)

window = pygame.display.set_mode(size)


background = pygame.image.load("228.jpg")
background = pygame.transform.scale(background, (width, height))

clock = pygame.time.Clock()



pygame.mixer.music.load("song228.mp3")
pygame.mixer.music.play()


class ship228(pygame.sprite.Sprite):
    def __init__(self, x=width / 2, y=height / 2):
        super().__init__()

        # self.image = pygame.image.load('ship228.png')
        self.image = pygame.image.load('ship228.png')
        self.image = pygame.transform.scale(self.image, (70, 70)) ###
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = y

    def update(self, *args):
        up, down, right, left = args

        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + self.rect.size[1] > height: #rect.size = ( 70, 70 )
            self.rect.y = height - self.rect.size[1]

        if up:
            self.rect.y -= 10
        if down:
            self.rect.y += 10


class ENEMY228(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()

        self.rect.y = random.randrange(height - self.rect.height)
        self.rect.x = random.randrange(width + 40, width + 100)
        self.speedx = random.randrange(5, 10)
        self.speedy = random.randrange(-2, 2)

    def update(self, *args):
        self.rect.x -= self.speedx
        self.rect.y += self.speedy

        if self.rect.right < 0:
            self.rect.y = random.randrange(height - self.rect.height)
            self.rect.x = random.randrange(width + 40, width + 100)
            self.speedx = random.randrange(5, 8)
            self.speedy = random.randrange(-3, 3)



all_sprites = pygame.sprite.Group()
shtu4ki = pygame.sprite.Group()

for i in range(10):
    bullet = ENEMY228()
    all_sprites.add(bullet)
    shtu4ki.add(bullet)

ship = ship228()
all_sprites.add(ship)

while True:
    keys = pygame.key.get_pressed()

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    up, down, right, left = keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_RIGHT], keys[pygame.K_LEFT]
    all_sprites.update(up, down, right, left)


    window.blit(background, (0, 0))
    all_sprites.draw(window)

    situation = pygame.sprite.spritecollide(ship, shtu4ki, False)

    if situation: #коллизия
        pygame.display.update()
        pygame.time.wait(1000)
        sys.exit()

    pygame.display.update()