import sys
from ball_class import Ball
from paddle_class import Paddle
from pong_default_values import *


pygame.init()
clock = pygame.time.Clock()


# pygame window size and title
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong!")

moving = False  # stops game from starting immediately

# paddle and ball objects
left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()


def redraw_window():
    game_window.fill(background_colour)  # background

    # scores
    game_window.blit(ball.collide_with_boundary()[0], (100, 15))  # player 1 score
    game_window.blit(ball.collide_with_boundary()[1], (window_width - 220, 15))  # player 2 score

    # round and time
    game_window.blit(ball.collide_with_boundary()[2], (75, window_height - 65))
    game_window.blit(ball.collide_with_boundary()[3], (75, window_height - 40))

    # shapes
    pygame.draw.rect(game_window, box_colour, (25, 75, window_width - 50, window_height - 150), 5)  # boundary (box)
    left_paddle.draw(game_window)  # left paddle
    right_paddle.draw(game_window)  # right paddle
    ball.draw(game_window)  # ball

    pygame.display.update()


if __name__ == "__main__":

    while True:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current_time = pygame.time.get_ticks()  # time since pygame initialised
        key = pygame.key.get_pressed()  # gets pressed key

        if key[pygame.K_UP]:  # up arrow key moves right paddle up
            right_paddle.move_up()
        if key[pygame.K_DOWN]:  # down arrow key moves right paddle down
            right_paddle.move_down()
        if key[pygame.K_w]:  # w key moves left paddle up
            left_paddle.move_up()
        if key[pygame.K_s]:  # s key moves left paddle down
            left_paddle.move_down()
        if key[pygame.K_SPACE]:  # starts game
            ball.new_round()
            moving = True

        if moving:
            ball.move()
            ball.collide_with_boundary()
            ball.collide_with_paddle(left_paddle, right_paddle)

        redraw_window()
