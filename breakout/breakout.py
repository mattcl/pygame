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
    self.bricks = pygame.sprite.Group(bricks)

  def make_paddle(self):
    self.paddle = Paddle((Breakout.WIDTH - Breakout.PADDLE_WIDTH) / 2,
        Breakout.HEIGHT - Breakout.PADDLE_Y_OFFSET,
        (Breakout.PADDLE_WIDTH, Breakout.PADDLE_HEIGHT),
        (0, 0, 0))
    self.paddles = pygame.sprite.Group([self.paddle])

  def make_balls(self):
    self.ball = Ball(Breakout.WIDTH / 2, Breakout.HEIGHT / 2, Breakout.BALL_RADIUS)
    self.balls = pygame.sprite.Group([self.ball])

  def handle_collisions(self):
    collisions = pygame.sprite.groupcollide(self.balls, self.bricks, False, True)
    for ball in collisions:
      ball.bounceY()

    collisions = pygame.sprite.groupcollide(self.balls, self.paddles, False, False)
    for ball in collisions:
      ball.bounceY()

    for ball in self.balls.sprites():
      if ball.rect.x + ball.rect.width >= Breakout.WIDTH or ball.rect.x <= 0:
        ball.bounceX()

      if ball.rect.y + ball.rect.height >= Breakout.HEIGHT or ball.rect.y <= 0:
        ball.bounceY()

  def update_screen(self):
    self.surface.fill((255, 255, 255))
    self.bricks.draw(self.surface)
    self.balls.draw(self.surface)
    self.paddles.draw(self.surface)

  def handle_events(self):
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == MOUSEMOTION:
        new_x = event.pos[0] - Breakout.PADDLE_WIDTH / 2
        new_x = min(max(new_x, 0), Breakout.WIDTH - Breakout.PADDLE_WIDTH)
        self.paddle.rect.x = new_x
      else:
        pass

  def run(self):
    self.make_paddle()
    self.make_bricks()
    self.make_balls()

    while True:
      self.handle_events()
      self.handle_collisions()
      self.update_screen()
      self.balls.update()

      pygame.display.flip()
      self.clock.tick(60)

Breakout().run()
