import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
          'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        completeDeck = ''
        for card in self.deck:
            completeDeck += '\n' + card.__str__()
        return "The deck has: " + completeDeck

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand():
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        # 'card' passed in will be from deck 
        
        self.cards.append(card)
        self.value += values[card.rank]
    	
        # track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, your bet can't exceed {chips.total}")
            else:
                break

def hit(deck,hand):
    
    singleCard = deck.eal()
    hand.add_card(singleCard)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input('Hit or Stand? Enter h or s')
        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        
        else:
            print("Error! Please enter 'h' or 's' only.")
            continue
        
        break

def show_some(player,dealer):
    
    print('Dealers Hand:')
    print('one card hidden')
    print(dealer.cards[1])
    print('\n')
    print('Players Hand:')
    for card in player.cards:
        print(card)
        
def show_all(player,dealer):
    
    pirnt('Dealers hand:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Players hand:')
    for card in player.cards:
        print(card)

def player_busts(player,dealer,chips):
    print("Bust player!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Player Wins! Dealer Busted!')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print('Dealer and player tie! PUSH')

while True:
    # Print an opening statement
    
    print("BLACKJACK 21!")
    
    # Create & shuffle the deck, deal two cards to each player
    
    deck = Deck()
    deck.shuffle()
    
    playerHand = Hand()
    playerHand.add_card(deck.deal())
    playerHand.add_card(deck.deal())
    
    dealerHand = Hand()
    dealerHand.add_card(deck.deal())
    dealerHand.add_card(deck.deal())
    
    # Set up the Player's chips
    
    playerChips = Chips()
    
    
    # Prompt the Player for their bet
    
    take_bet(playerChips)
    
    # Show cards (but keep one dealer card hidden)

    show_some(playerHand,dealerHand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,playerHand)
        
        # Show cards (but keep one dealer card hidden)
        
        show_some(playerHand,dealerHand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        
        if playerHand.value > 21:
            player_busts(playerHand,dealerHand,playerChips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if playerHand.value <= 21:
        
        while dealerHand.value < 17:
            hit(deck,dealerHand)
    
        # Show all cards
        
        show_all(playerHand,dealerHand)
        
        # Run different winning scenarios
        
        if dealerHand.value > 21:
            dealer_busts(playerHand,dealerHand,playerChips)
        elif dealerHand.value > playerHand.value:
            dealer_wins(playerHand,dealerHand,playerChips)
        elif dealerHand.value < playerHand.value:
            player_wins(playerHand,dealerHand,playerChips)
        else:
            push(playerHand,dealerHand)
    # Inform Player of their chips total 
    
    print(f'\n Player total chips are at: {playerChips.total}')
    
    # Ask to play again
    
    newGame = input("Would you like to play another hand? y/n")
    
    if newGame[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing')
        break