import random
enufrom enum import Enum
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
    return (amt - 10)//2 
isRandom = 0

class consoleClass: 
     print("Would you like a random charecter? y or n")
     randomAnswer = input()
     if randomAnswer == "y":
        isRandom = 1
     else:
         print("please choose a race 1) Elf 2) Human 3) Dwarf 4) Hafling 5) Dragonborn 6) Halfelf 7) Halfork 8) Tiefling")
         class Race(enum)
            Elf = 1
            Human = 2
            Dwarf = 3
            Halfling = 4
            Dragonborn = 5
            Halfelf = 6
            Halfork = 7
            Tiefling = 8
         print("please chosse a class 1) Barbarian 2) Bard 3) Cleric 4) Druid 5) Fighter 6) paladin 7) Ranger 8) Rouge 9) Wizard")
         class characterClass(enum)
             Barbarian = 1
             Bard =2
             Cleric =3
             Druid =4
             Fighter = 5
             paladin = 6
             Ranger = 7 
             Rouge = 8
             Wizard = 9