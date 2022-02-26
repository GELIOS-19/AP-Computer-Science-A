import abc
import math

import pygame


# First, we must write all the class definitions for the
# classes we are planning to use in the program.
class MovableObject(abc.ABC):
  """ MovableObject is an abstract base class that serves
  as the foundation for any game object. """

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
  MovableObject. """

  def __init__(self, coords, velocity, color, dims):
    """ Constructor
    Args:
      coords :: List[int, int]
        Represents the screenspace coordinates where the 
        player will be drawn.
      velocity :: int | float
        Represents the velocity with which the player will 
        move.
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
    # of the rectangle. This is done to maintain consistency 
    # with the way pygame draws circles.
    coords = [coords[0] - (dims[0] / 2),
              coords[1] - (dims[1] / 2)]
    super(Player, self).__init__(coords, velocity)
    self.color = color
    self.dims = dims

  def draw(self, window):
    """ Player implementation of the abstract draw method 
    from the MovableObject base class. Refer to line 32. """
    pygame.draw.rect(window, self.color,
                     self.coords + self.dims)
    # Since pygame.draw.line() draws a line with the reference
    # point as the starting point, the translations done to
    # self.coords need to be reversed.
    mc = pygame.mouse.get_pos()
    origc = [self.coords[0] + (self.dims[0] / 2),
             self.coords[1] + (self.dims[1] / 2)]
    pygame.draw.line(window, self.color, origc, mc, 10)


class Circle(MovableObject):
  """ Circle is a class that represents a circle. This class
  derives from MovableObject. """

  def __init__(self, coords, velocity, color, radius):
    """ Constructor
    Args:
      coords :: List[int, int]
        Represents the screenspace coordinates where the 
        circle will be drawn.
      velocity :: int | float
        Represents the velocity with which the circle will 
        move.
      color :: Tuple[int, int, int]
        Represents the color of the circle in RGB format.
      radius :: int
        Represents the radius of the circle.
    """
    super(Circle, self).__init__(coords, velocity)
    self.color = color
    self.radius = radius

  def draw(self, window):
    """ Circle implementation of the abstract draw method 
    from the MovableObject base class. Refer to line 32. """
    pygame.draw.circle(window, self.color,
                       self.coords, self.radius)


def main(*args, **kwargs):
  """ This is the main method which is called when the script
  is executed.
  Args:
    args :: Tuple[str]
      Some default arguments.
    kwargs :: Dict[str, Any]
      Some default keyword arguments.
  """
  # Before we can start using the pygame library, we must
  # do a few things in order to initialize it. Firstly, we must
  # call the pygame.init() method in order to initialize the
  # library. Then, we need to set up a window to which our game
  # will be rendered (we can optionally choose to title the
  # window) Finally, we must set up a clock, which is a timer
  # that moderates the number of frames drawn per second (we
  # use this because we want the game to run at the same speed
  # on different hardware).
  pygame.init()
  window = pygame.display.set_mode([800, 600])
  pygame.display.set_caption("Circle War")
  clock = pygame.time.Clock()

  # Here, we will instantiate the objects that we want to use
  # in our game when the game initially starts running.
  circle = Circle([100, 100], 2, (0, 0, 0), 20)
  player = Player([400, 300], 1, (0, 0, 0), [50, 50])

  # This is the start of the game loop, which is a loop that
  # runs throughout the lifetime of the game. Each iteration of
  # this loop represents a single frame. In this loop, we must
  # have three phases: drawing phase, update phase, and event
  # phase. The variable run_flag will be True while the loop is
  # running. In order to end the loop and stop the game, we
  # need to set run_flag to False.
  run_flag = True
  while run_flag:
    # In the drawing phase, we must draw all the objects we want
    # to show on the subsequent frame.
    circle.draw(window)
    player.draw(window)

    # In the update phase, we must make any changes we want to 
    # the attributes of the game objects drawn on the screen.
    # Additionally, we need to call the pygame.display.update()
    # function to refresh the screen for the next frame. Then we
    # need to overwrite the current frame by filling it with a 
    # solid color. Finally, we need to tick our clock to keep 
    # time.
    circle.move_to((400, 300))

    pygame.display.update()
    window.fill((255, 255, 255))
    clock.tick(60)

    # In the event phase, we must check if game events have
    # occured. This most significantly includes keyboard 
    # events and window events. We can check for these events
    # using pygame's event loop method, called 
    # pygame.event.get().
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run_flag = False


if __name__ == "__main__":
  main()
