# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# global variables
num_range = 100
remaining_guesses = 7
secret_number = random.randrange(0, num_range + 1)

# helper functions

def init():
    """
    initializes new game
    """
    
    global secret_number
    secret_number = random.randrange(0, num_range + 1)
    
    print
    print 'New game. Range is from 0 to', num_range
    print 'Number of remaining guesses is', remaining_guesses

# define event handlers
    
def range100():
    """
    button that changes range to range [0,100] and restarts
    """
    
    global num_range, remaining_guesses
    num_range = 100
    remaining_guesses = 7
    init()

def range1000():
    """
    button that changes range to range [0,1000] and restarts
    """
    
    global num_range, remaining_guesses
    num_range = 1000
    remaining_guesses = 10
    init()
    
def get_input(guess):
    """
    input field that takes player's guess,
    compares it to secret number,
    outputs result,
    and restarts if game is over
    """
    
    global remaining_guesses
    remaining_guesses -= 1
    
    guess = int (guess)
    
    print
    print 'Guess was', guess
    print 'Number of remaining guesses is', remaining_guesses  
   
    # main game logic goes here
    
    if (guess == secret_number) and (num_range == 100):
        print 'Correct!'
        range100()
    elif (guess == secret_number) and (num_range == 1000):
        print 'Correct!'
        range1000()
    elif (remaining_guesses == 0) and (num_range == 100):
        print 'You ran out of guesses. The number was', secret_number
        range100()
    elif (remaining_guesses == 0) and (num_range == 1000):
        print 'You ran out of guesses. The number was', secret_number
        range1000()
    elif guess < secret_number:
        print 'Higher!'
    elif guess > secret_number:
        print 'Lower!'


# function call to initialize first game
init()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers
frame.add_button("Range is [0, 100]", range100, 200)
frame.add_button("Range is [0, 1000]", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

# start frame
frame.start()