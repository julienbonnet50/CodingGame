import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Hand:
    def __init__(self):
        self.cards = []

    def evaluateCardPossibleToPlay(self, mana):
        cardsNumberToPlay = []
        for card in self.cards:
            if card.cost <= mana and card.location == 0:
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
        allySummoned = []
        ennemieSummoned = []
        actionForSummon = ""
        for card in self.cards:
            if card.instanceId == 1:
                allySummoned.append(card)
            if card.instanceId == -1:
                ennemieSummoned.append(card)
        if len(allySummoned) > 1 and len(ennemieSummoned) < 1:
            for card in allySummoned:
                actionForSummon = actionForSummon + "ATTACK " + card.instanceId + " -1;"
        elif len(allySummoned) > 1 and len(ennemieSummoned) > 1:
            for card in allySummoned:
                actionForSummon = actionForSummon + "ATTACK " + card.instanceId + " " + ennemieSummoned[random.randint(0, len(ennemieSummoned))].instanceId

        return actionForSummon

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

    def __str__(self):
        return (f"CardNumber: {self.cardNumber}, InstanceId: {self.instanceId}, Location: {self.location}, "
                f"CardType: {self.cardType}, Cost: {self.cost}, Attack: {self.attack}, "
                f"Defense: {self.defense}, Abilities: {self.abilities}, "
                f"MyHealthChange: {self.myHealthChange}, OpponentHealthChange: {self.opponentHealthChange}, "
                f"CardDraw: {self.cardDraw}")


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
    hand = Hand()
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
        hand.addCard(currentCard)

    for i in range(2):
        print(player, file=sys.stderr, flush = True)

    for card in hand.cards:
        print(card, file=sys.stderr, flush=True)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

        # Phase de Draft
    if turnCount < 30:
        # Choix d'une carte aléatoire
        print("PICK " + str(hand.evaluateCard()))

    else:
        # TODO: Jouer après le draft
        cardToPlay = hand.evaluateCardPossibleToPlay(player.mana)
        print("Card to play:", cardToPlay, "then player mana:", player.mana, file=sys.stderr, flush=True)
        print("choseCardToSummon:", hand.choseCardToSummon(cardToPlay), file=sys.stderr, flush=True)
        print(hand.printSummon(hand.choseCardToSummon(cardToPlay)) + ";" )

        print("Evualate summon to play : " + hand.evaluateSummonPlay(),  file=sys.stderr, flush=True)

    turnCount += 1
    hand = None