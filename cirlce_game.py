# Game Dev with PyGame

import math

import pygame


WINDOW_WIDTH, WINDOW_HEIGT = 800, 600
FRAMERATE = 60

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGT))
pygame.display.set_caption("Circle War")
clock = pygame.time.Clock()


class HitBox:
    COLOR = (255, 0, 0)

    def __init__(self, object_):
        self.hitbox_x = object_.rectangle_x_position
        self.hitbox_y = object_.rectangle_y_position
        self.hitbox_length = object_.rectangle_length
        self.hitbox_width = object_.rectangle_width

    def draw_frame(self, window):
        pygame.draw.rect(window, self.COLOR, (self.hitbox_x, self.hitbox_y, self.hitbox_length, self.hitbox_width), 1)

    def object_in_hitbox(self, object_):
        pass

class CircleEnemy:
    def __init__(self, 
                 initial_x_position: float, 
                 initial_y_position: float, 
                 radius: float, 
                 velocity: float, 
                 color: (float, float, float)) -> None:
        self.x_position = initial_x_position
        self.y_position = initial_y_position
        self.radius = radius
        self.velocity = velocity
        self.color = color

    # standard attrs
    @property
    def rectangle_length(self): return self.radius * 2 
    @property
    def rectangle_width(self): return self.radius * 2
    @property
    def rectangle_x_position(self): return self.x_position - self.radius
    @property
    def rectangle_y_position(self): return self.y_position - self.radius

    def draw_frame(self, window: pygame.Surface) -> None:
        pygame.draw.circle(window, self.color, (self.x_position, self.y_position), self.radius)

    def move_toward(self, x_coordinate: float, y_coordinate: float):
        # reference unit circle
        x_difference = x_coordinate - self.x_position
        y_difference = y_coordinate - self.y_position
        theta_angle = math.atan2(y_difference, x_difference)
        if x_difference != 0 or y_difference != 0:
            self.x_position += math.cos(theta_angle) * self.velocity
            self.y_position += math.sin(theta_angle) * self.velocity

    @property
    def hitbox(self):
        return HitBox(self)

if __name__ == "__main__":
    RUN_FLAG = True # variable true during runtime

    # make objects
    my_circle = CircleEnemy(100, 100, 50, 1, (255, 255, 255))

    # game loop
    while RUN_FLAG:
        # draw objects
        my_circle.draw_frame(window)
        my_circle.move_toward(73.23, 392.67)
        my_circle.hitbox.draw_frame(window)

        # update frame
        pygame.display.update()
        window.fill((0, 0, 0))
        clock.tick(FRAMERATE)
        
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN_FLAG = False

    quit()
