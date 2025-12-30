import random

#random.seed(0)  # want the rolls to be the same each time

def print_dict(dictionary, level=0):
    dictionary = {
        key: dictionary[key] for key in sorted(list(dictionary.keys()))
    }
    for key, value in dictionary.items():
        if type(value) is dict:
            print(level * "  ", key)
            print_dict(value, level + 1)
        elif value == 1:
            print(level * "  ", key)
        else:
            print(level * "  ", value, "x", key)

def D(n, advantage=False, disadvantage=False):
    if advantage:
        return max(random.randrange(n) + 1, random.randrange(n) + 1)
    elif disadvantage:
        return min(random.randrange(n) + 1, random.randrange(n) + 1)
    else:
        return random.randrange(n) + 1

class Weapon:
    def __init__(self, name, dice, plus):
        self.name = name
        self.die = dice
        self.plus = plus
class Armour:
    def __init__(self, name, base_ac):
        self.name = name
        self.base_ac = base_ac
        
        
class Character:
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.level = 1
        self.proficiency_bonus = 2

        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        self.skills = {
            "acrobatics": {
                "ability": "dexterity", "proficiency": 0
            },
            "animal handling": {
                "ability": "wisdom", "proficiency": 0
            },
            "arcana": {
                "ability": "intelligence", "proficiency": 0
            },
            "athletics": {
                "ability": "strength", "proficiency": 0
            },
            "deception": {
                "ability": "charisma", "proficiency": 0
            },
            "history": {
                "ability": "intelligence", "proficiency": 0
            },
            "insight": {
                "ability": "wisdom", "proficiency": 0
            },
            "intimidation": {
                "ability": "charisma", "proficiency": 0
            },
            "investigation": {
                "ability": "intelligence", "proficiency": 0
            },
            "medicine": {
                "ability": "wisdom", "proficiency": 0
            },
            "nature": {
                "ability": "intelligence", "proficiency": 0
            },
            "perception": {
                "ability": "wisdom", "proficiency": 0
            },
            "performance": {
                "ability": "charisma", "proficiency": 0
            },
            "persuasion": {
                "ability": "charisma", "proficiency": 0
            },
            "religion": {
                "ability": "intelligence", "proficiency": 0
            },
            "slight of hand": {
                "ability": "dexterity", "proficiency": 0
            },
            "stealth": {
                "ability": "dexterity", "proficiency": 0
            },
            "survival": {
                "ability": "wisdom", "proficiency": 0
            },
        }
    def get_ac(self):
        return self.armour.base_ac + self.get_modifier("dexterity")

    def attack(self, weapon, advantage = False, disadvantage = False):
        print(f"---- attacking with {weapon.name}")

        attack_roll = D(20, advantage, disadvantage)
        
        damage =\
        self.get_modifier("dexterity")
        + self.proficiency_bonus
        + sum(D(dice) for dice in weapon.die)
        
        if attack_roll == 20:
            print("critical hit!")
            damage +=\
            self.get_modifier("dexterity")
            + self.proficiency_bonus,
            + sum(weaopn.die)
        else:
            print(
                f"---- rolled {attack_roll},",
                (
                    attack_roll
                    + self.get_modifier('dexterity')
                    + self.proficiency_bonus
                    + weapon.plus
                ),
                "to hit"
            )
        print(f"---- {damage} damage")
    def get_modifier(self, ability):
        return int((getattr(self, ability) - 10) / 2)
    def roll(skill, advantage = False, disadvantage = False):
        n = D(20, advantage, disadvantage)
        modifier = self.get_modifier(self.skills[skill]["ability"])
        bonus = self.proficiency_bonus + self.skills[skill]["proficiency"]
        result = n + modifier + bonus
        print(f"rolled {result} for {skill} ({n} + {modifier} + {bonus})")
    def long_rest(self):
        self.curr_hp = self.full_hp
        self.hit_dice = self.level
        

karla = Character(10, 15, 14, 14, 10, 8)
# custom tiefling
karla.dexterity += 2
karla.constitution += 1
# two proficiencies from background (noble)
karla.skills["history"]["proficiency"] = 1
karla.skills["persuasion"]["proficiency"] = 1
# three proficiencies from origin feat (skilled)
karla.skills["acrobatics"]["proficiency"] = 1
karla.skills["investigation"]["proficiency"] = 1
karla.skills["insight"]["proficiency"] = 1
# level 1 bonus ASI - thank you Kaia! <3
karla.dexterity += 1
karla.constitution += 1
# fighter hit die is D10
karla.full_hp = 10 + karla.get_modifier("constitution")
# starting gear is custom
karla.gold = 10
karla.silver = 0
karla.copper = 0
karla.inventory = {
    "common clothes": 1,
    "quiver": {
        "arrow": 50,
    },
    "backpack": {
        "bedroll": 1,
        "blanket": 1,
        "mess kit": 1,
        "waterskin": 1,
        "rations": 10,
        "hempen rope": 50,
        "chain": 10,
        "soap": 1,
        "whetstone": 1,
    }
}
karla.sword = Weapon("rapier", [8], 0)
karla.bow = Weapon("longbow", [8], 0)
karla.armour = Armour("studded leather", 12)
karla.shield = Armour("shield", 2)

# level 2
karla.level = 2
karla.full_hp += 6 + 3

# level 3
karla.level = 3
karla.full_hp += 6 + 3
karla.superiority_dice = 4
karla.maneuvers = [
    "commander`s strike",
    "riposte"
    "trip attack",
]
# one artisan's tools and one fighter skill proficiency
karla.skills["perception"]["proficiency"] = 1

# level 4
karla.level = 4
karla.full_hp += 6 + 3
karla.dexterity += 2

karla.long_rest()
karla.attack(karla.sword)

print_dict(karla.inventory)
print(
    karla.gold, "gold,",
    karla.silver, "silver,",
    karla.copper, "copper"
)
print(karla.curr_hp, '/', karla.full_hp, "HP,", karla.hit_dice, "hit die")
print(f"{karla.get_ac()} AC + {karla.shield.base_ac} with shield")
print(karla.superiority_dice, "superiority dice")
