# "Stopwatch: The Game"

import simplegui

# global variables

counter = 0
score = 0
attempts = 0
timer_running = False

# helper functions 

def format(t):
    """
    converts time in tenths of seconds
    into formatted string A:BC.D
    """
    A = int (counter / 600)
    B = int (counter / 100) % 6
    C = int (counter / 10) % 10
    D = counter % 10
    
    current_time = str(A) + ":" + str(B) + str(C) + "." + str(D)
    return current_time
    
# event handlers for buttons; "Start", "Stop", "Reset"

def start():
    """
    starts timer and sets timer status
    """
    timer.start()
    global timer_running
    timer_running = True
    
def stop():
    """
    stops timer, updates score, and sets timer status
    """
    timer.stop()
    global score, attempts, timer_running
    if timer_running:
        attempts += 1
        if (counter % 10) == 0:
            score += 1
    timer_running = False
    
def reset():
    """
    resets timer and score
    """
    timer.stop()
    global counter, score, attempts
    counter = 0
    score = 0
    attempts = 0

# event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1

# draw handler
def draw_handler(canvas):
    canvas.draw_text(format(counter), (60, 85), 30, "White")
    canvas.draw_text(str(score) + "/" + str(attempts), (150, 25), 25, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 150)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
start_button = frame.add_button("Start", start, 100)
stop_button = frame.add_button("Stop", stop, 100)
reset_button = frame.add_button("Reset", reset, 100)

# start frame
frame.start()
