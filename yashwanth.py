
import abc
import math

import pygame


class Entity(abc.ABC):
  """ Models an entity which is drawn to the window and can move during runtime. """

  def __init__(self, col: (float, float, float), crds: [float, float], dims: [float, float], vel: float) -> None:
    self._crds = crds
    self._dims = dims
    self._vel = vel
    self._col = col

  @property
  def left_crd(self) -> float:
    """ Returns the left coordinate. """
    return self._crds[0]

  @property
  def top_crd(self) -> float:
    """ Returns the top coordinate. """
    return self._crds[1]

  @property
  def width(self) -> float:
    """ Returns the width in the horizontal direction. """
    return self._dims[0]

  @property
  def height(self):
    """ Returns the height in the vertical direction. """
    return self._dims[1]

  @abc.abstractmethod
  def draw_frame(self, window: pygame.surface.Surface) -> None:
    """ Draws the entity for a single frame. """
    pass

  def move_to(self, new_crds: [float, float]) -> None:
    """ Shifts the coordinates of the entity towards new desired coordinates. """
    diffs = [new_crds[0] - self._crds[0], new_crds[1] - self._crds[1]]
    ang = math.atan2(diffs[1], diffs[0])
    if round(diffs[0]) not in range(-int(self._vel), int(self._vel)) or round(diffs[1]) not in range(-int(self._vel), int(self._vel)):
      self._crds[0] += math.cos(ang) * self._vel
      self._crds[1] += math.sin(ang) * self._vel


class CircleEntity(Entity):
  """ An entity that takes the shape of a circle. """
  def __init__(self, col: (float, float, float), crds: [float, float], dims: [float, float], vel: float) -> None:
    assert dims[0] == dims[1]
    super(CircleEntity, self).__init__(col, crds, dims, vel)

  def draw_frame(self, window: pygame.surface.Surface) -> None:
    """ Overrides the `draw_frame` method from the base class. """
    center_crds = [self._crds[0] + (self._dims[0] / 2), self._crds[1] + (self._dims[1] / 2)]
    pygame.draw.circle(window, self._col, center_crds, self._dims[0] / 2)


def main() -> None:
  """ Called when the program executes. """
  # constants
  SCREEN_RESOLUTION = (800, 600)
  SCREEN_TITLE = "Circle Game"
  SCREEN_FRAME_RATE = 60

  # contextualize
  pygame.init()
  window = pygame.display.set_mode(SCREEN_RESOLUTION)
  pygame.display.set_caption(SCREEN_TITLE)
  clock = pygame.time.Clock()

  # create game objects
  my_circles = []
  for i in range(10):
    my_circles.append(CircleEntity(col=(255-i*15, 255-i*15, 255-i*15), crds=[100, 100], dims=(i*10, i*10), vel=i))

  # game loop
  run_flag = True
  while run_flag:
    # draw objects
    for my_circle in my_circles:
      my_circle.draw_frame(window)
      my_circle.move_to([400, 300])

    # update frame
    pygame.display.update()
    window.fill((255, 255, 255))
    clock.tick(SCREEN_FRAME_RATE)

    # check events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run_flag = False


if __name__ == "__main__":
  main()
  exit()
