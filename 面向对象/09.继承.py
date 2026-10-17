class Person:

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def speak(self,msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

# 定义一个Student类（子类、派生类）， 继承自Person类（父类、超类、基类）
class Student(Person):
    # def speak(self,msg):
    #     print('这是Student身上的speak方法',msg)
    def __init__(self,name,age,gender,rank,ind):
    #     #方式一(更推荐)
        super().__init__(name,age,gender)
    #     #方式二
    #     Person.__init__(self,name,age,gender)
        self.rank=rank
        self.ind=ind
        # print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我的修为是：{self.rank},我的身份是{self.ind}')
    def study(self):
        print(f'我的名字是{self.name},我在努力修行，争取到达{self.rank}')

s1=Student('古月方源',16,'男','三转','家老')
# print(s1.__dict__)
# print(type(s1))
s1.study()

# s1.speak('落魄谷中寒风吹')