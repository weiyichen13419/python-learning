
class Person:
    max_age=120
    def __init__(self,name,age,idcard):
        self.name=name
        self._age=age
        self.__idcard=idcard


    # 注册 age 属性的 getter 方法：当访问 Person 实例的 age 属性时，age方法会自动调用
    @property
    def age(self):
        return self._age

    # 注册 age 属性的 setter 方法：当给 Person 实例的 age 属性赋值时，age方法会自动调用
    @age.setter
    def age(self,value):
        if value<=Person.max_age:
           self._age=value
        else:
            print('年龄非法，已将年龄变为最大值120')
            self._age = 120

    @property
    def idcard(self):
        return self.__idcard[:6]+'********'+self.__idcard[-4:]

    @idcard.setter
    def idcard(self,value):
        print('抱歉，身份证号码不允许修改')

p1 = Person('张三', 18, '110101199001011234')
print(p1.age)
p1.age=22
print(p1.age)
p1.idcard=111
print(p1.idcard)