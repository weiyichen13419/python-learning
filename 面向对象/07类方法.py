#定一个Person类
from 基础.leixing import name


class Person:
    max_age=120
    planet='地球'
#初始化
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
 # 下面的speak方法、run方法，都保存在类身上，但他们主要是供实例调用，所以他们都叫：实例方法
    # 自定义方法（给实例添加行为）
    def speak(self,msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

    def run(self,distance):
        print(f'{self.name}疯狂游行了{distance}米')


 # 使用 @classmethod 装饰过的方法，就叫：类方法，类方法保存在类身上的
    # 类方法收到的参数：当前类本身（cls）、自定义的参数
    # 因为收到了cls参数，所以类方法中是可以访问类属性的def
    # 类方法通常用于实现：与类相关的逻辑，例如：操作类级别的信息、一些工厂方法
    @classmethod
    def change_planet(cls,value):
        cls.planet=value


    @classmethod
    def test2(cls):
        print('我是test2')


Person.change_planet('月球')
print(Person.__dict__)

