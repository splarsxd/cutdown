import os

# league of legends calculator for cutdown and coup de grace made by splars#1252

maxhp = int(input("Health: "))
hp = maxhp
cdg_maxhp = maxhp
cdg_hp = maxhp
ad = int(input("Attack Damage: "))
count = 0
cdg_count = 0

print("Cut Down | Coup de Grace")
while True:
    if hp > (maxhp * 0.6):
        hp -= (ad * 1.08)
        count += 1
    else:
        hp -= ad
        count += 1

    if cdg_hp < (cdg_maxhp * 0.4):
        cdg_hp -= (ad * 1.08)
        cdg_count += 1
    else:
        cdg_hp -= ad
        cdg_count += 1

    print(f"HP: {round(hp)}/{round(maxhp)} | {round(cdg_hp)}/{round(cdg_maxhp)} | Difference HP: {round(cdg_hp-hp)}, Hits: {count}")
    if hp <= 0 and cdg_hp <= 0:
        break

os.system("pause >nul")
