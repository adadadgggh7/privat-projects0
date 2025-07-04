from multiprocessing.reduction import duplicate

#1Write a Python program to take the even numbers from a given list  and put into another list
# first_list = [1,5,6,2,3,4,7,8,]
# second_list = []
# x = 0
# for i in first_list:
#     x = i % 2
#     if x == 0:
#         second_list = second_list + [i]
# print(second_list)

#2 Write a Python program to find the second largest number in a list

# first_list = [1,5,6,2,3,4,7,8,]
# x = max(first_list)
# first_list.remove(x)
# i = max(first_list)
# print(i)

#3 Write a Python script that takes a list and
# removes two duplicate numbers from a given list.
# ex. [1, 1, 5] , >>> [5]   use list.count() method

# first_list = [1,1,5,55]
# second_list = []
# for i in first_list:
#     x = first_list.count(i)
#     if x <= 1:
#         second_list = second_list + [i]
# print(f'>>{second_list}')

#4Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains
# only the elements that are common between
# the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# duplicate = []
# for x in a:
#     if x in a and b and x not in duplicate:
#             duplicate.append(x)
# print(duplicate)

#5Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]  and write a program
# that prints out all the elements of the list that are less than given number (number will provide the user)

# x = int(input('insert your number\n'))
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# d = []
# for i in a:
#     if x > i:
#         d = d + [i]
# print(d)