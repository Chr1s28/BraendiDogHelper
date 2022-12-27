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
    
    def playCard(self, card, action, actionData):
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
            pass


class Action(Enum):
    MOVE = 1
    MOVEFINISH = 2
    LEAVEHOMEBASE = 3
    STEAL = 4
    EXCHANGE = 5
    JOKER = 6

class Cards(Enum):
    __order__ = 'ASS TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JONGE QUEEN KING JOKER'
    ASS = {'Value': [1, 11], 'Actions': [Action.MOVE, Action.MOVEFINISH, Action.LEAVEHOMEBASE]}
    TWO = {'Value': [2], 'Actions': [Action.MOVE, Action.MOVEFINISH, Action.STEAL]}
    THREE = {'Value': [3], 'Actions': [Action.MOVE, Action.MOVEFINISH]}
    FOUR = {'Value': [4], 'Actions': [Action.MOVE, Action.MOVEFINISH]}
    FIVE = {'Value': [5], 'Actions': [Action.MOVE, Action.MOVEFINISH]}
    SIX = {'Value': [6], 'Actions': [Action.MOVE, Action.MOVEFINISH]}
    SEVEN = {'Value': [1, 2, 3, 4, 5, 6, 7], 'Actions': [Action.MOVE, Action.MOVEFINISH]}
    EIGHT = {'Value': [8], 'Actions': [Action.MOVE, Action.MOVEFINISH]}
    NINE = {'Value': [9], 'Actions': [Action.MOVE, Action.MOVEFINISH]}
    TEN = {'Value': [10], 'Actions': [Action.MOVE, Action.MOVEFINISH]}
    JONGE = {'Value': None, 'Actions': [Action.EXCHANGE]}
    QUEEN = {'Value': [12], 'Actions': [Action.MOVE, Action.MOVEFINISH]}
    KING = {'Value': [13], 'Actions': [Action.MOVE, Action.MOVEFINISH, Action.LEAVEHOMEBASE]}
    JOKER = {'Value': None, 'Actions': [Action.JOKER]}

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
        return maxMove

class Deck:
    def __init__(self) -> None:
        self.cards = []

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(0, 13):
                self.cards.append(list(Cards)[value])
        self.cards.append(Cards.JOKER)
        self.cards.append(Cards.JOKER)
    
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0 , i)
            self.cards[i], self.cards[r] = self.cards[r] , self.cards[i]
    
    def drawCard(self):
        return self.cards.pop()

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