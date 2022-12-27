from enum import Enum
import random

class Player:
    def __init__(self, color, startPos, marbles, hand, myTurn) -> None:
        self.color = color
        self.partner = None
        self.startPos = startPos
        self.marbles = marbles
        self.hand = hand
        self.cardFromPartner = None
        self.myTurn = myTurn
        self.finish = [None]*4
    
    def draw(self, deck):
        self.hand.append(deck.drawCard())

    def giveCard(self, card):
        if card in self.hand:
            self.hand.remove(card)
            self.partner.cardFromPartner = card
    
    def takeCard(self):
        self.hand.append(self.cardFromPartner)
        self.cardFromPartner = None
    
    def stealCard(self, player):
        stolenCard = random.choice(player.hand)
        self.hand.append(stolenCard)
        player.hand.remove(stolenCard)
    
    def playCard(self, card, action):
        global board
        self.hand.remove(card)
        playedCardStack.append(card)

        if action == Action.LEAVEHOMEBASE:
            if board[self.startPos] != None:
                board[self.startPos].pos = None
                board[self.startPos].onHomebase = True
            self.marbles[-1].onHomebase = False
            self.marbles[-1].freshOnSpawn = True
            self.marbles[-1].pos = self.startPos
            board[self.startPos] = self.marbles[-1]
        elif action == Action.MOVE:


class Action(Enum):
    MOVE = 1
    MOVEFINISH = 2
    LEAVEHOMEBASE = 3
    STEAL = 4
    EXCHANGE = 5

class Marble:
    def __init__(self, pos, onHomebase) -> None:
        self.pos = pos
        self.onHomebase = onHomebase
        self.freshOnSpawn = None
    
    def calculateAvailableSpaces(self):
        maxMove = 0
        for i in range(1, 14):
            if board[self.pos+i] == None:
                maxMove = i
            elif not board[self.pos+i].freshOnSpawn:
                maxMove = i

class Deck:
    def __init__(self) -> None:
        self.cards = []

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))
        self.cards.append(Card(suit=None, value="Joker"))
        self.cards.append(Card(suit=None, value="Joker"))
    
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0 , i)
            self.cards[i], self.cards[r] = self.cards[r] , self.cards[i]
    
    def drawCard(self):
        return self.cards.pop()

class Card:
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value

getOutList = [1, 13, "Joker"]

board = [None]*64
players = []
someoneWon = False
cardCount = 6
deck = Deck()
deck.build()
deck.shuffle()

playedCardStack = []

blue = Player(color="blue", startPos=0, marbles=[], hand=[], myTurn=True)
players.append(blue)

green = Player(color="green", startPos=16, marbles=[], hand=[], myTurn=False)
players.append(green)

red = Player(color="red", startPos=32, marbles=[], hand=[], myTurn=False)
players.append(red)

yellow = Player(color="yellow", startPos=48, marbles=[], hand=[], myTurn=False)
players.append(yellow)

blue.partner = red
red.partner = blue
green.partner = yellow
yellow.partner = green