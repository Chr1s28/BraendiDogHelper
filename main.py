import random

from rich import print

from data import blue, yellow, green, red, Marble, players, cardCount, deck, getOutList, board, someoneWon

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
    cardsAvailable = player.hand
    if sum([marble.onHomebase for marble in player.marbles]) == 4:
        cardsAvailable = [card for card in cardsAvailable if card.value in getOutList]
    if cardsAvailable == []:
        player.hand = []
    else:
        print([card.value for card in cardsAvailable])
        selectedCard = input(f"What card should {player.color} play? ")
        action = input(f"What action do you want to do? ")
        for card in cardsAvailable:
            if str(card.value) == selectedCard:
                player.playCard(card, action)
                break
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
