import random

uesr1_hp = random.randint(100,4000)
uesr1_pows = random.randint(100,1000)
uesr2_hp = random.randint(100,4000)
uesr2_pows = random.randint(100,1000)

# print(uesr2_pows)
# print(uesr1_pows)
while True:
    uesr1_hp = uesr1_hp - uesr2_pows
    uesr2_hp = uesr2_hp - uesr1_pows


    if uesr1_hp <= 0:
        print(f"我的血量为：{uesr1_hp}")
        print(f"你的血量为：{uesr2_hp}")
        print("我输了")
        # print(uesr1_hp)
        # print(uesr2_hp)
        break
    elif uesr2_hp <= 0:
        print(f"我的血量为：{uesr1_hp}")
        print(f"你的血量为：{uesr2_hp}")
        print("我赢了")
        break