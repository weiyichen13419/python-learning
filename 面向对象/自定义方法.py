#定一个Person类
class Person:
#初始化
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
 # 自定义方法（给实例添加行为）
    # speak方法收到的参数是：调用speak方法的实例对象（self）、其它参数
    # speak方法只有一份，保存在Person类身上的，所有Person类的实例对象，都可以调用到speak方法
    def speak(self,msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

    def doing(self,action):
        print(f'我是{self.name}，接下来我要去{action}')
p1=Person('魏依辰','男',20)
p2=Person('古月方源','男',20)

# 验证一下：Person的实例对象身上是没有speak方法的
# print(p1.__dict__)
# print(p2.__dict__)
# 当执行p1.speak()的时候，查找speak方法的过程：1.实例对象自身(p1)  =>  2.实例的“缔造者”的身上(Person)
p1.speak('落魄谷中寒风吹')
p2.speak('春秋蝉鸣少年归')

p1.doing('学习python')
p2.doing('白骨山获得遗藏')

def doing():
    print('突破二转')
p1.doing=doing
p1.doing()

def speak():
    print('llll')
p1.speak=speak
print(p1.__dict__)
print(p2.__dict__)
p1.speak()