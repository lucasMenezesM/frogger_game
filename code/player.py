import pygame
from settings import WINDOW_HEIGHT, WINDOW_WIDTH

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, groups):
    super().__init__(groups)
    self.image = pygame.Surface((50,50))
    self.image.fill("blue")
    self.rect = self.image.get_rect(center=pos)
    self.mask = pygame.mask.from_surface(self.image)

    self.pos = pygame.math.Vector2(self.rect.topleft)
    self.direction = pygame.math.Vector2()
    self.speed = 400


  def move(self, dt):
    if self.direction.magnitude() > 0:
      self.direction = self.direction.normalize()
    self.pos += self.speed * self.direction * dt
    self.rect.center = (round(self.pos.x), round(self.pos.y))


  def input(self):
    keys = pygame.key.get_pressed()

    # vertical input
    if keys[pygame.K_w]:
      self.direction.y = -1
    elif keys[pygame.K_s]:
      self.direction.y = 1
    else:
      self.direction.y = 0

    # horizontal input
    if keys[pygame.K_a]:
      self.direction.x = -1
    elif keys[pygame.K_d]:
      self.direction.x = 1
    else:
      self.direction.x = 0


  def update(self, dt):
    self.input() 
    self.move(dt)
