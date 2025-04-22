from character import Enemy
fingleflop = Enemy("Fingleflop", "a towering dragon that uses its ears to fly")
fingleflop.describe()
fingleflop.set_weakness("music")
print(fingleflop.get_weakness())

fight_with = input("What will you fight with?")
fingleflop.fight(fight_with)



