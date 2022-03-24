import abc
import math

import pygame


class MovableObject(abc.ABC):
    """MovableObject is an abstract base class that serves as the foundation
    for any game object."""

    def __init__(self, coords, velocity):
        """Constructor
        Args:
            coords: List[int, int]
                Represents the screenspace coordinates at which the game object
                is drawn.
            velocity: int | float
                Represents the velocity or speed with which the game object
                moves.
        """
        self.coords = coords
        self.velocity = velocity

    @abc.abstractmethod
    def draw(self, window):
        """Abstract method that draws the game object to a particular window
        object for a single frame. This method should be called inside the game
        loop.
        Args:
            window: pygame.surface.Surface
                Represents the surface on which the game object is
                drawn.
        """
        pass

    def move_to(self, new_coordinates):
        """Method that implements logic to move a game object to any
        screenspace coordinate.
        Args:
            new_coordinates: Tuple[int, int]
                Represents the screenspace coordinates to which the game object
                moves to.
        Returns:
            bool
                Indicates if the game object has reached new_coordinates.
        """
        xdiff = new_coordinates[0] - self.coords[0]
        ydiff = new_coordinates[1] - self.coords[1]
        angle = math.atan2(ydiff, xdiff)
        if (xdiff >= self.velocity or
                xdiff <= -self.velocity) or (ydiff >= self.velocity or
                                             ydiff <= -self.velocity):
            self.coords[0] += math.cos(angle) * self.velocity
            self.coords[1] += math.sin(angle) * self.velocity
            return False
        return True


class Player(MovableObject):
    """Player is a class that represents the character in the game which the
    user controls. This class derives from MovableObject."""

    def __init__(self, coords, velocity, color, dims):
        """Constructor
        Args:
            coords: List[int, int]
                Represents the screenspace coordinates where the player will be
                drawn.
            velocity: int | float
                Represents the velocity with which the player will move.
            color: Tuple[int, int, int]
                Represents the color of the player using RGB format.
            dims: List[int, int]
                Represents the length and width of the player.
        """
        super(Player, self).__init__(coords, velocity)
        self.color = color
        self.dims = dims

    def _get_termc(self):
        """Gets the coordinates at the end of the barrel of the player's gun.
        Returns:
            List[float, float]
                The coordinates of the point where the player's barrel ends.
        """
        mousec = pygame.mouse.get_pos()
        xdiff = mousec[0] - self.coords[0]
        ydiff = mousec[1] - self.coords[1]
        angle = math.atan2(ydiff, xdiff)
        termc = [
            self.coords[0] + math.cos(angle) * 100,
            self.coords[1] + math.sin(angle) * 100
        ]
        return termc

    def draw(self, window):
        """Player implementation of the abstract draw method from the 
        MovableObject base class. Refer to line 32."""
        coords = [
            self.coords[0] - (self.dims[0] / 2),
            self.coords[1] - (self.dims[1] / 2)
        ]
        pygame.draw.rect(window, self.color, coords + self.dims)
        termc = self._get_termc()
        pygame.draw.line(window, self.color, self.coords, termc, 10)


class Circle(MovableObject):
    """Circle is a class that represents a circle. This class derives from
    MovableObject."""

    def __init__(self, coords, velocity, color, radius):
        """Constructor
        Args:
            coords: List[int, int]
                Represents the screenspace coordinates where the circle will be
                drawn.
            velocity: int | float
                Represents the velocity with which the circle will move.
            color: Tuple[int, int, int]
                Represents the color of the circle in RGB format.
            radius: int
                Represents the radius of the circle.
        """
        super(Circle, self).__init__(coords, velocity)
        self.color = color
        self.radius = radius

    def draw(self, window):
        """Circle implementation of the abstract draw method from the
        MovableObject base class. Refer to line 32."""
        pygame.draw.circle(window, self.color, self.coords, self.radius)


def main(*args, **kwargs):
    """This is the main method which is called when the script is executed.
    Args:
        args: Tuple[str]
            Some default arguments.
        kwargs: Dict[str, Any]
            Some default keyword arguments.
    """
    pygame.init()
    window = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("Circle War")
    clock = pygame.time.Clock()

    circle = Circle([100, 100], 2, (0, 0, 0), 20)
    player = Player([400, 300], 1, (0, 0, 0), [50, 50])

    run_flag = True
    while run_flag:
        circle.draw(window)
        player.draw(window)

        circle_arrived = circle.move_to((400, 300))

        pygame.display.update()
        window.fill((255, 255, 255))
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False


if __name__ == "__main__":
    main()
