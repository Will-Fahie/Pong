import random
from pong_default_values import *

p1_score = 0
p2_score = 0
Round = 1
current_time = 0
round_start_time = 0


class Ball(object):
    def __init__(self, speed=ball_speed, radius=ball_radius, colour=ball_colour):
        self.speed = speed
        self.d_x = self.speed * (random.choice([1, -1]))  # horizontal movement (random start direction)
        self.d_y = self.speed * (random.choice([1, -1]))  # vertical movement (random start direction)
        self.radius = radius
        self.colour = colour
        self.position_x = window_width / 2
        self.position_y = window_height / 2
        self.rect = pygame.Rect(self.position_x, self.position_y, self.radius, self.radius)
        self.lastCollision = None
        self.start = False

    def draw(self, window):
        # draws ball
        self.rect = pygame.Rect(self.position_x, self.position_y, self.radius, self.radius)
        pygame.draw.circle(window, self.colour, (self.position_x, self.position_y), self.radius)

    def move(self):
        # moves ball
        self.position_x += self.d_x
        self.position_y += self.d_y

    @staticmethod
    def new_round():
        global round_start_time
        round_start_time = pygame.time.get_ticks()  # time the round started

    def collide_with_boundary(self):
        global p1_score, p2_score, Round, round_start_time, current_time

        # collides with right side wall
        if self.position_x >= window_width - 25 - ball_radius:
            self.position_x = window_width / 2
            self.position_y = window_height / 2
            self.d_x = -self.d_x
            p1_score += 1
            Round += 1
            self.lastCollision = None
            self.new_round()

        # collides with left side wall
        elif self.position_x <= 25 + ball_radius:
            self.position_x = window_width / 2
            self.position_y = window_height / 2
            self.d_x = -self.d_x
            p2_score += 1
            Round += 1
            self.lastCollision = None
            self.new_round()

        # collides with top or bottom wall
        elif self.position_y >= window_height - 75 - ball_radius or self.position_y <= 75 + ball_radius:
            self.d_y = -self.d_y

        if round_start_time != 0:
            current_time = pygame.time.get_ticks()

        round_time = round((current_time - round_start_time) / 1000)

        p1_score_label = score_font.render(("P1 : " + str(p1_score)), 1, font_colour)
        p2_score_label = score_font.render(("P2 : " + str(p2_score)), 1, font_colour)
        round_label = time_font.render(("Round : " + str(Round)), 1, font_colour)
        round_time_label = time_font.render(("Round time : " + str(round_time)), 1, font_colour)

        return p1_score_label, p2_score_label, round_label, round_time_label

    def collide_with_paddle(self, left_paddle, right_paddle):
        # collides with paddle
        if self.rect.colliderect(left_paddle.rect) and (self.lastCollision == "right" or self.lastCollision is None):
            self.d_x = -self.d_x
            self.lastCollision = "left"
        if self.rect.colliderect(right_paddle.rect) and (self.lastCollision == "left" or self.lastCollision is None):
            self.d_x = -self.d_x
            self.lastCollision = "right"
