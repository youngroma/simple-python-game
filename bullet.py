import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        'create a bullet in the current position of the gun'
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,2,12)
        self.color = 139, 195, 74
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        'bullet upward movement'
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        'drawing a bullet on the display'
        pygame.draw.rect(self.screen, self.color, self.rect)