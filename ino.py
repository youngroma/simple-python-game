import pygame

class Ino(pygame.sprite.Sprite):
    'one alien class'
    def __init__(self, screen):
        'initialize and set starting position'
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        'aliens display'
        self.screen.blit(self.image, self.rect)
    def update(self):
        'alien travel'
        self.y += 0.1
        self.rect.y = self.y