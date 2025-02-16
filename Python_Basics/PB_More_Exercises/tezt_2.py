# class MyClass:
#     class_variable = 1
#
#     def __init__(self, instance_variable):
#         self.instance_variable = instance_variable
#
#
# first = MyClass(2)
# second = MyClass(3)
#
# print(MyClass.__dict__)  # {'__module__': '__main__', ... }
# print(first.__dict__)  # { 'instance_variable': 2 }
# print(second.__dict__)  # { 'instance_variable': 3 }

# ll = [f'{2 * 3} a']
#
# print(ll)

# ll += f'{3 * 12} b!!!'
#
# print(ll)


# class Person:
#     def __init__(self):
#         self.first_name = 'Peter'
#         self.last_name = 'Parker'
#         self.__some_prop = 'Ale'
#
#     def __full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def info(self):
#         return self.__full_name()
#
#
# person = Person()
# print(person.info())	              # Peter Parker
# # print(person.__full_name())	   # AttributeError
# print(person._Person__full_name())  # Peter Parker
# print(person._Person__some_prop)
#
# a = 5
# b = 6

# class Phone:
#     def __init__(self):
#         self.color = 'black'
#     def __getattr__(self, attr):
#         return attr.upper() + '!@#'
#
# phone = Phone()
# print(phone.color)            # None
# print(getattr(phone, 'size')) # None

#
# class Phone:
#     def __setattr__(self, attr, value):
#         self.__dict__[attr] = value.upper()
#         # self.attr = value.upper()  # RecursionError: maximum recursion depth exceeded while calling a Python object
#
#
# phone = Phone()
# phone.color = 'black!1'
# print(phone.color)  # BLACK
#


my_dict = {
    'a': 12,
    'b': 13,
    'c': 14,
    'd': 1,
    'e': 200,
    # 'f': 'some',  # TypeError: '>' not supported between instances of 'str' and 'int'
}

max_key = max(my_dict, key=my_dict.get)
min_key = max(my_dict, key=lambda x: -my_dict.get(x))
min_key_alt = min(my_dict, key=my_dict.get)

print(max_key)  # e
print(min_key)  # d
print(min_key_alt)  # d
print(min_key == min_key_alt)  # True

