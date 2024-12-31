import pygame
import sys
from settings import *
from player import Player
from car import Car
from random import choice

class AllSprites(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.offset = pygame.math.Vector2()
    self.bg = pygame.image.load("./graphics/main/map.png").convert()
    self.overlay = pygame.image.load("./graphics/main/overlay.png").convert_alpha()

  def customize_draw(self):
    self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
    self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

    display_surface.blit(self.bg, -self.offset)

    for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery):
      offset_pos = sprite.rect.topleft - self.offset
      display_surface.blit(sprite.image, offset_pos)

    display_surface.blit(self.overlay, -self.offset)
        

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Frogger game")

# groups
all_groups = AllSprites()

# player
player = Player(pos=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2), groups=all_groups)

# custom events
spawn_car = pygame.event.custom_type()
pygame.time.set_timer(spawn_car, 50)

pos_list = []

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == spawn_car:
      random_pos = choice(CAR_START_POSITIONS)
      if random_pos not in pos_list:
        Car(pos=random_pos, groups=all_groups)
      pos_list.append(random_pos)
      if len(pos_list) > 5:
        del pos_list[0]

  dt = clock.tick(120) / 1000

  # background
  display_surface.fill("black")

  # groups draw
  all_groups.customize_draw()

  # updates
  all_groups.update(dt)

  pygame.display.update()
  