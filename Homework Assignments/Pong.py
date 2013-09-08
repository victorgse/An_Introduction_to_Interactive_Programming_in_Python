# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    
    if right == True:
        ball_vel[0] = random.randrange(2, 5)
        ball_vel[1] = - random.randrange(1, 4)
    elif right == False:
        ball_vel[0] = - random.randrange(2, 5)
        ball_vel[1] = - random.randrange(1, 4)
        
# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    paddle1_pos = float(HEIGHT / 2)
    paddle2_pos = float(HEIGHT / 2)
    paddle1_vel = 0.00
    paddle2_vel = 0.00
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    ball_init(random.choice([True, False]))

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT) and (paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle1_pos += paddle1_vel
        
    if (paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT) and (paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT):
        paddle2_pos += paddle2_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polyline([[HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT]], PAD_WIDTH, "White") 
    c.draw_polyline([[WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT]], PAD_WIDTH, "White")
     
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    if (ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH)) and (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT):
        ball_vel[0] = - (1.10 * ball_vel[0])
    elif ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH):
        score1 += 1
        ball_init(False)
    
    if (ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) and (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT):
        ball_vel[0] = - (1.10 * ball_vel[0])
    elif ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        score2 += 1
        ball_init(True)
            
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    c.draw_text(str(score1), (130, 100), 75, "White")
    c.draw_text(str(score2), (430, 100), 75, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = - 10.00
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 10.00
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = - 10.00
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 10.00
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0.00
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0.00
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0.00
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0.00

new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

# start frame
frame.start()
