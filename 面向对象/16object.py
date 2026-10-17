class Person(object):
    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender
# print(issubclass(Person, object))
# print(issubclass(int, object))
# print(issubclass(str, object))
# print(issubclass(list, object))
# print(issubclass(tuple, object))
# print(issubclass(bool, object))
# 因为 object 是所有类的父类，所以 Python 中的所有对象，都间接是 object 类的实例。
# p1 = Person('张三', 18, '男')
# print(isinstance(p1, object))
# print(isinstance(100, object))
# print(isinstance('hello', object))
# print(isinstance(True, object))
# print(isinstance(None, object))
# print(isinstance([10, 20, 30], object))

# for key in object.__dict__:
#     print(key)
# print(object.__dict__)
p1 = Person('张三', 18, '男')
print(dir(p1))