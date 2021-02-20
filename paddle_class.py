from pong_default_values import *


class Paddle(object):
    def __init__(self, side, height=paddle_height, width=paddle_width, colour=paddle_colour, speed=paddle_speed):
        self.side = side  # left or right
        self.height = height
        self.width = width
        self.colour = colour
        self.speed = speed
        if self.side == "left":
            self.position_x = 50
            self.rectWidth = self.width + ball_radius  # stops ball clipping inside left paddle
        elif self.side == "right":
            self.position_x = window_width - width - 50
            self.rectWidth = self.width
        self.position_y = window_height / 2 - height / 2
        self.rect = pygame.Rect(self.position_x, self.position_y, self.rectWidth, self.height)  # rectangle to detect collisions

    def draw(self, window):
        # draws paddle
        self.rect = pygame.Rect(self.position_x, self.position_y, self.rectWidth, self.height)  # updates collision rectangle
        pygame.draw.rect(window, self.colour, (self.position_x, self.position_y, self.width, self.height))  # redraws rectangle

    def move_up(self):
        # moves paddle up
        if self.position_y > 80:  # top boundary
            self.position_y -= self.speed

    def move_down(self):
        # moves paddle down
        if self.position_y < window_height - self.height - 80:  # stops rectangle clipping inside boundary
            self.position_y += self.speed
