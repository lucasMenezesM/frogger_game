import pygame
from os import walk

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, groups):
    super().__init__(groups)

    # player animation
    self.animations_dict = {}
    self.import_assets()
    self.walk_status = "up"
    self.frame_index = 0

    # player appearance
    self.image = self.animations_dict[self.walk_status][self.frame_index]
    self.rect = self.image.get_rect(center=pos)
    self.mask = pygame.mask.from_surface(self.image)

    # player movement
    self.pos = pygame.math.Vector2(self.rect.topleft)
    self.direction = pygame.math.Vector2()
    self.speed = 400


  def import_assets(self):
    for index, folder in enumerate(walk("./graphics/player")):
      if index == 0:
        for key in folder[1]:
          self.animations_dict[key] = []
      else:
        for file_name in folder[2]:
          path = folder[0].replace("\\", "/")+f"/{file_name}"
          surf = pygame.image.load(path).convert_alpha()
          key = folder[0].split("\\")[1]
          
          self.animations_dict[key].append(surf)
    
    print(self.animations_dict)
    

  def animate(self, dt):
    current_animation = self.animations_dict[self.walk_status]
    if self.direction.magnitude() != 0:
      self.frame_index += 8 * dt
      if self.frame_index > len(current_animation):
        self.frame_index = 0
    else:
      self.frame_index = 0
    self.image = self.animations_dict[self.walk_status][int(self.frame_index)]


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
      self.walk_status = "up"
    elif keys[pygame.K_s]:
      self.direction.y = 1
      self.walk_status = "down"
    else:
      self.direction.y = 0

    # horizontal input
    if keys[pygame.K_a]:
      self.direction.x = -1
      self.walk_status = "left"
    elif keys[pygame.K_d]:
      self.direction.x = 1
      self.walk_status = "right"
    else:
      self.direction.x = 0


  def update(self, dt):
    self.input() 
    self.move(dt)
    self.animate(dt)
