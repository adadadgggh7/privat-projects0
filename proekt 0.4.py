#.1 write a python program to check leap year without using datetime library

# year = int(input('enter year '))
# if year % 400 == 0 :
# 	print('leap')
# elif year % 100 == 0:
#     print(' not leap')
# elif year % 4 == 0:
#     print(' leap')
# else:
#     print('not leap')

#2 Write a python program to check whether a number is divisible by 5 or 11 or not.

# x = int(input('number '))
# if x % 5 == 0 and x % 11 == 0:
#     print("The number is divisible by both 5 and 11.") 
# elif x % 5 == 0:
#     print('The number is divisible by 5')
# elif x % 11 == 0:
#     print('The number is divisible by 11')       
# else:
#     print('not')
# #.3 Write an app that takes a number.  If the number is divisible by 3, it should return “Fizz”.  If it is divisible by 5, it should return “Buzz”.  If it is divisible by both 3 and 5, it should return “FizzBuzz”.  Otherwise, it should return the same number.

#  x = int(input('your number'))
#  if x % 15 == 0:
#  	print('fizzbuzz')
#  elif x % 3 == 0:
#  	print('buzz')
#  elif x % 5 == 0:
#  	print('fizz')
#  else:
#   print(x) 

#4 Write a Python program to find the first appearance of the substring ‘not’ and ‘poor’ from a given string, if ‘not’ follows the ‘poor’, replace the whole ‘not’...‘poor’ substring with ‘good’. Return the resulting string. 

# x = input('text ')
# not_ = x.find('not')
# poor = x.find('poor')
# if not_ >= 0 and poor > not_:
#     yz = x[not_:poor + 4]
#     y = x.replace(yz,'good')
#     print(y)
# else:
#     print(x)

#5 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to ‘$’, except the first char itself. Go to the editor

# x = input('text ')
# k = x[1:].replace(x[0],'$')
# kx = x[0]+k
# print(kx)
