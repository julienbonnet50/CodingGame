import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Board:
    def __init__(self):
        self.cards = []
        self.cardsOnMyBoard = []
        self.cardsOppositeBoard = []
        self.cardsInHand = []

    def sortCard(self):
        for card in self.cards:
            if card.location == 0:
                self.cardsInHand.append(card)
            elif card.location == 1:
                self.cardsOnMyBoard.append(card)
            elif card.location == -1:
                self.cardsOppositeBoard.append(card)

    def evaluateCardPossibleToPlay(self, mana):
        cardsNumberToPlay = []
        for card in self.cardsInHand:
            if card.cost <= mana:
                cardsNumberToPlay.append(card.instanceId)
        return cardsNumberToPlay

    def choseCardToSummon(self, cards):
        if len(cards) < 1:
            return -1
        else :
            return cards[0]

    def printSummon(self, int):
        if int < 0 or self.countCardOnBoard() > 5:
            return "PASS"
        else :
            return "SUMMON " + str(int)

    def evaluateSummonPlay(self):
        actionForSummon = ""
        # If board contains less than 5 cards
        if len(self.cardsOnMyBoard) > 0:
            if len(self.cardsOppositeBoard) < 1:
                for card in self.cardsOnMyBoard:
                    actionForSummon += "ATTACK " + str(card.instanceId) + " -1;"
            elif len(self.cardsOppositeBoard) > 1:
                for card in self.cardsOnMyBoard:
                    actionForSummon += "ATTACK " + str(card.instanceId) + " " + str(self.cardsOppositeBoard[random.randint(0, len(self.cardsOppositeBoard))-1].instanceId) + ";"

            return actionForSummon

        else:
            # board is Full
            return ""


    def countCardOnBoard(self):
        count = 0
        for card in self.cards:
            if card.location == 1:
                count+=1
        return count

    def evaluateCard(self):
        return random.randint(0, 2)

    def addCard(self, cardToAdd):
        self.cards.append(cardToAdd)

    # Main turn function
    def doTurn(self):
        turnStatements = ""

        # Chose a card to summon
        if len(self.cardsOnMyBoard) < 5:
            turnStatements += self.printSummon(self.choseCardToSummon(cardToPlay)) + ";"

        # For each card in my board
        turnStatements += self.evaluateSummonPlay()

        return turnStatements

class Card:
    def __init__(self, cardNumber, instanceId, location, cardType, cost, attack, defense, abilities, myHealthChange, opponentHealthChange, cardDraw):
        self.cardNumber = cardNumber
        self.instanceId = instanceId
        self.location = location
        self.cardType = cardType
        self.cost = cost
        self.attack = attack
        self.defense = defense
        self.abilities = abilities
        self.myHealthChange = myHealthChange
        self.opponentHealthChange = opponentHealthChange
        self.cardDraw = cardDraw

        # Abilities
        self.breakThough = "false"
        self.charge = "false"
        self.guard = "false"


    def __str__(self):
        return (f"CardNumber: {self.cardNumber}, InstanceId: {self.instanceId}, Location: {self.location}, "
                f"CardType: {self.cardType}, Cost: {self.cost}, Attack: {self.attack}, "
                f"Defense: {self.defense}, Abilities: {self.abilities}, "
                f"MyHealthChange: {self.myHealthChange}, OpponentHealthChange: {self.opponentHealthChange}, "
                f"CardDraw: {self.cardDraw}"
                f"CardBreakthough: {self.breakThough}, CardCharge: {self.charge}, CardGuard: {self.guard}")

    def giveAbilitiesAttributes(self):
        if "B" in self.abilities:
            self.breakThough = "true"
        elif "G" in self.abilities:
            self.guard = "true"
        elif "C" in self.abilities:
            self.charge = "true"

class Player:
    def __init__(self, health, mana, deck, rune, draw):
        self.health = health
        self.mana = mana
        self.deck = deck
        self.rune = rune
        self.draw = draw

turnCount = 0

# game loop
while True:
    player = Player(0, 0, 0, 0, 0)
    opponent = Player(0, 0, 0, 0, 0)
    board = Board()
    for i in range(2):
        player_health, player_mana, player_deck, player_rune, player_draw = [int(j) for j in input().split()]
        if i == 0:
            player = Player(player_health, player_mana, player_deck, player_rune, player_draw)
        else:
            opponent = Player(player_health, player_mana, player_deck, player_rune, player_draw)

    opponent_hand, opponent_actions = [int(i) for i in input().split()]
    for i in range(opponent_actions):
        card_number_and_action = input()
    card_count = int(input())
    for i in range(card_count):
        inputs = input().split()
        card_number = int(inputs[0])
        instance_id = int(inputs[1])
        location = int(inputs[2])
        card_type = int(inputs[3])
        cost = int(inputs[4])
        attack = int(inputs[5])
        defense = int(inputs[6])
        abilities = inputs[7]
        my_health_change = int(inputs[8])
        opponent_health_change = int(inputs[9])
        card_draw = int(inputs[10])

        currentCard = Card(card_number, instance_id, location, card_type, cost, attack, defense, abilities, my_health_change, opponent_health_change, card_draw)
        currentCard.giveAbilitiesAttributes()
        board.addCard(currentCard)

    # Sorting board cards into Hand, myBoard and Opposite board
    board.sortCard()

    # Printing all cards on board
    for card in board.cards:
        print(card, file=sys.stderr, flush=True)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Phase de Draft
    if turnCount < 30:
        # Choix d'une carte aléatoire
        # TODO : Choisir les meilleures cartes à drafter
        print("PICK " + str(board.evaluateCard()))

    else:
        # Jouer après le draft
        cardToPlay = board.evaluateCardPossibleToPlay(player.mana)
        print("Card to play:", cardToPlay, "then player mana:", player.mana, file=sys.stderr, flush=True)
        print("choseCardToSummon:", board.choseCardToSummon(cardToPlay), file=sys.stderr, flush=True)
        print("Evualate summon to play : " + board.evaluateSummonPlay(),  file=sys.stderr, flush=True)

        print(board.doTurn())

    turnCount += 1
    board = None