#自行车类

class Bicycle:
    #调用时显示骑行里程km，（km为传入的数字）
    def run(self,km):
        #使用f读取参数
        print(f"一共用脚骑行了{km}公里，累了累了")

bike = Bicycle()
#传入参数（km）
bike.run(10)

#继承Bicycle的属性，把父类名称放在类名后面的小括号中
class EBicycle(Bicycle):
    #属性需要传参定义，可以直接放到构造函数中。
    #传参直接放入括号中，用self.参数名 = 参数名的形式进行传参
    def __init__(self,valume):
        #当前电量为 self.valume 度电
        self.valume = valume

    #充电的方法
    def fill_charge(self,vol):
        #充电后的电量是多少
        self.valume = self.valume + vol
        #打印充了多少电，充完电是多少电
        print(f"冲了{vol}度电，现在的电量为{self.valume}")

    def run(self,km):
        #获取目前电量所能电动骑行的最大里程数
        power_km = self.valume * 10

        #做判断当前电量
        if power_km >= km:
            print()

ebike = EBicycle(1)

ebike.fill_charge(20)


