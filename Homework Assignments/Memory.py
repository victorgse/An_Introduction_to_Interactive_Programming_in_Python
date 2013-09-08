# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def init():
    global pos, deck, moves, state, exposed
    pos = [10, 70]
    deck = range(8) + range(8)
    random.shuffle(deck)
    moves = 0
    label.set_text("Moves = " + str(moves))
    state = 0
    exposed = []
    for n in range(16):
        exposed.append(False)
     
# define event handlers
def mouseclick(pos):
    i = pos[0] // 50
    global state, card_1_index, card_2_index, moves
    if state == 0:
        exposed[i] = True
        card_1_index = i
        state = 1
    elif state == 1:
        if (i != card_1_index) and (exposed[i] != True):
            exposed[i] = True
            card_2_index = i
            state = 2
            moves += 1
    elif state == 2:
        if (deck[card_1_index] != deck[card_2_index]) and (i != card_1_index) and (i != card_2_index) and (exposed[i] != True):
            exposed[card_1_index] = False
            exposed[card_2_index] = False
            exposed[i] = True
            card_1_index = i
            state = 1
        elif (deck[card_1_index] == deck[card_2_index]) and (i != card_1_index) and (i != card_2_index) and (exposed[i] != True):
            exposed[i] = True
            card_1_index = i
            state = 1
    label.set_text("Moves = " + str(moves))
                           
def draw(canvas):
    for i in range(len(deck)):
        if exposed[i] == True:
            canvas.draw_text(str(deck[i]), (pos[0] + i * 50, pos[1]), 60, "White")
        else:
            canvas.draw_polygon([[0 + i * 50, 0], [0 + i * 50, 100],
                                 [50 + i * 50, 100], [50 + i * 50, 0]], 1, "Red", "Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()
