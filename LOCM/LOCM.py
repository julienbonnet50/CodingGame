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
<<<<<<< HEAD
        self.players = []
        self.curve = {0: 0.0, 1: 2.0, 2: 5.0, 3: 8.0, 4: 9.0, 5: 4.0, 6: 1.0, 7: 0.0, 8: 0.0, 9: 1.0, 10: 0.0}


    def setPlayers(self, player1, player2):
        self.players.append(player1)
        self.players.append(player2)

        # Adjusting real mana

    def sortCard(self):
        for card in self.cards:
            if card.location == 0:
                self.cardsInHand.append(card)
            elif card.location == 1:
                self.cardsOnMyBoard.append(card)
            elif card.location == -1:
                self.cardsOppositeBoard.append(card)
=======

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
>>>>>>> 6c05901dcb3ac4eb71ef5b42113fdb5aa67f4677

    def evaluateCardsPossibleToPlay(self):
        cardsToPlay = []
        for card in self.cardsInHand:
            if card.cost <= self.players[0].mana:
                cardsToPlay.append(card)
        return cardsToPlay

    # TODO : Better optim for chose card to summon ^^
    def choseCardToSummon(self):
        cardsToPlay = self.evaluateCardsPossibleToPlay()
        if len(cardsToPlay) < 1:
            return -1
        else :
<<<<<<< HEAD
            print("Played Card " + str(cardsToPlay[0].instanceId) + " with cost : " + str(cardsToPlay[0].cost), file=sys.stderr, flush=True)
            self.players[0].mana -= cardsToPlay[0].cost
            self.cardsInHand.remove(cardsToPlay[0])
            return cardsToPlay[0]
    
    def printSummon(self, card):
        if card == -1 or self.countCardOnBoard() > 5:
=======
            return cards[0]

    def printSummon(self, int):
        if int < 0 or self.countCardOnBoard() > 5:
>>>>>>> 6c05901dcb3ac4eb71ef5b42113fdb5aa67f4677
            return "PASS"
        else :
            return "SUMMON " + str(card.instanceId)

    def evaluateSummonPlay(self):
        actionForSummon = ""
        # If board contains less than 5 cards
        if len(self.cardsOnMyBoard) > 0:
            if len(self.cardsOppositeBoard) < 1:
                for card in self.cardsOnMyBoard:
                    actionForSummon += "ATTACK " + str(card.instanceId) + " -1;"
            elif len(self.cardsOppositeBoard) > 1:
                for card in self.cardsOnMyBoard:
<<<<<<< HEAD
                    actionForSummon += "ATTACK " + str(card.instanceId) + " " + str(self.evaluateSummonToAttack(card)) + ";"

            return actionForSummon

        else:
            # board is Full
            return ""

    def evaluateSummonToAttack(self, mySummonCard):
        # First lets check if card has attributes (Guard)
        if len(self.cardsOppositeBoard) > 0:
            for ennemiCard in self.cardsOppositeBoard:
                if ennemiCard.guard == "true":
                    self.battleBoardPreview(mySummonCard, ennemiCard)
                    return ennemiCard.instanceId
            
            cardToAttack = self.cardsOppositeBoard[0]
            self.battleBoardPreview(mySummonCard, cardToAttack)
            return cardToAttack.instanceId
        else:
            return -1

    def battleCardPreview(self, mySummonCard, ennemiCard):
        if (mySummonCard.attack >= ennemiCard.defense):
            return 1
        else:
            return 0

    def battleBoardPreview(self, mySummonCard, ennemiCard):
        if (mySummonCard.attack >= ennemiCard.defense):
            print("Card " + str(mySummonCard.instanceId) + " attack and kill card : " + str(ennemiCard.instanceId), file=sys.stderr, flush=True)
            self.deleteCard(ennemiCard)
            return

        count = 0
        for card in self.cardsOppositeBoard:
            if card == ennemiCard:
                print("Card " + str(mySummonCard.instanceId) + " attack and damage card : " + str(card.instanceId), file=sys.stderr, flush=True)
                self.cardsOppositeBoard[count].defense -= mySummonCard.attack
            count =+ 1
=======
                    actionForSummon += "ATTACK " + str(card.instanceId) + " " + str(self.cardsOppositeBoard[random.randint(0, len(self.cardsOppositeBoard))-1].instanceId) + ";"

            return actionForSummon

        else:
            # board is Full
            return ""

>>>>>>> 6c05901dcb3ac4eb71ef5b42113fdb5aa67f4677

    def countCardOnBoard(self):
        count = 0
        for card in self.cards:
            if card.location == 1:
                count+=1
        return count


    # TODO : Find a better optimisation for draft ^^
    def evaluateCard(self, turn):
        def get_weighted_score(card):
                return weighted_scores[card]

        normalized_curve = {cost: value / sum(self.curve.values()) for cost, value in self.curve.items()}
        weighted_scores = {card: normalized_curve[card.cost] for card in self.cards}

        # Choose the card with the highest weighted score
        selected_card = max(weighted_scores, key=get_weighted_score)
        count = 0
        for card in self.cards:
            if card == selected_card:  
                return count
            count += 1

    def addCard(self, cardToAdd):
        self.cards.append(cardToAdd)
    
    def deleteCard(self, cardToDelete):
        self.cardsOppositeBoard.remove(cardToDelete)

<<<<<<< HEAD
    def checkIfSummonIsCharge(self, cardInstanceId):
        statement = ""
        for card in self.cardsInHand:
            if card.instanceId == cardInstanceId:
                if card.charge == "true":
                    statement += "ATTACK " + str(card.instanceId) + " " + str(self.evaluateSummonToAttack(card)) + ";"
                    return statement
                else:
                    return statement
        return statement

    def getLowestCostCardInHand(self):
        lowestCost = 10
        for card in self.cardsInHand:
            if card.cost  < lowestCost:
                lowestCost = card.cost

        return lowestCost

    # Main turn function
    def doTurn(self):
        turnStatements = ""
        lowestCostCardInHand = self.getLowestCostCardInHand()

        # Chose a card to summon 
        if len(self.cardsOnMyBoard) < 5:
            for cardToPlay in self.cardsInHand:
                if card.cost > lowestCostCardInHand:
                    print("Card on board " + str(len(self.cardsOnMyBoard)) + " and mana available : " + str(self.players[0].mana) + " vs lowest card in Hard " + str(lowestCostCardInHand),  file=sys.stderr, flush=True)
                    turnStatements += self.printSummon(cardToPlay) + ";" + self.checkIfSummonIsCharge(cardToPlay)

        # For each card in my board
        turnStatements += self.evaluateSummonPlay()
        
=======
    # Main turn function
    def doTurn(self):
        turnStatements = ""

        # Chose a card to summon
        if len(self.cardsOnMyBoard) < 5:
            turnStatements += self.printSummon(self.choseCardToSummon(cardToPlay)) + ";"

        # For each card in my board
        turnStatements += self.evaluateSummonPlay()

>>>>>>> 6c05901dcb3ac4eb71ef5b42113fdb5aa67f4677
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
<<<<<<< HEAD
                f"CardDraw: {self.cardDraw} "
                f"CardBreakthough: {self.breakThough}, CardCharge: {self.charge}, CardGuard: {self.guard}")   
=======
                f"CardDraw: {self.cardDraw}"
                f"CardBreakthough: {self.breakThough}, CardCharge: {self.charge}, CardGuard: {self.guard}")
>>>>>>> 6c05901dcb3ac4eb71ef5b42113fdb5aa67f4677

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
    
    board.setPlayers(player, opponent)
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
<<<<<<< HEAD
    
    # Sorting board cards into Hand, myBoard and Opposite board
    board.sortCard()

    # Printing all cards on board
    print("_________Cards on board : " + str(turnCount) + "____________", file=sys.stderr, flush=True)
=======

    # Sorting board cards into Hand, myBoard and Opposite board
    board.sortCard()

    # Printing all cards on board
>>>>>>> 6c05901dcb3ac4eb71ef5b42113fdb5aa67f4677
    for card in board.cards:
        print(card, file=sys.stderr, flush=True)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Phase de Draft
    if turnCount < 30:
<<<<<<< HEAD
        # Choix d'une carte aléatoire 
        # TODO : Choisir les meilleures cartes à drafter
        print("PICK " + str(board.evaluateCard(turnCount)))
=======
        # Choix d'une carte aléatoire
        # TODO : Choisir les meilleures cartes à drafter
        print("PICK " + str(board.evaluateCard()))
>>>>>>> 6c05901dcb3ac4eb71ef5b42113fdb5aa67f4677

        # Jouer après le draft
    else:
<<<<<<< HEAD
        print("_________Start of turn : " + str(turnCount) + "____________", file=sys.stderr, flush=True)

        # print("Card to play:", cardToPlay, "then player mana:", player.mana, file=sys.stderr, flush=True)
        # print("choseCardToSummon:", board.choseCardToSummon(cardToPlay), file=sys.stderr, flush=True)
        # print("Evualate summon to play : " + board.evaluateSummonPlay(),  file=sys.stderr, flush=True)

=======
        # Jouer après le draft
        cardToPlay = board.evaluateCardPossibleToPlay(player.mana)
        print("Card to play:", cardToPlay, "then player mana:", player.mana, file=sys.stderr, flush=True)
        print("choseCardToSummon:", board.choseCardToSummon(cardToPlay), file=sys.stderr, flush=True)
        print("Evualate summon to play : " + board.evaluateSummonPlay(),  file=sys.stderr, flush=True)

>>>>>>> 6c05901dcb3ac4eb71ef5b42113fdb5aa67f4677
        print(board.doTurn())

    turnCount += 1
    board = None