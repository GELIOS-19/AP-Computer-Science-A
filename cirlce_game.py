import abc
import math

import pygame


# define classes
class MovableObject(abc.ABC):
  """ MovableObject is an abstract base class that serves
  as the foundation for any game object."""

  def __init__(self, coords, velocity):
    """ Constructor
    Args:
      coords :: List[int, int]
        Represents the screenspace coordinates at which the 
        game object is drawn.
      velocity :: int | float
        Represents the velocity or speed with which the game
        object moves.
    """
    self.coords = coords
    self.velocity = velocity

  @abc.abstractmethod
  def draw(self, window):
    """ Abstract method that draws the game object to a 
    particular window object for a single frame. This method 
    should be called inside of the game loop. 
    Args:
      window :: pygame.surface.Surface
        Represents the surface on which the game object is 
        drawn.
    """
    pass  

  def move_to(self, new_coordinates):
    """ Method that implements logic to move a game object to 
    any screenspace coordinate.
    Args:
      new_coordinates :: Tuple[int, int]
        Represents the screenspace coordinates to which the 
        game object moves to. 
    """
    nx, ny = new_coordinates
    x, y = self.coords
    xdiff = nx - x
    ydiff = ny - y  
    angle = math.atan2(ydiff, xdiff)
    if round(xdiff) != 0 or round(ydiff) != 0:
      self.coords[0] += math.cos(angle) * self.velocity
      self.coords[1] += math.sin(angle) * self.velocity


class Player(MovableObject):
  """ Player is a class that represents the character in the 
  game which the user controls. This class derives from 
  MovaleObject. """

  def __init__(self, coords, velocity, color, dims):
    """ Constructor
    Args:
      coords :: List[int, int]
        Represents the screenspace coordinates where the
        game object will be drawn.
      velocity :: int | float
        Represents the velocity with which the player
        will move.
      color :: Tuple[int, int, int]
        Represents the color of the player using RGB format.
      dims :: List[int, int]
        Represents the length and width of the player.
    """
    # Since pygame draws rectangles with the point of reference
    # being the top left corner, we need to modify the coords 
    # parameter by subtracting half the length from the 
    # x-coordinate and half the width from the y-coordinate.
    # This will change the point of reference to the center
    # of the rectangle. This is done to maintain consistancy with 
    # the way pygame draws circles.
    coords = [coords[0] - (dims[0] / 2), 
              coords[1] - (dims[1] / 2)]
    super(Player, self).__init__(coords, velocity)
    self.color = color
    self.dims = dims

  def draw(self, window):
    """ Implementation of the abstract draw method from the 
    MoveableObject base class. Refer to line 32. """
    pygame.draw.rect(window, self.color, 
                     self.coords + self.dims)


class Circle(MovableObject):
  """ Circle is a class that represents a circle. This class
  derives from MovableObject. """

  def __init__(self, coords, velocity, color, radius):
    super(Circle, self).__init__(coords, velocity)
    self.color = color
    self.radius = radius

  def draw(self, window):
    pygame.draw.circle(window, self.color, 
                       self.coords, self.radius)


def main():
  # contextualize
  pygame.init()
  window = pygame.display.set_mode([800, 600])
  pygame.display.set_caption("Circle War")
  clock = pygame.time.Clock()

  # make objects
  circle = Circle([100, 100], 2, (0, 0, 0), 20)
  player = Player([400, 300], 1, (0, 0, 0), [50, 50])

  # game loop
  run_flag = True
  while run_flag:
    # draw objects
    circle.draw(window)
    circle.move_to((400, 300))
    player.draw(window)

    # update every frame
    pygame.display.update()
    window.fill((255, 255, 255))
    clock.tick(60)

    # check for events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run_flag = False


if __name__ == "__main__":
  main()
