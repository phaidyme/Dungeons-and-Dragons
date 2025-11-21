import random

random.seed(0)  # want the rolls to be the same each time


"black spider"

"cragmoar castle"
"king grohl leads the cragmore tribe?"
"iiki goblin fren"
"iaino albric wizard headed to cragmore castle a while back"
"gundry rockseeker has two brothers"
"	nundrow youngest & thardin oldest"
"wave echo cave"
"sildar retired knight of the lords' alliance"
"	forge of spells is made in wave echo cave inside phandaline"
"	orcs raided the city reinforced by merc wizards"
"	battle destroyed the cave"
"	gildar wanted to find the cave he had a map"
"	phandaline was rebuilt and the cave was found by the rockseeker brothers"
"	sildar is looking for the wizard iaino"
AC = 18 + 1 + 2


gold = 20  # unit is gold coins
gold += 10  # for delivering supplies to barthen in phandaline
gold += 2  # thora refused his reward so it was split amongst the party

# paid for room
gold -= 1
silver = 5

inv = {
    "chainmail": 1,
    "immovable rod halberd": 1,
    "smithing apron": 1,
    "handaxe": 1,
    "longsword": 1,
    "explorer's backpack": {
        "bedroll": 1,
        "mess kit": 1,
        "tinderbox": 1,
        "waterskin": 1,
        "torch": 10,
        "rations": 10,
        "hempen rope": 50,  # feet
    },
}
# toblin stonehill owns and trileena are married

# athkatlar

inv.update({"full-plate armour +1": 1})
inv.pop("chainmail")
inv["shield"] = 1

max_HP = 20


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

STR, DEX, CON, INT, WIS, CHA = [
    int((thing - 10) / 2) for thing in [
        14 + 2,
        13,
        13 + 1,
        10,
        8,
        14
    ]
]
proficiency = 2


def D(n, modifier=0, advantage=False, disadvantage=False):
    a = random.randrange(n) + 1
    b = random.randrange(n) + 1
    if advantage:
        n = max(a, b)
    elif disadvantage:
        n = min(a, b)
    else:
        n = a
    n += modifier
    return n


def attack():
    print("_" * 20)
    n = D(20)
    longsword = D(8) + STR
    halberd = D(10) + STR
    handaxe = D(6) + STR

    longsword += 2  # dueling fighting style
    longsword += 1  # +1 longsword

    if n == 20:
        print("critical hit!")
        longsword += 8 + STR
        halberd += 10 + STR
        handaxe += 6 + STR

        longsword += 2  # dueling fighting style
        longsword += 1  # +1 longsword
    else:
        print(f"rolled {n}, {n + STR + proficiency} to hit")

    print(f"longsword : {longsword} slashing damage")
    print(f"halberd: {halberd} piercing/slashing damage")
    print(f"handaxe: {handaxe} slashing damage")
    print("_" * 20)


# contents of journal of ?:
#   b/w clans of dwarfs and gnomes
#   rich mine in wave echo cave
#   contained great magical power
#   called "the forge of spells"
#   humans joined after discovery
#   began to channel and bind that power to create the forge
#   used to make magical items
#   good times all 'round
#   raided by orcs reinforced by evil wizards
#   in that battle the cave was destroyed
#   and its location was lost
#   magical mace named lightbringer comissioned by lathander priests
#   glass staff is keanu reaves


# found a wooden chest next to the corpses in red brandit cave
inv["longsword +1"] = 1
inv.pop("longsword")
gold += 24
silver += 32
# ilya's cut
gold += 24
silver += 32

# found another wooden chest in glass staff's room
gold += 26
silver += 32

# found in the gambling room
electrum = 4
gold += 3
silver += 11
copper = 15

# reward from sildar for turning in keanu
gold += 40

# LEVEL UP (lvl 3)
# bane and hunter's mark permanently prepared
# smite: extra 2d8 radiant damage, 3d8 for fiend or undead, +1d8 per extra level
# 1 free divine smite per long rest
# 2 channel divinity charges per long rest: divine sense, vow of emnity
# Every time I attack, I can use channel divinity to vow of emnity on an enemy within 30 feet, gives me advantage for 1 minute
# 4 prepared spells
# 3 lvl 1 spell slots
max_HP = 27
HP = max_HP

# prepared spells:
# - cure wounds
# - heroism
# - command
# - compelled duel

# paid for food from Ilya's cut
gold -= 1

# owlbear fight
HP -= 11
inv["owlbear head"] = 1
HP = max_HP

# red boulbous things on the ground turned into wings
print("initiative", D(20, DEX))

attack()  # handaxe throw

# making a fire
print("survival", D(20, WIS))

# goblin ambush before sleeping
print("initiative", D(20, DEX))

HP -= 5

HP = max_HP

# phaelis' sword, day 3
print("smith", D(20, STR+proficiency, advantage=True))

# tree fight tree fight tree fight tree fiiiiight whoohoo
print("initiative", D(20, DEX))
HP -= 6
attack()
HP -= 3
HP -= 5
HP += D(10) # short rest

# reidoth is a druid of the emerald enclave (silvanus?)

# shambling
print("initiative", D(20, DEX))
HP -= 15
attack()
HP += 15 # lay on hands

print("cure wounds Ilya", D(8, CHA))
print("cure wounds Thora", D(8, CHA))

# long rest
HP = max_HP
ss_1 = 3
lay_on_hands = 15
# prepared spells:
# - cure wounds
# - bless
# - command
# - compelled duel

# favric is boss of dragon cult
lay_on_hands -= 2 # joe mama
print("insight", D(20, CHA+proficiency))
print("insight", D(20, CHA+proficiency))
print("initiative", D(20, DEX))
# dragon's name is venomfang

# we're going into another goddamned house??
print("perception", D(20, WIS))
print("initiative", D(20, DEX))
attack()

print("insight", D(20, WIS+proficiency)) # boar outside dragon lair

# DRAGON TIME DRAGON TIME DING DING DING DING :3
print("initiative", D(20, DEX))
attack()
attack() # advantage from vow of emnity
attack() # opportunity
attack()
attack() # advantage from vow of emnity
attack()
attack() # advantage from vow of emnity

gold += 30
silver += 160

lay_on_hands -= 13

inv["emblazened dwarven shield"] = 1
inv["Morrodin's Amulet of the Devout"] = 1
inv.pop("shield")

HP -= 3 + 7 # fell down trap

print("initiative", D(20, DEX)) # invisible
print("intelligence", D(20, INT))
print("perception", D(20, WIS))
print("animal handling", D(20, WIS))
print("const save", D(20, CON)) # grapple
HP -= 6 # thunder
HP -= 11 # force
print("death save", D(20))
print("animal handling", D(20, WIS))
print("horsey hit", D(20, 5, disadvantage=True))
print("horsey hit DM rolled 17+5")
print("horsey damage", D(8,3))
print("death save", D(20))
print("death save", D(20))
horsey_HP = 7
print("horsey hit", D(20, 5, advantage=True))
print("dex save against faelys fairy fire", D(20, 1))
HP = 1

print("perception", D(20, WIS))
print("dex save", D(20, DEX))
HP -= 7 # acid damage from trap
print("death save", D(20))
HP = 1

ss_1 -= 2
print("cure wounds", 2 * D(8) + 2) # Ilya
print("cure wounds", 2 * D(8) + 2) # Faelys


temp = D(10, 2)
print("short rest, HP +", temp)
HP += temp
temp = D(10, 2)
print("short rest, HP +", temp)
HP += temp
temp = D(10, 2)
print("short rest, HP +", temp)
HP += temp
hit_die = 0

print("animal handling", D(20, WIS))

# long rest
# - cure wounds
# - heroism
# - command
# - compelled duel
# - toll the dead
# - word of radiance
inv["ring of blessing"] = 1 # phaelis stole it off of a corpse
def cure_wounds():
    return D(8) + D(8)
    + CHA
    + D(4) # from ring of blessing
HP = max_HP
ss_1 = 3
lay_on_hands = 15
hit_die = 3

# GROHL
attack() # handaxe vs grohl
print("smite", D(8) + D(8))
print("initiative", D(20, DEX))

HP -= 8 # drow lady
attack() # sword vs drow lady
print("fire damage extra", D(4))

# level up to 4
# prepared: shield of faith
hit_die += 1
max_HP += 5
DEX += 1 # sentinel feat
lay_on_hands = 20
ss_1_max = 3

temp = D(10, 2)
print("short rest, HP +", temp)
HP += temp

print("initiative", D(20, DEX))
print("rollies", D(20))
print("table flip", D(20, STR))
attack()
attack()
lay_on_hands -= 5
print("lay on hands", D(4))
attack()
HP -= 5
attack()
print("goblin bodies", D(20, INT))
print("water", D(20, INT))
print("perception", D(20, WIS))
attack()
print("initiative", D(20, DEX))
lay_on_hands -= 5
print("lay on hands", D(4))
print("initiative", D(20, DEX))
print("perception", D(20, WIS))
attack()
HP -= 7
print("con save", D(20, CON))
HP -= 7
attack()
attack()
attack()
attack()
print("investigation", D(20, INT, advantage=True))
print("history", D(20, INT))
print("initiative", D(20, DEX))
print("history", D(20, INT))
print("intimidation", D(20, CHA))

# next session

print("investigation", D(20, INT))
print("survival", D(20, WIS))
print("cooking", D(20, WIS, advantage=True))
# long rest
HP = max_HP
ss_1 = ss_1_max

print("perception", D(20, WIS))

print('_'*50)
print_dict(inv)
print(gold, "gold")
print(silver, "silver")
print(copper, "copper")
print(HP, '/', max_HP, "HP,", hit_die, "hit die")
print(AC, "AC")
print("spell slots:", ss_1)
print("lay on hands", lay_on_hands)


#def attack(die, )
