# 1 Rectangle Class
#Create a class Rectangle with width and height. Add methods to compute:
#area()
#perimeter()

# class Rectangle:
#     def __init__(self, width:int, height:int):
#         self.width = width
#         self.height = height
#     def get_area(self):
#         S = self.width * self.height
#         return f'{S}'
#     def get_perimeter(self):
#         P = 2 * (self.width + self.height)
#         return P
# Rectangle1 = Rectangle(25,30)
# print('area = ',Rectangle1.get_area())
# print('perimeter = ',Rectangle1.get_perimeter())

#2 Write a Python class named Circle constructed by a radius and
# two methods which will compute the area and the perimeter of a circle

# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def get_area(self):
#         return math.pi * (self.radius)**2
#     def get_perimeter(self):
#         return self.radius * math.pi * 2
# Circle1 = int(input('number '))
# Circle2 = Circle(Circle1)
# print(f'area {Circle2.get_area()}')
# print(f'perimetr {Circle2.get_perimeter()}')

#3 Student Class
# Create a class Student with name, age, and grades (a list). Add methods:
# add_grade(grade)
# average_grade()

# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.grades = []
#
#     def add_grade(self,grade):
#         return self.grades.append(grade)
#     def average_grade(self):
#         if not self.grades:
#             return 0
#         x = sum(self.grades)/len(self.grades)
#         return float(x)
#
# x = input(f'your name ')
# z = int(input('your age '))
# s = Student(x, z)
# Tr = True
# while Tr:
#     y = input('input grade if you wanna end press x ')
#     if y == 'x':
#         Tr = False
#     else:
#         l = int(y)
#         s.add_grade(l)
# print(f'self name {s.name} and age {s.age}')
# print(f'grade {s.grades}')
# print(f'averge grade {s.average_grade()} ')

#4 Create class Human which will be INITIALIZED
# with following attributes:
# Name, surname, age, height, weight, gender . And will have these methods:
# A method which will tel in which year the person will be 100 years old
# A method which will tell the optimal weight
# A method to present

class Human:
    def __init__(self,name,surname,age,height,weight,gender):
       self.name = name
       self.surname = surname
       self.age = age
       self.height = height
       self.weight = weight
       self.gender = gender
    def year_to_be_100(self):
        return 100 - self.age
    def optimal_weight(self):
        imt = (self.weight / self.height ** 2)
        return round(imt)
    def present(self):
        return f'Hello, I am {self.name}, {self.age} years old, {self.gender}.'


n = input('hello what your name ')
s = input('your surname ')
a = int(input('age '))
h = int(input('height '))
w = int(input('weight '))
g = input('gender (M/F) ')
if g not in ['m','M','male','f','F','famale']:
        print('wrong gender')
else:
    H = Human(n,s,a,h,w,g)
print(f'person will be 100 years old after {H.year_to_be_100()} years later')
print(f'optimal weight for you {H.optimal_weight()}')
print(f'{H.present()}')