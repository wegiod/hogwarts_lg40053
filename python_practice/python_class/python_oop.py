class House:
    #静态属性->类变量（一定在类当中，在方法之外）
    door = "red"
    floor = "white"

    #构造函数，在类实例化的时候直接执行。每次实例化对象时，都会优先执行构造函数
    def __init__(self):
        #在构造函数或者方法中，调用类变量需要加上self.
        print(self.door)
        #实例变量，在类当中，方法当中，以self.变量名的方式来定义
        self.kitchen = "cook"


    #动态方法
    def sleep(self):
        #普通变量：类当中，方法当中，前面没有self
        bad = "席梦思"
        #在方法中定义实例变量
        self.table = "桌子上可以放东西"
        #普通变量可以在当前方法中调用
        print(f"在房子{bad}里睡觉")


    def cook(self,adb):
        self.adb = adb
        #调用构造函数中的实例变量
        print(self.kitchen)
        #调用方法中的实例变量
        print(self.table)
        print("在房子里可以吃饭")


#把类实例化
#北欧房子

north_house = House()

#中式房子

china_house = House()

#调用构造函数中的实例变量，也调用了方法中的实例变量，但是需要先调用sleep方法进行声明
north_house.sleep()
print(north_house.cook())

# #调用类属性
# print(House.door)
#
# #修改类属性
# House.door = "whith"
# print(House.door)
#
# #实例对象调用属性
#
# print(north_house.door)
#
# #修改实例对象属性,当类属性和对象属性同时修改时，按对象属性打印
# north_house.door = "bad"
# print(north_house.door)
# print(House.door)





