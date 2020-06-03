# class MyFirstClass:
#     pass


# my_first_instance = MyFirstClass()
# my_second_instane = MyFirstClass()

# print(my_first_instance)
# print(my_second_instane)
# print(MyFirstClass)

# class Student:
#     my_list = []
#     def _init_(self, first_name, last_name):
#        self.first_name = first_name
#        self.last_name = last_name
#        Student.my_list.append(self)

#     def _str_(self):
#         return f"This students name is {self.last_name}, {self.first_name}."

# me = Student("Juana", "Villalpando")
# you = Student("hello", "world")
# print(me.my_list)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return "hello"
#     def __repr__(self):
#         return f"Point(x({self.x}, y={self.y}))"

# my_point = Point(3, 5) 
# my_point.x=3
# my_point.y=5
# print(my_point)

# x = 1
# y = 2

# def my_function(x):
#     y = 3
#     print(x,y)

# my_function(10)
# print(x,y)

# print(pow(2,3))

# print(__name__)

# print(len('cat'))

# def my_function():
#     global x
#     x = 100

# my_function() #this needs to get called ,else it will not call the global x in the function. 
# print(x)

class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"{self.name}\n"
        for idx, category in enumerate(self.categories):
            output += " " + str(idx+1) + "." + category + "\n"

        return output

my_store = Store("The Dugout", ["Running", "Basebal", 'Basketball'])

print(my_store)

selection = input("Select the number of the department:")
print("The user selected " + str(selection))