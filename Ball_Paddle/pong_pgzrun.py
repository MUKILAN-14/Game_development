import pgzrun
WIDTH = 800
HEIGHT = 500
orange = (254, 176, 88)
white = (255,255,255)
ball = Actor('ball')
paddle = Actor('paddle')
paddle.pos = (100, HEIGHT - 20)
ball_velocity_x = 10
ball_velocity_y = 5
score = 0
missed = False


def draw():
    screen.fill(orange)
    ball.draw()
    paddle.draw()
    screen.draw.text('score:'+str(score), (10,10), fontsize=20, color = white)
    if missed:
        screen.draw.text('GAME OVER !',(200,200), fontsize=50, color = white)


def update():
    if not missed:
        ball.right = ball.right+ball_velocity_x
        ball.bottom = ball.bottom+ball_velocity_y
        check_boundaries()
        check_collision()
        check_paddle_miss()


def on_mouse_move(pos):
    if not missed:
        paddle.left = pos[0]
    if paddle.right > WIDTH:
        paddle.right = WIDTH
    if paddle.left < 0:
        paddle.left = 0


def check_boundaries():
    global ball_velocity_x
    global ball_velocity_y
    if ball.right > WIDTH or ball.left < 0:
        ball_velocity_x *= -1
    if ball.top < 0:
        ball_velocity_y *= -1


def check_collision():
    global ball_velocity_y, score
    if ball.colliderect(paddle):
        score += 1
        ball_velocity_y *= -1


def check_paddle_miss():
    global missed
    if ball.bottom > paddle.bottom:
        missed = True


pgzrun.go()