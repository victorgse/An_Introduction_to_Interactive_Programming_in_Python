# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
player_choice = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        ans = ""
        for i in range(len(self.hand)):
            ans += str(self.hand[i]) + " "
        return "Hand contains " + ans

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # compute the value of the hand
        hand_value = sum(VALUES[card.get_rank()] for card in self.hand)
        
        if hand_value == 0:
            return 0
        else:
            for card in self.hand:
                if 'A' != card.get_rank():
                    return hand_value
                elif hand_value + 10 <= 21:
                    return hand_value + 10
                else:
                    return hand_value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas,pos)
            pos[0] += 100
         
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in range(len(SUITS)):
            for rank in range(len(RANKS)):
                self.deck.append(SUITS[suit] + RANKS[rank])        

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.deck)        
        
    def deal_card(self):
        # deal a card object from the deck
        dealt_card = self.deck.pop()
        return Card(dealt_card[0], dealt_card[1])        
    
    def __str__(self):
        # return a string representing the deck
        ans = ""
        for i in range(len(self.deck)):
            ans += str(self.deck[i]) + " "
        return "Deck contains " + ans

#define event handlers for buttons
def deal():
    global outcome, player_choice, in_play, score, deck, player_hand, dealer_hand
    outcome = ""
    player_choice = "Hit or Stand?"
    if in_play == True:
        outcome = "You lose."
        score -= 1
    in_play = True

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()
    
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())       

def hit():
    global outcome, player_choice, in_play, score
    # if the hand is in play, hit the player
    if in_play == True:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
            outcome = ""
   
    # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "You went bust. You lose."
            player_choice = "New deal?"
            in_play = False
            score -= 1
       
def stand():
    global outcome, player_choice, in_play, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        
    # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() > 21:
            outcome = "Dealer went bust. You win."
            player_choice = "New deal?"
            in_play = False
            score += 1
        elif dealer_hand.get_value() >= player_hand.get_value():
            outcome = "You lose."
            player_choice = "New deal?"
            in_play = False
            score -= 1
        else:
            outcome = "You win."
            player_choice = "New deal?"
            in_play = False
            score += 1

# draw handler    
def draw(canvas):
    dealer_hand.draw(canvas, [100, 200])
    player_hand.draw(canvas, [100, 400])
    canvas.draw_text("Blackjack", [120, 100], 40, "Blue")
    canvas.draw_text("Dealer", [100, 180], 30, "Black")
    canvas.draw_text("Player", [100, 380], 30, "Black")
    canvas.draw_text(outcome, [250, 180], 30, "Black")
    canvas.draw_text(player_choice, [250, 380], 30, "Black")
    canvas.draw_text("Score: " + str(score), [400, 100], 30, "Black")
    
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (136, 249), CARD_BACK_SIZE)    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
