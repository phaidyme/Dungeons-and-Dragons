"""
  - tiefling (fiendish legacy)
  - family is working class but rich enough to hang out with nobility
  - family tries really hard to belong in that circle
    including hiding the racialised aspects of their appearance and demeanour

  - raised and trained from birth to become high ranked city guard
  - possibly had a rivalry/friendship with Ilya and felt jealousy towards her
    because of internalised racism
  - volunteered to track Ilya down, half because she was mad that Ilya dared
    abandon the life goal she thought they shared, half because she wanted
    to bring her friend back

  - dex based battle master fighter
  - duelling fighting style, "rapier" and shield
    rapier not bendy, more like a thin and light longsword
"""
from base import *

karla = Character(8, 15, 15, 10, 14, 8)
# fiendish legacy tiefling
karla.spells = ["fire bolt"]
# fighter
karla.proficiencies["perception"] = 1
karla.proficiencies["acrobatics"] = 1
# soldier background
karla.proficiencies["athletics"] = 1
karla.proficiencies["intimidation"] = 1
karla.dexterity += 2
karla.constitution += 1
# martial adept as origin feat
karla.mSuperiorityDice = [6]
karla.maneuvers = ["riposte", "trip"]
# level 1 bonus ASI - thank you Kaia! <3
karla.dexterity += 2
# fighter hit die is D10
karla.full_hp = 10 + mod(karla.constitution)
karla.gold = 56
karla.silver = 7
karla.copper = 5
karla.inventory = {
    "quiver": {
        "arrow": 20,
    },
    "backpack": {
        "bedroll": 1,
        "mess kit": {
            "cup": 1,
            "simple cutlery": 1,
            "cooking pan": 1,
            "shallow bowl": 1
        },
        "waterskin": 1,
        "rations": 10,
        "hempen rope": 50,
        "soap": 1,
        "whetstone": 1,
        "crowbar": 1
    },
    "chain": 10,
    "grappling hook": 1,
}
karla.clothes = "traveler's  clothes"
karla.armour = Armour("studded leather", 12)
karla.shield = Armour("shield", 2)

karla.sword = Weapon("rapier", [8], 0)
karla.bow = Weapon("longbow", [8], 0)

# level 2
karla.level = 2
karla.full_hp += 6 + 3

# level 3
karla.level = 3
karla.full_hp += 6 + 3
# from battlemaster fighter
karla.mSuperiorityDice += [8, 8, 8, 8]
karla.maneuvers += [
    "distracting strike",
    "commander's strike",
    "brace"
]
karla.proficiencies["history"] = 1
karla.proficiencies["woodcarver's tools"] = 1
# from fiendish legacy
karla.spells.append("hellish rebuke")

# level 4
karla.level = 4
karla.full_hp += 6 + 3
# skill expert feat
karla.dexterity += 1
karla.proficiencies["insight"] = 1
karla.proficiencies["perception"] = 2

karla.long_rest()
karla.roll(perception)

print(" inventory ".center(80, '-'))
print_dict(karla.inventory)
print(" status ".center(80, '-'))
print(f"{karla.gold} gold, {karla.silver} silver, {karla.copper} copper")
print(f"{karla.curr_hp} / {karla.full_hp} HP, {karla.hit_dice} hit die")
print(f"{karla.get_ac()} AC + {karla.shield.base_ac} with shield")
print("spells:", ', '.join(karla.spells), "(once per long rest)")
print("maneuvers:", ', '.join(karla.maneuvers))
print("superiority dice:", *(karla.SuperiorityDice))
