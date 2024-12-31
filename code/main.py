import pygame
import sys
from settings import *
from player import Player
from car import Car

pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Frogger game")

# groups
player_group = pygame.sprite.GroupSingle()
car_group = pygame.sprite.Group()

# player
player = Player(pos=(WINDOW_WIDTH/2,WINDOW_HEIGHT/2), groups=player_group)

# car
car = Car(pos=(100, 500), groups=car_group)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  dt = clock.tick(120) / 1000

  # background
  display_surface.fill("black")

  # groups draw
  player_group.draw(surface=display_surface)
  car_group.draw(surface=display_surface)

  # updates
  player_group.update(dt)
  car_group.update(dt)

  pygame.display.update()
  