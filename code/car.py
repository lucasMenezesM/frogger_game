import pygame
from os import walk
from random import choice

class Car(pygame.sprite.Sprite):
  def __init__(self,pos, groups):
    super().__init__(groups)
    
    # import assets
    self.car_images = []
    self.import_assets()

    # car appearance
    self.image = choice(self.car_images)
    self.rect = self.image.get_rect(center = pos)

    # car movement
    self.pos = pygame.math.Vector2(self.rect.center)
    if self.pos[0] < 300:
      self.direction = pygame.math.Vector2((1,0))
    else:
      self.direction = pygame.math.Vector2((-1,0))
      self.image = pygame.transform.flip(self.image, True, False)

    self.speed = 500
  
  
  def import_assets(self):
    # print(walk("./graphics/cars")[2])
    for folder in walk("./graphics/cars"):
      for file in folder[2]:
        path = folder[0] + "/" + file
        surf = pygame.image.load(path).convert_alpha()
        self.car_images.append(surf)


  def move(self, dt):
    self.pos += self.direction * self.speed * dt
    self.rect.center = (round(self.pos.x), round(self.pos.y))

    # destroy when car disappear
    if not -200 < self.pos[0] < 3400:
      self.kill()


  def update(self, dt):
    self.move(dt)