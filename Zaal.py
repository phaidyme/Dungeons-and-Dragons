import random

random.seed()


def mod(ability_score):
    return (ability_score - 10) // 2


def athletics():
    return mod(str)


def acrobatics():
    return mod(dex) + profficiency


def sleight_of_hand():
    return mod(dex)


def stealth():
    return mod(dex)


def arcana():
    return mod(int)


def animal_handling():
    return mod(wis)


def insight():
    return mod(wis) + profficiency


def medicine():
    return mod(wis) + profficiency


def perception():
    return mod(wis)


def survival():
    return mod(wis)


def deception():
    return mod(cha)


def intimidation():
    return mod(cha)


def performance():
    return mod(cha)


def persuasion():
    return mod(cha) + profficiency


def d20():
    return random.randint(1, 20)


def roll(stat):
    return d20() + stat()


str = 8
dex = 14
con = 15
int = 10
wis = 12
cha = 15 + 2

# race: half-elf
movement = 20
vision = "dark vision: 60ft"
profficiency = 2

+10gp
spell scroll of magic stone
potion of healing
potion of climbing
wand of conducting
+50gp
