def attack(dice, bonus, advantage=False):
    print()
    if isinstance(dice, int):
        # if only one die, convert to list for rest of logic
        dice = [dice]
    n = D(20, advantage=True)
    damage = STR + bonus + sum([D(n) for n in dice])
    if n == 20:
        print("critical hit!")
        damage += STR + bonus + sum([n for n in dice])
    else:
        print(f"rolled {n}, {n + STR + proficiency} to hit")
    print(damage, "damage")
    