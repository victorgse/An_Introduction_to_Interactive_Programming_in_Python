# Rock-paper-scissors-lizard-Spock


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def number_to_name(number):
    """
    converts number to a name and returns the result
    """
    
    if number == 0:
        name = 'rock'
        return name
    elif number == 1:
        name = 'Spock'
        return name
    elif number == 2:
        name = 'paper'
        return name
    elif number == 3:
        name = 'lizard'
        return name
    elif number == 4:
        name = 'scissors'
        return name
    else:
        print "Error: number not in correct range"
    
def name_to_number(name):
    """
    converts name to a number and returns the result
    """
    
    if name == 'rock':
        number = 0
        return number
    elif name == 'Spock':
        number = 1
        return number
    elif name == 'paper':
        number = 2
        return number
    elif name == 'lizard':
        number = 3
        return number
    elif name == 'scissors':
        number = 4
        return number
    else:
        print "Error: invalid entry"

# main function
        
def rpsls(name):

    # converts name to player_number using name_to_number
    player_number = name_to_number(name)
    
    # computes a random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
   
    # computes the difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5
    
    # determines winner
    if (difference == 1) or (difference == 2):
        winner = 'Player wins!'
    elif (difference == 3) or (difference == 4):
        winner = 'Computer wins!'
    else:
        winner = 'Player and computer tie!'

    # converts player_number to name using number_to_name
    player_guess = number_to_name(player_number)
  
    # converts comp_number to name using number_to_name
    computer_guess = number_to_name(comp_number)
   
    # prints results
    print
    print 'Player chooses', player_guess
    print 'Computer chooses', computer_guess
    print winner
    
# tests the code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
