import pygame


pygame.font.init()

# window properties
window_width = 1000
window_height = 700

# colours
black = (0, 0, 0)
white = (255, 255, 255)
light_grey = (96, 96, 96)
turquoise = (0, 204, 204)
background_colour = black
box_colour = white
font_colour = white
alternate_font_colour = black

# fonts
score_font = pygame.font.SysFont("Arial", 40)
time_font = pygame.font.SysFont("Arial", 25)

# default ball properties
ball_radius = 10
ball_speed = 3
ball_colour = white

# default paddle properties
paddle_height = 100
paddle_width = 5
paddle_colour = white
paddle_speed = 5

# scores
p1_score = 0
p2_score = 0