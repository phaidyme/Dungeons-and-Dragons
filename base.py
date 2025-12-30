import random

random.seed(0)  # want the rolls to be the same each time

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
        self.dice = dice
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
            "initiative": {
                "ability": "dexterity", "proficiency": 0
            },
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
        print(f" - attacking with {weapon.name}")

        attack_roll = D(20, advantage, disadvantage)
        
        if attack_roll == 1:
            print("   critical miss :(")
            return
        
        damage = sum([
            self.get_modifier("dexterity"),
            self.proficiency_bonus,
            sum([D(die) for die in weapon.dice]),
            weapon.plus
        ])
        
        if attack_roll == 20:
            print("   critical hit!")
            critical = sum([
                self.get_modifier("dexterity"),
                self.proficiency_bonus,
                sum(weapon.dice),
                weapon.plus
            ])
            print(f"   {damage} + {critical} = {damage + critical} damage")
        else:
            print(
                f"   rolled {attack_roll},",
                (
                    attack_roll
                    + self.get_modifier('dexterity')
                    + self.proficiency_bonus
                    + weapon.plus
                ),
                "to hit"
            )
            print(f"   {damage} damage")
        return attack_roll
    def get_modifier(self, ability):
        return int((getattr(self, ability) - 10) / 2)
    def roll(skill, advantage = False, disadvantage = False):
        n = D(20, advantage, disadvantage)
        modifier = self.get_modifier(self.skills[skill]["ability"])
        bonus = self.proficiency_bonus + self.skills[skill]["proficiency"]
        result = n + modifier + bonus
        print(f"rolled {result} for {skill} ({n} + {modifier} + {bonus})")
        return result
    def long_rest(self):
        self.curr_hp = self.full_hp
        self.hit_dice = self.level
    def short_rest(self):
        print(" - short rest")
        i = self.hit_dice
        n = 0
        total_healed = 0
        while(self.hit_dice > 0 and self.curr_hp + 10 < self.full_hp):
            healing = D(10) + self.get_modifier("constitution")
            self.hit_dice -= 1
            self.curr_hp += healing
            n += 1
            total_healed += healing
        print(f"   used {n}/{i} hit dice to heal {total_healed} HP")
