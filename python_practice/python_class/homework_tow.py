
import random

#定义天山童姥类

class TongLao():
    #输入我自己的生命值
    my_hp = eval(input("请输入你的生命值："))
    #敌人的生命值从100~400之间随机
    enemy_hp = random.randint(100,400)
    #输入我的攻击力
    my_power = eval(input("请输入你的攻击力："))
    #敌人的攻击力从100~400之间随机
    enemy_power = random.randint(100,400)

    #定义构造函数
    def __init__(self,name={}):
        #输入我的姓名
        self.name = name



    #定义people方法
    def see_people(self,name):
        self.name = name
        #传入参数WYZ,则打印"师弟！！！！"
        if self.name == "WYZ":
            print("师弟！！！！")

        #如果传入"李秋水"，则打印"师弟是我的！"
        elif self.name == "李秋水":
            print("师弟是我的！")

        #如果传入"丁春秋"打印"叛徒，我杀了你"
        elif self.name == "丁春秋":
            print("叛徒，我杀了你")



    #定义zms方法（天山折梅手），调用该方法，会将自己的武力值提升10倍，血量缩减2倍，需要传入敌人的HP,power，
    # 进行一回合对打，打完之后，双方血量的一方获胜。
    def zms(self):

       #将自己的攻击力提升10倍
        self.my_power = self.my_power * 10
       #打印我使用天山折梅手提升后的攻击力是多少
        print(f"我现在的攻击力是{self.my_power}")

       #将自己的血量减少两倍
        self.my_hp = self.my_hp / 2
       #打印我使用天山折梅手减少后的血量是多少
        print(f"我现在剩余的血量是{self.my_hp}")


        if self.enemy_hp - self.my_power <= 0:
            print("我赢了")
        elif self.my_hp - self.enemy_power <= 0:
            print("我输了")

#定义一个XuZun类，继承童姥。
class XuZun:
    #虚竹不想打架，只有念经（read）技能，每次调用都会打印"罪过罪过"
    def read(self):
        print("罪过罪过")

me = TongLao()

me.see_people(input("请输入姓名："))


me.zms()

ls = XuZun()
ls.read()