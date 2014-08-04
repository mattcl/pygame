import sys
import pygame
from pygame.locals import *
from pygame.sprite import Sprite

pygame.init()

class Brick(Sprite):
  WIDTH = 34
  HEIGHT = 8

  def __init__(self, x, y, color):
    Sprite.__init__(self)
    self.image = pygame.Surface([Brick.WIDTH, Brick.HEIGHT])
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

# this is random shit
class Breakout:
  def __init__(self):
    self.surface = pygame.display.set_mode((400, 600))
    pygame.display.set_caption('Hello World')

  def make_bricks(self):
    pass

  def run(self):
    green = (0, 255, 0)
    brick = Brick(40, 60, green)
    bricks = pygame.sprite.Group([brick])
    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      bricks.draw(self.surface)
      pygame.display.flip()

Breakout().run()
