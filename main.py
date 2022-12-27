import random

from rich import print

from data import blue, yellow, green, red, Marble, players, cardCount, deck, board, someoneWon, Action, Cards

for player in players:
    for i in range(0, 4):
        player.marbles.append(Marble(pos=None, onHomebase=True))
    for i in range(0, cardCount):
        player.hand.append(deck.drawCard())

cardCount = cardCount - 1

from view import generateBoard

generateBoard()
input("Got cards\n")

for player in players:
    player.giveCard(player.hand[0])

for player in players:
    player.takeCard()

generateBoard()
input("Exchanged cards\n")

def playTurn(players):
    player = [player for player in players if player.myTurn][0]
    actionsAvailable = []
    cardsAvailable = []

    cardsAvailable += [card for card in player.hand if Action.STEAL in card.value['Actions']]
    if any([card for card in player.hand if Action.STEAL in card.value['Actions']]):
        actionsAvailable.append(Action.STEAL)
    cardsAvailable += [card for card in player.hand if Action.JOKER in card.value['Actions']]
    if any([card for card in player.hand if Action.JOKER in card.value['Actions']]):
        actionsAvailable.append(Action.JOKER)

    if sum([marble.onHomebase for marble in player.marbles]) != 0:
        if board[player.startPos] == None or board[player.startPos].freshOnSpawn == False:
            cardsAvailable += [card for card in player.hand if Action.LEAVEHOMEBASE in card.value['Actions']]
            if any([card for card in player.hand if Action.LEAVEHOMEBASE in card.value['Actions']]):
                actionsAvailable.append(Action.LEAVEHOMEBASE)
    for marble in player.marbles:
        highestMoveNum = 0
        anyNotFreshOnSpawn = False
        if not marble.onHomebase:
            if not marble.freshOnSpawn:
                anyNotFreshOnSpawn = True
            moveNum = marble.calculateAvailableSpaces()
            if moveNum > highestMoveNum:
                highestMoveNum = moveNum
    cardsAvailable += [card for card in player.hand if card.value['Value'] != None and any([value for value in card.value['Value'] if value <= highestMoveNum])]
    if any([card for card in player.hand if card.value['Value'] != None and any([value for value in card.value['Value'] if value <= highestMoveNum])]):
        actionsAvailable += [Action.MOVE, Action.MOVEFINISH]
    if anyNotFreshOnSpawn:
        addJonge = False
        for marble in player.partner.marbles:
            if not marble.onHomebase:
                if not marble.freshOnSpawn:
                    addJonge = True
        if addJonge:
            cardsAvailable += [card for card in player.hand if Action.EXCHANGE in card.value['Actions']]
            if any([card for card in player.hand if Action.EXCHANGE in card.value['Actions']]):
                actionsAvailable.append(Action.EXCHANGE)

    if cardsAvailable == []:
        player.hand = []
    else:
        print([card.name for card in cardsAvailable])
        selectedCard = input(f"What card should {player.color} play? ")
        for card in cardsAvailable:
            if card.name == selectedCard:
                break
        print([action.name for action in actionsAvailable if action in card.value['Actions']])
        selectedAction = input(f"What action do you want to do? ")
        for action in actionsAvailable:
            if action.name == selectedAction:
                break
        player.playCard(card, action, None)

    player.myTurn = False
    if player.color == "blue":
        green.myTurn = True
    elif player.color == "green":
        red.myTurn = True
    elif player.color == "red":
        yellow.myTurn = True
    elif player.color == "yellow":
        blue.myTurn = True

turn = 1
while someoneWon == False:
    playTurn(players)
    generateBoard()
    input(f"End of turn {turn}\n")
    turn = turn + 1
player = [player for player in players if player.myTurn][0]
print(player.color)
