import random

random.seed(0) # want the rolls to be the same each time

def print_dict(dictionary, level=0):
    keys = sorted(list(dictionary.keys()))
    nested_keys = []
    numbered_keys = []
    single_keys = []
    for key in keys:
        if type(dictionary[key]) is dict:
            nested_keys.append(key)
        elif dictionary[key] > 1:
            numbered_keys.append(key)
        else:
            single_keys.append(key)
    keys = single_keys + numbered_keys + nested_keys
    for key in keys:
        value = dictionary[key]
        if type(value) is dict:
            print(level * "  " + key)
            print_dict(value, level + 1)
        elif value == 1:
            print(level * "  " + key)
        else:
            print(level * "  " + str(value), "x", key)

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

class Skill:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def __str__(self):
        return self.name    

initiative = Skill("initiative", "dexterity")

athletics = Skill("athletics", "strength")

acrobatics = Skill("acrobatics", "dexterity")
sleight_of_hand = Skill("sleight_of_hand", "dexterity")
stealth = Skill("stealth", "dexterity")

arcana = Skill("arcana", "intelligence")
history = Skill("history", "intelligence")
investigation = Skill("investigation", "intelligence")
nature = Skill("nature", "intelligence")
religion = Skill("religion", "intelligence")

animal_handling = Skill("animal_handling", "wisdom")
insight = Skill("insight", "wisdom")
medicine = Skill("medicine", "wisdom")
perception = Skill("perception", "wisdom")
survival = Skill("survival", "wisdom")

deception = Skill("deception", "charisma")
intimidation = Skill("intimidation", "charisma")
performance = Skill("performance", "charisma")
persuasion = Skill("persuasion", "charisma")

strength_save = Skill("strength save", "strength")
constitution_save = Skill("constitution save", "constitution")

def mod(ability_score):
    return int((ability_score - 10) / 2)
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

        self.proficiencies = {}
    def get_ac(self):
        return self.armour.base_ac + mod(self.dexterity)

    def attack(self, weapon, advantage = False, disadvantage = False):
        print(f" - attacking with {weapon.name}")

        attack_roll = D(20, advantage, disadvantage)
        
        if attack_roll == 1:
            print("   critical miss :(")
            return
        
        damage = sum([
            mod(self.dexterity),
            self.proficiency_bonus,
            sum([D(die) for die in weapon.dice]),
            weapon.plus
        ])
        
        if attack_roll == 20:
            print("   critical hit!")
            critical = sum([
                mod(self.dexterity),
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
                    + mod(self.dexterity)
                    + self.proficiency_bonus
                    + weapon.plus
                ),
                "to hit"
            )
            print(f"   {damage} damage")
        return attack_roll
    def roll(self, skill, advantage = False, disadvantage = False):
        n = D(20, advantage, disadvantage)
        modifier = mod(getattr(self, skill.ability))
        proficiency = self.proficiency_bonus * self.proficiencies.get(
            skill.name,
            0 # default to zero if don't have proficiency in skill
        )
        result = n + modifier + proficiency
        print(f"rolled {result} for {skill} ({n} + {modifier} + {proficiency})")
        return result
    def long_rest(self):
        self.curr_hp = self.full_hp
        self.hit_dice = self.level
        self.SuperiorityDice = self.mSuperiorityDice
    def short_rest(self):
        self.SuperiorityDice = self.mSuperiorityDice
        print(" - short rest")
        i = self.hit_dice
        n = 0
        total_healed = 0
        while(self.hit_dice > 0 and self.curr_hp + 10 < self.full_hp):
            healing = D(10) + mod(self.constitution)
            self.hit_dice -= 1
            self.curr_hp += healing
            n += 1
            total_healed += healing
        print(f"   used {n}/{i} hit dice to heal {total_healed} HP")

if __name__ == "__main__":
    n = int(1e5)

    print("flat D20 (should be 10.5)")
    print(sum([D(20) for i in range(n)]) / n)
    
    print("D20 with advantage (should be 13.825)")
    print(sum([D(20, advantage=True) for i in range(n)]) / n)

    print("D20 with disadvantage (should be 7.175)")
    print(sum([D(20, disadvantage=True) for i in range(n)]) / n)

    print(sum([-205,
        45, # studded leather
        10, # shield
        25, # rapier
        50, # longbow
        1, # arrows
        2, # backpack
        1, # bedroll
        5, # chain
        2, # traveler's clothes
        2, # crowbar
        2, # grappling hook
        0.02, # mess kit
        1, # quiver
        1, # rations
        1, # rope
        0.02, # soap
        0.2, # waterskin
        0.01, # whetstone
    ]))