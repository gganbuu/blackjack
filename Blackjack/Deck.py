import random 
# class Card:
#     # create card
#     def __init__(self, card_number, card_suit):
#         self.card_number = card_number
#         self.card_suit = card_suit
    
#     #get card
#     def get_card(self):
#         return(self.card_number, self.card_suit)
class Dealer:
    def __init__(self):
        self.name = ''
        self.hand = []
    pass

    def isBlackjack(self):
        values = []
        for value in range(len(self.hand)): 
            values.append(self.hand[value][0])
        if 'K' in values or 'Q' in values or 'J' in values or 10 in values:
            if 1 in values:
                return True
        return False

    def calculateTotal(self):
        total = 0
        if self.isBlackjack():
            return True
        for card in range(len(self.hand)):
            if (self.hand[card][0] == 'K' or 
                self.hand[card][0] == 'Q' or 
                self.hand[card][0] == 'J'):
                total+=10
            else:
                total+=self.hand[card][0]
        return total

    def setHand(self, cards):
        self.hand.extend(cards)
        
    

class Table:
    def __init__(self, shoes):
        self.deck = Shoe(shoes)
        self.player = Player()
        self.dealer = Dealer()
    
    def playBlackjack(self):
        # create player name and add money
        self.player.name = 'Tim' # input('Enter your name: ')
        self.player.cash = 400 # input('How much money: ')

        # print("Welcome to the Tim's Casino")
        # input('Type "s" to play Blackjack, and "q" to quit')
        
        #print balance and enter bet
        
        self.player.placeBet(int(input("Amount to bet:")))

        #shuffle deck and deal cards
        self.deck.shuffle()
        self.dealer.setHand(self.deck.deal(2))
        self.player.setHand(self.deck.deal(2))
        print("The dealer is showing " + str(self.dealer.hand[0]))
        print("You have turned " + str(self.player.hand))
    
    def hit(self):
        pass

    def hitAble(self):
        pass

    def split(self):
        pass
    
    def splitAble(self):
        pass

    def stand(self):
        pass


    
    def wins(self, player, dealer):
        if player.calculateTotal() > dealer.calculateTotal():
            print('Player wins!')
        elif player.calculateTotal() < dealer.calculateTotal():
            print('Dealer wins')
        else:
            print('Push!')
    


class Player:
    def __init__(self):
        self.cash = 0
        self.bet = 0
        self.name = ''
        self.hand = []

    def isDouble(self):
        if self.hand[0][0] == self.hand[1][0]:
            return True
        return False
    
    def isBlackjack(self):
        values = []
        for value in range(len(self.hand)): 
            values.append(self.hand[value][0])
        if 'K' in values or 'Q' in values or 'J' in values or 10 in values:
            if 1 in values:
                return True
        return False

    def calculateTotal(self):
        total = 0
        if self.isBlackjack():
            return 'Blackjack!'
        for card in range(len(self.hand)):
            if (self.hand[card][0] == 'K' or 
                self.hand[card][0] == 'Q' or 
                self.hand[card][0] == 'J'):
                total+=10
            else:
                total+=self.hand[card][0]
        return total
    
    def setHand(self, cards):
        self.hand.extend(cards)

    def placeBet(self, amount):
        self.cash-=amount
        self.bet+=amount
        
        

class Shoe:
    def __init__(self, number_of_decks):
        #initialises and creates deck of cards.
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        numbers = [1,2,3,4,5,6,7,8,9,10,'J','Q','K']
        cards = []
        for i in range(number_of_decks):
            for suit in suits:
                for number in numbers:
                    card = (number, suit)
                    cards.append(card)
            i+=1
        self.cards = cards

    def printDeck(self):
        #prints all decks card in its entirety
        print(self.cards)


    def deal(self, number_of_cards):
        # deals cards, removing dealt from deck, takes in parameter that 
        # specifies amount of cards dealt
        dealtCards = []
        for i in range(number_of_cards):
            dealtCards.append(self.cards[0])
            del self.cards[0]
            i+=1
        return dealtCards
    
    def shuffle(self):
        #shuffles card
        random.shuffle(self.cards)

table = Table(1)
table.playBlackjack()






        
        

        

