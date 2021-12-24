import math
import random

import pygame


class Circle:
    def __init__(self, color, x_position, y_position, radius):
        self.color = color

        self.x_position = x_position
        self.y_position = y_position

        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x_position, self.y_position), self.radius)

    def move(self, new_x_position, new_y_position, smooth_transition=False, smooth_transition_velocity=1):
        if not smooth_transition:
            self.x_position = new_x_position
            self.y_position = new_y_position

        elif smooth_transition:
            x_distance = new_x_position - self.x_position
            y_distance = new_y_position - self.y_position

            theta_angle = math.atan2(x_distance, y_distance)

            if x_distance != 0 or y_distance != 0:
                self.x_position += math.sin(theta_angle) * smooth_transition_velocity
                self.y_position += math.cos(theta_angle) * smooth_transition_velocity


def main(*args, **kwargs):
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FRAMERATE = 60

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Screen")

    clock = pygame.time.Clock()

    circle = Circle((255, 255, 255), 100, 100, 20)
    click_position = [circle.x_position, circle.y_position]

    run_flag = True
    while run_flag:

        if pygame.mouse.get_pressed()[0]:
            click_position = pygame.mouse.get_pos()

        circle.draw(screen)
        circle.move(click_position[0], click_position[1], smooth_transition=True, smooth_transition_velocity=5)
        # circle.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        pygame.display.update()
        screen.fill((0, 0, 0))

        clock.tick(FRAMERATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False

    pygame.quit()
    

if __name__ == "__main__":
    main()
    quit()
