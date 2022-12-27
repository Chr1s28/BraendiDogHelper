from rich.console import Console
console = Console()

from data import yellow, red, blue, green, playedCardStack, board

boardString = ""

def generateBoard():
    global boardString

    boardString = ""

    checkPlayerBase(yellow, 0, False)
    for j in range(0, 17):
        index = (j * -1) + 48
        if j == 0:
            checkNormalSpace(index, "yellow")
        elif j == 16:
            checkNormalSpace(index, "red")
        else:
            checkNormalSpace(index)
    checkPlayerBase(red, 0, True)

    checkPlayerBase(yellow, 1, False)
    checkNormalSpace(49)
    checkPlayerFinish(yellow, 0, False)
    boardString += "                                       "
    checkPlayerFinish(red, 0, True)
    checkNormalSpace(31)
    checkPlayerBase(red, 1, True)

    checkPlayerBase(yellow, 2, False)
    checkNormalSpace(50)
    checkPlayerFinish(yellow, 1, False)
    boardString += "                                 "
    checkPlayerFinish(red, 1, True)
    checkNormalSpace(30)
    checkPlayerBase(red, 2, True)

    checkPlayerBase(yellow, 3, False)
    checkNormalSpace(51)
    checkPlayerFinish(yellow, 2, False)
    boardString += "                           "
    checkPlayerFinish(red, 2, True)
    checkNormalSpace(29)
    checkPlayerBase(red, 3, True)

    boardString += f" [yellow]{len(yellow.hand)}  "
    checkNormalSpace(52)
    checkPlayerFinish(yellow, 3, False)
    boardString += "                     "
    checkPlayerFinish(red, 3, True)
    checkNormalSpace(28)
    boardString += f"  [red]{len(red.hand)}"

    boardString += "\n    "
    checkNormalSpace(53)
    boardString += "                                             "
    checkNormalSpace(27)

    boardString += "\n    "
    checkNormalSpace(54)
    boardString += "                                             "
    checkNormalSpace(26)

    boardString += "\n    "
    checkNormalSpace(55)
    boardString += "                                             "
    checkNormalSpace(25)

    boardString += "\n    "
    checkNormalSpace(56)
    if len(playedCardStack) > 0:
        card = (playedCardStack[-1])
        if card.value == 1:
            cardString = f"Ass"
        elif card.value == 11:
            cardString = f"Jonge"
        elif card.value == 12:
            cardString = f"Queen"
        elif card.value == 13:
            cardString = f"King"
        else:
            cardString = str(card.value)
    else:
        cardString = None
    boardString += f" Last played card: {cardString}			    "
    checkNormalSpace(24)

    boardString += "\n    "
    checkNormalSpace(57)
    boardString += "                                             "
    checkNormalSpace(23)

    boardString += "\n    "
    checkNormalSpace(58)
    boardString += "                                             "
    checkNormalSpace(22)

    boardString += "\n    "
    checkNormalSpace(59)
    boardString += "                                             "
    checkNormalSpace(21)

    boardString += f"\n [blue]{len(blue.hand)}  "
    checkNormalSpace(60)
    checkPlayerFinish(blue, 3, False)
    boardString += "                     "
    checkPlayerFinish(green, 3, True)
    checkNormalSpace(20)
    boardString += f"  [green]{len(green.hand)}"

    boardString += "\n"
    checkPlayerBase(blue, 3, False)
    checkNormalSpace(61)
    checkPlayerFinish(blue, 2, False)
    boardString += "                           "
    checkPlayerFinish(green, 2, True)
    checkNormalSpace(19)
    checkPlayerBase(green, 3, True)

    checkPlayerBase(blue, 2, False)
    checkNormalSpace(62)
    checkPlayerFinish(blue, 1, False)
    boardString += "                                 "
    checkPlayerFinish(green, 1, True)
    checkNormalSpace(18)
    checkPlayerBase(green, 2, True)

    checkPlayerBase(blue, 1, False)
    checkNormalSpace(63)
    checkPlayerFinish(blue, 0, False)
    boardString += "                                       "
    checkPlayerFinish(green, 0, True)
    checkNormalSpace(17)
    checkPlayerBase(green, 1, True)

    checkPlayerBase(blue, 0, False)
    for j in range(0, 17):
        if j == 0:
            checkNormalSpace(j, "blue")
        elif j == 16:
            checkNormalSpace(j, "green")
        else:
            checkNormalSpace(j)
    checkPlayerBase(green, 0, True)

    handString = ""
    for card in blue.hand:
        if card.value == 1:
            handString += f"Ass "
        elif card.value == 11:
            handString += f"Jonge "
        elif card.value == 12:
            handString += f"Queen "
        elif card.value == 13:
            handString += f"King "
        else:
            handString += f"{card.value} "
    boardString += "[blue]	Hand: "+handString+"\n"

    console.print(boardString)

def checkNormalSpace(index, spaceColor="white"):
    global boardString
    if board[index] == None:
        boardString += f"[{spaceColor}][ ]"
    else:
        boardString += f"[{spaceColor}][●]"

def checkPlayerBase(player, index, end):
    global boardString
    if end:
        if sum([marble.onHomebase for marble in player.marbles]) >= index+1:
            boardString += f" [{player.color}][●]\n"
        else:
            boardString += f" [{player.color}][ ]\n"
    else:
        if sum([marble.onHomebase for marble in player.marbles]) >= index+1:
            boardString += f"[{player.color}][●] "
        else:
            boardString += f"[{player.color}][ ] "

def checkPlayerFinish(player, index, end):
    global boardString
    finishString = ""
    if end:
        if player.finish[index] == None:
            finishString += f"[{player.color}][ ]" + "   "*index
        else:
            finishString += f"[{player.color}][●]" + "   "*index
    else:
        if player.finish[index] == None:
            finishString += "   "*index + f"[{player.color}][ ]"
        else:
            finishString += "   "*index + f"[{player.color}][●]"
    boardString += finishString
