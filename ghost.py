import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

def is_word(s, wordlist):
    if s in wordlist:
        return True
    else:
        return False
        
def is_fragment(s, wordlist):
    for word in wordlist:
        if s in word:
            return False
    return True

def whose_turn(turn, players):
    if players == 2:
        if turn%2 == 1:
            return 'Player 1'
        else:
            return 'Player 2'
    elif players == 3:
        if turn%3 == 1:
            return 'Player 1'
        elif turn%3 == 2:
            return 'Player 2'
        else:
            return 'Player 3'
        
def valid_move(s):
    if len(s) == 1 and s in string.ascii_letters:
        return True
    else:
        return False
        
def play_again():
    print "Play again? y/n"
    choice = raw_input('> ')
    if choice == 'y':
        ghost()
    elif choice == 'n':
        print "Thanks for playing!"
        exit(0)
    else:
        print "Invalid command!"
        play_again()
             
def ghost():
    turn = 1
    char = ''
    word = ''
    print "Welcome to Ghost!"
    print "Do you want a 2 or 3 player game?"
    players = raw_input('> ')
    while players != '2' and players != '3':
        print "Invalid number!"
        players = raw_input('> ')
        
    players = int(players) 
    while True:
        
        
        print "It is %s's turn." % whose_turn(turn, players)
        print "Current word fragment: %s" % word
        char = raw_input('> ')
        char = char.lower().strip()
        while valid_move(char) == False:
            print "Invalid move!"
            char = raw_input('> ')
            char = char.lower().strip()
        word += char
        
        if len(word) > 3 and valid_move(char):
            if is_word(word, wordlist):
                print "%s is a word. %s loses!" % (word, whose_turn(turn, players))
                play_again()
                
            elif is_fragment(word, wordlist):
                print "No word begins with %s. %s loses!" % (word, whose_turn(turn, players))
                play_again()
        elif len(word) <= 3 and valid_move(char):
            if is_fragment(word, wordlist):
                print "No word begins with %s. %s loses!" % (word, whose_turn(turn, players))
                play_again()    
        turn += 1

ghost()


