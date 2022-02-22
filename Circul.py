import pygame, sys
import math
import time
import random
 
pygame.init()
 
win_size = (1920, 1080)
win = pygame.display.set_mode((win_size))
pygame.display.set_caption('Bubble Shooter')
clock = pygame.time.Clock()
 
#Colors
WHITE = (255, 255, 255)
RED = (255, 0, 73)
DARK_RED = (199, 0, 57)
PURPLE = (155, 89, 182)
DARK_PURPLE = (142, 68, 173)
CYAN = (41, 128, 185)
DARK_CYAN = (36, 113, 163)
BLUE = (52, 152, 219)
DARK_BLUE = (46, 134, 193)
GREEN = (26, 188, 156)
DARK_GREEN = (22, 160, 133)
YELLOW = (244, 208, 63)
DARK_YELLOW = (241, 196, 15)
GRAY = (174, 182, 191)
DARK_GRAY = (133, 146, 158)
BLUE_GRAY = (52, 73, 94)
DARK_BLUE_GRAY = (44, 62, 80)
BLACK = (0, 0, 0)
BROWN = (94, 51, 51)
 
 
 
def print_to_display(display, text, font_name, font_size, bold, italic, color, posx, posy, center_around_point, set_custom_dimensions, custom_dimension_width, custom_dimension_height):
    text_parameters = pygame.font.SysFont(font_name, font_size, bold=bold, italic=italic)
    rendered_text = text_parameters.render(text, True, color)
    text_dimensions = rendered_text.get_rect()
    if center_around_point == True and set_custom_dimensions == False:
        text_dimensions.center = ((posx), (posy))
        display.blit(rendered_text, text_dimensions)
    elif center_around_point == False and set_custom_dimensions == False:
        text_dimensions.center = ((posx + text_dimensions[2]/2), (posy + text_dimensions[3]/2))
        display.blit(rendered_text, text_dimensions)
    elif center_around_point == False and set_custom_dimensions == True:
        text_dimensions.center = ((posx + custom_dimension_width/2), (posy + custom_dimension_height/2))
        display.blit(rendered_text, text_dimensions)
    else:
        print('error, can not set custom text dimensions when center around point is True')
 
 
 
 
class Button(object):
    def __init__(self, label, label_size, bold, italic, label_color, button_x, button_y, button_width, button_height, inactive_color, active_color):
        self.label = label
        self.button_x = button_x
        self.button_y = button_y
        self.button_width = button_width
        self.button_height = button_height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.label_size = label_size
        self.label_color = label_color
        self.bold = bold
        self.italic = italic
 
    def create(self, win):
 
        self.mouse_click = pygame.mouse.get_pressed()
        self.mouse_position = pygame.mouse.get_pos()
 
        if (self.button_x + self.button_width) > self.mouse_position[0] > (self.button_x) and (self.button_y + self.button_height) > self.mouse_position[1] > (self.button_y):
            pygame.draw.rect(win, self.active_color, (self.button_x, self.button_y, self.button_width, self.button_height))    
        else:
            pygame.draw.rect(win, self.inactive_color, (self.button_x, self.button_y, self.button_width, self.button_height))
 
        print_to_display(win, self.label, 'Times New Roman', self.label_size, self.bold, self.italic, self.label_color, self.button_x, self.button_y, False, True, self.button_width, self.button_height)
       
    def is_clicked(self):
        if self.button_x + self.button_width > self.mouse_position[0] > self.button_x and self.button_y + self.button_height > self.mouse_position[1] > self.button_y and self.mouse_click[0] == 1:
            return True
 
#Game classes
 
class Bubble(object):
   
    def __init__(self, color):
        self.color = color
        theta = random.randint(1, 360) * math.pi/180
        self.radius = random.randint(10, 40)
        self.x = 500 * math.cos(theta) + 400
        self.y = 500 * math.sin(theta) + 300
        self.offset = 2000
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)
        self.eff_deg = random.randint(1, 360)
 
    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius, 0)
       
        pygame.draw.rect(win, RED, self.hitbox, 2)
 
    def move(self):
        self.hitbox = (self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)
        angles = math.atan2(300 - self.y, 400 - self.x)
        vel = random.randint(3, 13) / 100
        distance = math.hypot(400 - self.x, 300 - self.y)
        distance = int(distance)
 
        self.move_x = math.cos(angles) * vel
        self.move_y = math.sin(angles) * vel
 
        if distance != 0:
            self.x += self.move_x
            self.y += self.move_y
       
        self.offset -= 1
 
class Effect(object):
    def __init__(self, eff_x, eff_y, eff_vel, eff_radius, eff_color):
        self.eff_x = eff_x
        self.eff_y = eff_y
        self.eff_vel = eff_vel
        self.eff_radius = eff_radius
        self.eff_dir = random.uniform(1, 360)
        self.eff_color = eff_color
 
    def bubble_pop_effect(self, win):
 
        pygame.draw.circle(win, self.eff_color, (int(self.eff_x), int(self.eff_y)), self.eff_radius)
 
        #movement
 
        self.move_x = math.cos(self.eff_dir) * self.eff_vel
        self.move_y = math.sin(self.eff_dir) * self.eff_vel
 
        self.eff_x += self.move_x
        self.eff_y += self.move_y
 
        #hitbox
 
        self.eff_hitbox = (self.eff_x - self.eff_radius, self.eff_y - self.eff_radius, self.eff_radius*2, self.eff_radius*2)
 
        pygame.draw.rect(win, RED, self.eff_hitbox, 2)
 
 
 
 
 
class Player:
    def __init__(self, player_x, player_y):
        self.width = 50
        self.height = 50
        self.player_x = player_x - self.width/2
        self.player_y = player_y - self.height/2
        self.player_color = BLUE_GRAY
        self.player_border_color = DARK_BLUE_GRAY
        self.point_x = 0
        self.point_y = 0
        self.hitbox_player = (self.player_x, self.player_y, self.width, self.height)
        self.hitbox_gun_start = (400, 300)
        self.hitbox_gun_end = (self.point_x, self.point_y)
       
    def draw(self, win):
 
        pygame.draw.rect(win, self.player_color, (self.player_x, self.player_y, self.width, self.height))
        pygame.draw.rect(win, self.player_border_color, (self.player_x, self.player_y, self.width, self.height), 5)
 
        mouse_x, mouse_y = pygame.mouse.get_pos()
        theta = math.atan2(mouse_y - 300, mouse_x - 400)
        self.point_x = 100 * math.cos(theta) + 400
        self.point_y = 100 * math.sin(theta) + 300
       
        pygame.draw.line(win, self.player_color, (400, 300), (self.point_x, self.point_y), 10)
 
        self.hitbox_gun_start = (400, 300)
        self.hitbox_gun_end = (self.point_x, self.point_y)
 
        pygame.draw.rect(win, RED, self.hitbox_player, 2)
        pygame.draw.line(win, RED, self.hitbox_gun_start, self.hitbox_gun_end, 2)
 
       
 
 
class Projectile(object):
    def __init__(self, color, vel, radius):
        self.color = color
        self.radius = radius
        self.vel = vel
       
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.theta = math.atan2(self.mouse_y - 300, self.mouse_x - 400)
        self.point_x = 100 * math.cos(self.theta) + 400
        self.point_y = 100 * math.sin(self.theta) + 300
       
        self.x = self.point_x
        self.y = self.point_y
 
 
    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(win, WHITE, (int(self.x + 4), int(self.y - 3)), 3)
 
    def move(self):
       
        self.move_x = math.cos(self.theta) * self.vel
        self.move_y = math.sin(self.theta) * self.vel
 
        self.x += self.move_x
        self.y += self.move_y
 
   
#loops
 
Menu = True
Game = False
Settings = False
 
start_button = Button('Start', 40, False, True, BLACK, 100, 270, 150, 150, GREEN, DARK_GREEN)
quit_button = Button('Quit', 40, False, True, BLACK, 525, 270, 150, 150, RED, DARK_RED)
 
 
#Game related variables
 
player = Player(400, 300)
shoot_timer = 0
click = False
 
#Player list
 
bubbles = [Bubble((random.randint(0, 89), random.randint(0, 37), 105))]
bullets = []
eff_bubbles = []
 
 
while Menu:
 
    #events
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
 
    #Basic Print
           
    win.fill(WHITE)
    print_to_display(win, 'Bubble Shooter', 'Times New Roman', 60, True, False, DARK_BLUE_GRAY, 400, 100, True, False, 0, 0)
    print_to_display(win, 'By Arjun', 'Times New Roman', 30, False, True, DARK_BLUE_GRAY, 400, 160, True, False, 0, 0)
 
    #Buttons and Functionality
   
    start_button.create(win)
    if start_button.is_clicked() == True:
        time.sleep(0.1)
        Game = True
        Menu = False
 
    quit_button.create(win)
    if quit_button.is_clicked() == True:
        pygame.quit()
        quit()
 
    pygame.display.update()
   
 
while Game:
   
    #events
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
 
    mouse_click = pygame.mouse.get_pressed()
 
    #timers
    if shoot_timer > 0:
        shoot_timer += 1
    if shoot_timer > 500:
        shoot_timer = 0
 
    #drawing
 
    player.draw(win)
 
    for bubble in bubbles:
        bubble.draw(win)
        bubble.move()
 
    if bubble.offset == 0:
        bubbles.append(Bubble((random.randint(0, 89), random.randint(0, 37), 105)))
    if len(bubbles) == 0:
        bubbles.append(Bubble((random.randint(0, 89), random.randint(0, 37), 105)))
 
 
 
 
    if mouse_click[0] == 1 and shoot_timer == 0:
       
        bullets.append(Projectile(BROWN, 0.2, 10))
        shoot_timer = 1
 
 
 
 
    #Particle draw
                                 
 
    for bullet in bullets:
        bullet.draw(win)
        bullet.move()
 
        for index, bubble in enumerate(bubbles):
            if bubble.hitbox[0] < bullet.x < bubble.hitbox[0] + bubble.hitbox[2] and bubble.hitbox[1] < bullet.y < bubble.hitbox[1] + bubble.hitbox[3]:
 
                if bubble.radius > 20:
                    for i in range(5):
                        eff_bubbles.append(Effect(bubble.x, bubble.y, 0.5, bubble.radius - 15, bubble.color))
 
                else:
                    for i in range(5):
                        eff_bubbles.append(Effect(bubble.x, bubble.y, 0.5, bubble.radius - 8, bubble.color))
                       
                bubbles.pop(index)
 
        for index, bullet in enumerate(bullets):
            if bubble.hitbox[0] < bullet.x < bubble.hitbox[0] + bubble.hitbox[2] and bubble.hitbox[1] < bullet.y < bubble.hitbox[1] + bubble.hitbox[3]:                
                bullets.pop(index)
 
    for eff_bubble in eff_bubbles:
        eff_bubble.bubble_pop_effect(win)
 
    #Game Over Check
 
    if bubble.hitbox[0] + bubble.hitbox[2] >= player.hitbox_player[0] and bubble.hitbox[0] <= player.hitbox_player[0] + player.hitbox_player[2] and bubble.hitbox[1] + bubble.hitbox[3] >= player.hitbox_player[1] and bubble.hitbox[1] <= player.hitbox_player[1] + player.hitbox_player[3]:
        print('hi')
 
#lag management
 
    if len(bullets) > 50:
        bullets.pop(0)
    if len(eff_bubbles) > 50:
        eff_bubbles.pop(0)
 
   
 
    pygame.display.update()
    win.fill(WHITE)
    clock.tick(100000)
 
 
 

