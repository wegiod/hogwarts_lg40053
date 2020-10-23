
#定义fight函数实现游戏逻辑
def fight():
    #定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    #定义最终血量计算方式
    my_fight_hp = my_hp - enemy_power
    enemy_fight_hp = enemy_hp - my_power

    #三目运算，判断输赢
    #只有简单的if可以使用三目运算，本质上来说只是语法简介了一些
    print("我赢了")if my_fight_hp > enemy_fight_hp else print("我输了")

fight()
