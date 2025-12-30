from base import *

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
    "quiver": {
        "arrow": 50,
    },
    "backpack": {
        "bedroll": 1,
        "blanket": 1,
        "mess kit": {
            "cup": 1,
            "simple cutlery": 1,
            "cooking pan": 1,
            "shallow bowl": 1
        },
        "waterskin": 1,
        "rations": 10,
        "hempen rope": 50,
        "chain": 10,
        "soap": 1,
        "whetstone": 1,
    }
}
karla.clothes = "common clothes"
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
karla.superiority_dice = 4
karla.maneuvers = [
    "commander's strike",
    "riposte",
    "trip attack"
]
# one artisan's tools and one fighter skill proficiency
karla.skills["perception"]["proficiency"] = 1
karla.skills["smith`s tools"] = {
    "ability": "strength", "proficiency": 1
}

# level 4
karla.level = 4
karla.full_hp += 6 + 3
# ASI
karla.dexterity += 2

karla.long_rest()

print("----- inventory -----")
print_dict(karla.inventory)
print("---------------------")
print('',
    karla.gold, "gold,",
    karla.silver, "silver,",
    karla.copper, "copper"
)
print(f" {karla.curr_hp} / {karla.full_hp} HP, {karla.hit_dice} hit die")
print(f" {karla.get_ac()} AC + {karla.shield.base_ac} with shield")
print(f" {karla.superiority_dice} superiority dice")
print(" maneuvers:", ', '.join(karla.maneuvers))
