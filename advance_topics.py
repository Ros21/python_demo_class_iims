list1=["a","d","e","f","g","h","i","j"]
for index, item in enumerate(list1, start=10):
    print(f"Item {index}: {item}")


# languages = ['Python', 'Java', 'JavaScript']
# # enumerate the list
# enumerated_languages = enumerate(languages)
# print(list(enumerated_languages))









#
#
#
#
#
#
#
#
#
# def describe_person(name, age, *hobbies, **traits):
#     print("Name:", name)
#     print("Age:", age)
#     print("Hobbies:", hobbies)
#     # print("Traits:", traits)
#     for key,value in traits.items():
#         print(f"{key} is {value}")
#
#
#
# describe_person("Ram", 25, "Reading", "Gaming", height="5'10", eye_color="brown")
#
#
#
#
#



# def add(*args):
#     sum = 0
#     for num in args:
#         sum+=num
#     return sum
#
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4,5))
# print(add(1, 2, 3, 4,5,10))






#
# def demo_func( str1, *args, **kwargs):
#     print(f"String1: {str1}")
#     print("Args:", args)
#     print("Kwargs:", kwargs)
#
# demo_func( "Ram", 20,30, name="Ram", age=25)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #
# # gen = (x**2 for x in range(5))
# # print(gen) # object 0
# # for val in gen:
# #     print(val)
# #
# #
# # squares = [x**2 for x in range(5)]
# # print(squares)# [0,1,4,9,16]
# # for val in squares:
# #     print(val)
#
#
#
#









# def my_generator():
#     # return 1
#     yield 1
#     yield 2
#     yield 3
#
#
# gen = my_generator()
# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3
# print(next(gen))
# next(gen) #now raises StopIteration
#
# # for i in gen:
# #     print(i)
#
# #
# #
# #
# #
#
#
#



















from pydoc import classname

#
# class Paginator:
#     def __init__(self, data, page_size):
#         self.data = data
#         self.page_size = page_size
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         start = self.index
#         end = self.index + self.page_size
#         self.index += self.page_size
#         return self.data[start:end]
#
# results = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7"]
# pager = Paginator(results, 2)
# for page in pager:
#     print("Page:", page)




















# class CountDown:
#     def __init__(self, start):
#         self.num = start
#
#     def __iter__(self):
#         return self  # Iterator object
#
#     def __next__(self):
#         if self.num <= 0:
#             raise StopIteration
#         self.num -= 1
#         return self.num
#
# cd = CountDown(3)
# print(next(cd))
#
# for number in cd:
#     print(f"Num: {number}")

"""
Create a pagination search results (3 at a time) using Iterator
# Example usage
results = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7"]
pager = Paginator(results, 3)
for page in pager:
    print("Page:", page)
"""











#
# def describe_person(name, age, *hobbies, **traits):
#     print(f"Name: {name}, Age: {age}")
#     print("Hobbies:", hobbies)
#     print("Traits:")
#     for trait, value in traits.items():
#         print(f"  {trait}: {value}")
#
# describe_person("Ram", 25, "Reading", "Gaming", height="5'10", eye_color="brown")
#
#
#





# class Paginator:
#     def __init__(self, data, page_size):
#         self.data = data
#         self.page_size = page_size
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         start = self.index
#         end = self.index + self.page_size
#         self.index += self.page_size
#         return self.data[start:end]
#
# # Example usage
# results = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7"]
# pager = Paginator(results, 3)
#
# for page in pager:
#     print("Page:", page)
#
# # Output:
# # Page: ['Item1', 'Item2', 'Item3']
# # Page: ['Item4', 'Item5', 'Item6']
# # Page: ['Item7']
