import random
import math
class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
    def ability(self):
        dice = []
        dice.append(random.randrange(1,6))
        dice.append(random.randrange(1,6))
        dice.append(random.randrange(1,6))
        dice.append(random.randrange(1,6))
        dice.sort()
        threeHighest =  dice[1] + dice[2] + dice[3]
        return threeHighest

def modifier(amt):
    return math.floor((amt - 10)/2) 