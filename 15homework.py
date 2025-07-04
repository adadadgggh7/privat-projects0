#1 Write a Python script to concatenate following dictionaries to create a new one.
#Sample Dictionary :
#
# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50,6:60}
# dict4 = {6:60,7:70}
# print(dict3)
# list_dict = [dict1, dict2,  dict3 ,dict4]
# list_dict2 = { }
# for key in list_dict:
#     list_dict2.update(key)
# print(list_dict2)

#2 Try for as second version Write a Python script to generate and
# print a dictionary that contains a number
# (between 1 and n) in the form (x, x*x). Sample Dictionary ( n = 5) :


# number = int(input('sample dict: '))
# dict = {}
# x = 0
# while number > x:
#     x += 1
#     dict[x] = x*x
# print(dict)

#3 Write a Python program to drop empty Items from a given Dictionary. Original Dictionary: {'c1': 'Red', 'c2': 'Green', 'c3': None}

# dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# newdict = {}
# for key in dict:
#     if dict[key] is not None:
#         newdict[key] = dict[key]
# print(newdict)