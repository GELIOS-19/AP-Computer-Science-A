import math
import sys
from abc import ABC

import pygame


class Entity:
  """ Models an entity which is drawn to the window and can move
  during runtime. """

  def __init__(self,
               col: (float, float, float),
               crds: [float, float],
               dims: [float, float],
               vel: float) -> None:
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

  def draw_frame(self, window) -> None:
    """ Draws the entity for a single frame. """
    raise NotImplementedError

  def move_to(self, new_crds: [float, float]) -> None:
    """ Shifts the coordinates of the entity towards new desired
    coordinates. """
    diffs = [new_crds[0] - self._crds[0], new_crds[1] - self._crds[1]]
    ang = math.atan2(diffs[1], diffs[0])
    if int(diffs[0]) != 0 or int(diffs[1]) != 0:
      self._crds[0] += math.cos(ang) * self._vel
      self._crds[1] += math.sin(ang) * self._vel


class CircleEntity(Entity, ABC):
  def __init__(self,
               col: (float, float, float),
               crds: [float, float],
               dims: [float, float],
               vel: float) -> None:
    super().__init__(col, crds, dims, vel)

  def draw_frame(self, window) -> None:
    center_crds = [self._crds[0] + (self._dims[0] / 2), self._crds[1] + (self._dims[1] / 2)]
    pygame.draw.circle(window, self._col, center_crds, self._dims[0] / 2)


def main(*args: [any], **kwargs: {str: any}) -> int:
  """
  Called when the program executes.

  Args:
    args :: [any]:
      Optional runtime arguments
    kwargs :: {str: any}:
      Optional runtime keyword arguments

  Returns:
     int:
      Exit code
  """
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
  my_circle = CircleEntity((0, 0, 0), [100, 100], (30, 30), 1)

  # game loop
  run_flag = True
  while run_flag:
    # draw objects
    my_circle.draw_frame(window)
    my_circle.move_to([200, 400])

    # update frame
    pygame.display.update()
    window.fill((255, 255, 255))
    clock.tick(SCREEN_FRAME_RATE)

    # check events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run_flag = False

  return 0


if __name__ == "__main__":
  exit_code = main()
  sys.exit(exit_code)
