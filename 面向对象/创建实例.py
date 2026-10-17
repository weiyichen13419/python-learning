#定一个Person类
class Person:
#初始化
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

## 创建Person的实例对象
p1=Person('魏依辰',20,'男')
p2=Person('古月方源',20,'男')

# 如果直接打印一个实例的话，我们是看不到实例身上的属性的
# print(p1)
# print(p2)

# 通过点语法可以访问或修改实例身上的属性
print(p1.name,p1.age,p1.gender)
print('-'*20)
print(p2.name,p2.age,p2.gender)
p1.name='白凝冰'
# 通过 实例.__dict__ 可以查看实例身上的所有属性
print(p1.__dict__)

# 实例创建完毕后，依然可以通过 实例.属性名 = 值 去给实例追加属性
p2.address='古月山寨'
print(p2.__dict__)

# 通过type函数，可以查看某个实例对象，是由哪个类创建出来的
print(type(p1))
print(type(p2))