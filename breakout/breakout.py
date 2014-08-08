import sys
import pygame
from pygame.locals import *
from pygame.sprite import Sprite

pygame.init()

class Ball(Sprite):
  def __init__(self, x, y, radius, color=(0, 0, 0)):
    Sprite.__init__(self)
    self.image = pygame.Surface((radius * 2, radius * 2))
    self.image.fill((255, 255, 255))
    pygame.draw.circle(self.image, color, (radius, radius), radius)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.vx = 5
    self.vy = 5

  def bounceX(self):
    self.vx = -self.vx

  def bounceY(self):
    self.vy = -self.vy

  def update(self):
    self.rect.x += self.vx
    self.rect.y += self.vy

class Paddle(Sprite):
  def __init__(self, x, y, size, color):
    Sprite.__init__(self)
    self.image = pygame.Surface(size)
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Brick(Sprite):
  def __init__(self, x, y, size, color):
    Sprite.__init__(self)
    self.image = pygame.Surface(size)
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Breakout:
  RED = (255, 0, 0)
  ORANGE = (255, 165, 0)
  GREEN = (0, 255, 0)
  YELLOW = (255, 255, 0)
  BLUE = (0, 0, 255)
  COLORS = [RED, ORANGE, GREEN, YELLOW, BLUE]

  WIDTH           = 400
  HEIGHT          = 600
  PADDLE_WIDTH    = 60
  PADDLE_HEIGHT   = 10
  PADDLE_Y_OFFSET = 30
  BRICKS_PER_ROW  = 10
  BRICK_ROWS      = 10
  BRICK_SEP       = 4
  BRICK_WIDTH     = (WIDTH - (BRICKS_PER_ROW - 1) * BRICK_SEP) / BRICKS_PER_ROW
  BRICK_HEIGHT    = 8
  BRICK_SIZE      = (BRICK_WIDTH, BRICK_HEIGHT)
  BALL_RADIUS     = 10
  BRICK_Y_OFFSET  = 70
  TURNS           = 3

  def __init__(self):
    self.surface = pygame.display.set_mode((400, 600))
    self.surface.fill((255, 255, 255))
    pygame.display.set_caption('Hello World')
    self.clock = pygame.time.Clock()

  def make_bricks(self):
    bricks = []
    for row in range(0, Breakout.BRICK_ROWS):
      y = row * Breakout.BRICK_SEP \
          + row * Breakout.BRICK_HEIGHT + Breakout.BRICK_Y_OFFSET
      for col in range(0, Breakout.BRICKS_PER_ROW):
        x = Breakout.BRICK_SEP / 2 \
            + col * Breakout.BRICK_SEP + col * Breakout.BRICK_WIDTH
        brick = Brick(x, y, Breakout.BRICK_SIZE, Breakout.COLORS[row / 2])
        bricks.append(brick)
    return pygame.sprite.Group(bricks)

  def handle_collisions(self):
    for ball in self.balls.sprites():
      if ball.rect.x + ball.rect.width >= Breakout.WIDTH or ball.rect.x <= 0:
        ball.bounceX()

      if ball.rect.y + ball.rect.height >= Breakout.HEIGHT or ball.rect.y <= 0:
        ball.bounceY()

  def run(self):
    self.bricks = self.make_bricks()
    ball = Ball(Breakout.WIDTH / 2, Breakout.HEIGHT / 2, Breakout.BALL_RADIUS)
    self.balls = pygame.sprite.Group([ball])
    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()

      self.handle_collisions()

      self.surface.fill((255, 255, 255))

      self.bricks.draw(self.surface)
      self.balls.draw(self.surface)
      self.balls.update()

      pygame.display.flip()
      self.clock.tick(60)

Breakout().run()
