#定一个Person类
class Person:
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

p1=Person('魏依辰',20,'男')
p2=Person('古月方源',20,'男')

# 通过实例调用实例方法
p1.speak('hello')
p1.run(200)

# 通过类去调用实例方法(能调用，但不推荐)
Person.run(p2,300)
