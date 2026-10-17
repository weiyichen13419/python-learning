#定一个Person类
class Person:
    # max_age、planet 他们都是类属性，类属性是保存在类身上的
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性通常用于保存：公共数据
    max_age=120
    planet='地球'

    def __init__(self,name,age,gender):
        self.name=name
        self.gender=gender

        self.age = age
        if age<Person.max_age:
            self.age=age
        else:
            print(f'年龄超出范围了，已经将年龄设置为最大值：{Person.max_age}')
            self.age=Person.max_age
print(Person.__dict__)

p1=Person('魏依辰',20,'男')
p2=Person('古月方源',20,'男')
# print(Person.max_age)
# print(p1.age)
# print(p2.age)
# # 测试一下年龄超出范围
# p3=Person('大爱仙尊',500,'男')
# print(p3.age)
