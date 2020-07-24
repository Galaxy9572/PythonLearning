# Person类定义
class Person:
    # 初始化方法
    def __init__(self, name):
        # 将外部传来的name赋值给Person类的__name属性，__开头的属性是私有的
        self.__name = name

    # 定义人洗衣服的方法
    def wash_cloth(self, cloth_number, washer):
        print("%s打开洗衣机盖子，放进%d件衣服" % (self.__name, cloth_number))
        print("%s放进洗衣液" % self.__name)
        # 人通过调用washer的wash_cloth方法来达到洗衣服的目的
        washer.wash_cloth(cloth_number)
        print("%s打开洗衣机盖子，拿出衣服" % self.__name)

    # 因为__name是私有属性，所以要定义公开的一个方法让外界能访问到
    def get_name(self):
        return self.__name

    # 因为__name是私有属性，所以要定义公开的一个给__name设置值的方法让外界能给__name赋值
    # 把__name改为name也行（变为公开的）只不过没这么安全，因为别人可以随便改值，不经过校验
    def set_name(self, name):
        if len(name) == 0:
            print("非法的名字")
            return
        self.__name = name


class Washer:

    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity

    def wash_cloth(self, cloth_number):
        if cloth_number > self.capacity:
            print("衣服太多了，放不下")
            return
        self.pour_water()
        print("洗衣机洗衣服")
        self.dehydration()
        self.drain()
        print("衣服洗完了")

    def pour_water(self):
        print("洗衣机倒水")

    def dehydration(self):
        print("脱水")

    def drain(self):
        print("排水")


class HaierWasher(Washer):
    def __init__(self, brand, capacity, color):
        super().__init__(brand, capacity)
        self.__color = color

    def wash_cloth(self, cloth_number):
        if cloth_number > self.capacity:
            print("衣服太多了，放不下")
            return
        self.pour_water()
        print("洗衣机洗衣服")
        self.dehydration()
        self.drain()
        self.__drying()
        print("衣服洗完了")

    def __drying(self):
        print("烘干")


if __name__ == "__main__":
    p = Person("lsy")
    # washer = Washer("海尔", 10)
    washer = HaierWasher("海尔", 10, "白色")
    p.wash_cloth(5, washer)
