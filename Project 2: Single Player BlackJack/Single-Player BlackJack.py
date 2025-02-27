'''
Project 2: BlackJack
'''

import random

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack': 10, 'King':10, 'Queen':10, 'Ace': 11,}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'King', 'Queen', 'Ace')

playing = True

class Card:

    ''' A class that creates a card with a specific value, rank, & suit '''

    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    ''' A class that instantiates a new deck of 52 cards, holds a list of the card, shuffles the deck,
    and deals a card.'''

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:

                created_card = Card(rank,suit)
                self.all_cards.append(created_card)

    def shuffle(self):
        # Shuffles the Created Deck of Cards
        random.shuffle(self.all_cards)

    def deal(self):
        # Deals one card from the deck
        single_card = self.all_cards.pop()
        return single_card

class Hand:

    ''' A class that stores, creates, and deals a hand for each player in the game '''

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):

        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet?: "))

        except:
            print("Your entry is invalid. Please try again.\n")

        else:
            if chips.bet > chips.total:
                print(f'You do not have enough money to make this bet. You have only ${chips.total} in your pot\n')

            else:
                break

def hit(deck,hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:

        x = input('Please (H) to Hit or (S) to Stand: ')

        if x.lower() == 'h':
            hit(deck,hand)

        elif x.lower() == 's':
            print('Dealer\'s Turn')
            playing = False

        else:
            print('Your entry is invalid. Please try again\n')
            continue

        break

def show_some(player,dealer):

    print(f'\nDealer\'s Hand: {dealer.cards[1]}')
    print(f'Dealers\'s Deck Value: {dealer.cards[1].value}')

    print('\nPlayer\'s Hand: ',*player.cards, sep=" | ")
    print(f'Player\'s Deck Value: {player.value}')
    print('')

def show_all(player,dealer):

    print('\nDealer\'s Hand: ', *dealer.cards, sep= ' | ')
    print(f'Dealer\'s Deck Value: {dealer.value}')
    print('')

    print('\nPlayer\'s Hand: ', *player.cards, sep= ' | ')
    print(f'Player\'s deck Value: {player.value}')

def player_busts(player,dealer,chips):
    print('Player Bust')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player Wins')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Dealer Bust')
    chips.lose_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer Wins')
    chips.win_bet()

def push(player,dealer):
    print('Push. It\'s a tie')

def how_to_play():
    print('-'*300)
    print('How to play BlackJack-:\n')
    print("Blackjack is a standard 52 card casino game where each player’s objective is to “beat the dealer” by getting their deck of cards closest to the value 21 without going over 21.\nIf a player goes over 21, they've gone BUST and the player loses their placed bet. The game will officially continue until the player either runs out of money or decides to 'cash out' and leave the game.\n")
    print('Card Value\n\t1.) Each card within the 52 card deck has a specified face value or number of points when drawn and added to a player’s deck')
    print('\t2.) The Face Cards (10 points) -: Joker, King, and Queens\n\t3.) 2-10 Cards (Face Value) -: Any card with a number on it equals it’s face value\n\t4.) Aces -: An Ace card can either count as either 1 or 11 points\n')
    print('Player Moves\n\tEach player is given a choice of 4 moves -:\n\n\t1.) Hit \n\t\tA Hit means that the player wants the dealer to give them another card drawn from the deck\n\t\tA player can ‘Hit’ as many times as they choose, as long as their deck of cards does not go over 21\n')
    print('\t2.) Stand\n\t\tA Stand means that a player does not want a cards from the deck. The player would skip their turn, and the dealer would move on the next player\n')
    print('\t3.) Split\n\t\tIf a player receives two cards of the same rank, they can choose to ‘Split’.\n\t\tA split allows a player to split their deck into two with each card acting as the base for the respective decks. For example -: If a player received two 2 of Hearts')
    print('\t\tFor a player to split, they must place another bet equal to the bet of their original bet for the new deck that was created\n\t\tThe player would be allow to hit or stand for both decks\n')
    print('\t4.) Double Down\n\t\tPlayers can increase the size of their initial bet by 100% or double, but, in doing so, the player is only allowed one extra card, and would have to stand for the rest of the game.')
    print('\t\tPlayers can only double down after the first two initial cards have been dealt. You can not “hit” then double down after the initial hit. You can’t have more than 3 cards then double down.\n')
    print('Rules\n\t1.) At the beginning of each round or game, players must place a bet before the dealer can give them any cards.')
    print('\t2.) If a player is deal ‘21’ on the first two dealt cards, this is called a BlackJack or Natural. This player automatically wins the round with a payout of 3:2. For every two “chips” I bet, I receive 3 ‘chips’ from the dealer.')
    print('\t3.) If a player has a higher face value that the dealer or if the dealer goes bust. Each player that has a high face value than the dealer would receive a payout equal to their original bet. For example -: If I bet $200, the dealer would pay $200 if I won against the dealer')
    print('\t4.) If a player and the dealer tie, and the player get to keep their bet. This is called a “Push”')
    print('\t5.) If a dealer has a hand that is 16 or less in face value, the dealer must “Hit”')
    print('\t6.) If a dealer has a hand that is 17 or more, they are forced to “Stand”\n')
    print('Here are all the rules on how to play BlackJack')

    print('-' * 300)

if __name__ == "__main__":
    print('Welcome to the BlackJack\n')
    while True:
        instructions = input('Would you like to see the rules of how to play BlackJack, then Press "Y". If not, then press "N" : ')
        instructions = instructions.strip()
        print('')

        if instructions.upper() == "Y":
            how_to_play()
            break

        elif instructions.upper() == "N":
            break

        else:
            print('Your entry was invalid. Press "Y" to learn how to play, or Press "N" to continue\n')

    print('At the start of each game, players will be given $100.\n')
    print('-'*300)
    print('')

    print('START')

    while True:

        # Create a 52 card deck
        deck = Deck()
        deck.shuffle()

        # Deal the first two player cards
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        # Deal the first two dealer cards
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Ask the player to make a bet
        player_chips = Chips()

        # Store the bet
        take_bet(player_chips)

        #Show the player's deck and one of the dealer's cards
        show_some(player_hand, dealer_hand)

        while playing:
            # Ask the player if they would like to "Hit" or "Stand"
            hit_or_stand(deck,player_hand)

            # Show the player's hand compared to the dealer
            show_some(player_hand, dealer_hand)

            # Check if the player has bust
            if player_hand.value > 21:

                player_busts(player_hand, dealer_hand, player_chips)
                break

        if player_hand.value <= 21:

            # Deal a card if the dealer's hand is less than 17
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)

            show_all(player_hand,dealer_hand)

            # Checks if the dealer has bust
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

            # Checks if the dealer has won
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            # Checks if there is a tie
            else:
                push(player_hand,dealer_hand)

        # Show the player their total pot
        print(f'\nPlayer total chips: {player_chips.total}')

        new_game = input('Would you like to play again. Press \'Y\' to continue or \'N\': ')
        print('')

        if new_game.lower() == 'y':
            playing = True
            continue

        else:
            print('Thank you for playing!!!\n')
            break
```
