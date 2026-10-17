# class Person:
#
#     def __init__(self,name,age,idcard):
#         self.name=name  #公有属性：当前类中，子类中，类外部都可以访问
#         self._age=age     # 受保护属性：当前类内部、子类内部，可以访问
#         self.__idcard=idcard  # 私有属性：仅能在当前类内部访问
#     def speak(self):
#         print(f'我叫{self.name},年龄{self._age},身份证{self.__idcard}')
# # p1 = Person('张三', 18, '110101199001011234')
# # p1.speak()
# class Student(Person):
#     def hello(self):
#         print(f"我叫：{self.name}，年龄：{self._age}")
# p1 = Person('张三', 18, '110101199001011234')
# # print(p1.name)
# # # 注意：如果在类的外部，强制访问【受保护的属性】，也能访问，但最好别这么做
# # print(p1._age)
# # 强制访问【私有属性】会报错
# # print(p1.__idcard)

class Person:
    def __init__(self,name,age,idcard):
        self.name=name
        self._age=age
        self.__idcard=idcard
    def speak(self):
     print(f'我叫{self.name},年龄{self._age},身份证{self.__idcard}')
p1=Person('zhangsan',18,'110')
p1.speak()
class Student(Person):
    def hello(self):
        print(f"我叫：{self.name}，年龄：{self._age}")
p2=Student('zhangsan',18,'110')
p2.hello()
